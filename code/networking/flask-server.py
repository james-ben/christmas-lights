import os
import sys
import json
import time
import threading
from itertools import cycle
from datetime import datetime
from flask import Flask, request, render_template, send_from_directory

sys.path.append(os.path.abspath("../"))
from procedures import (twinkler, stripes,
                        strobe, columns,
                        blink)
from networking import input_parser
from light_utils import colors

# import the right kind based on the system
if "linux" in sys.platform:
	if os.getlogin() == "pi":
		from light_utils import grid
	else:
		from light_utils import fake_grid as grid
else:
	from light_utils import fake_grid as grid


# perhaps this will be changed in the future
app = Flask(__name__)
ts = None


class TreeServer(object):
	def __init__(self):
		self.grid = grid.Grid()
		# alias
		self.strand = self.grid

		# interrupt flags
		self.stopFlag = False
		self.timerInterrupt = False

		# procedure objects
		self.twinkler = twinkler.TwinkleLights()
		self.striper = stripes.StripeLights()
		self.strobe = strobe.StrobeLights()
		self.column = columns.ColumnLights()
		self.blinker = blink.BlinkLights()

		self.functionMap = {
			"twinkle": self.twinkler.run,
			"stripes": self.striper.run,
			"strobe": self.strobe.run,
			"columns": self.column.run,
			"blink": self.blinker.run,
		}

		# init the state
		self.procList = [{"name" : "off"}]
		self.procCycle = cycle(self.procList)

		# background thread that runs all the things
		self.backLock = threading.Event()
		self.procFlag = threading.Event()
		self.completed = False
		self.backgroundThread = threading.Thread(target=self.runBackground)
		self.backgroundThread.start()

	def __del__(self):
		"""Stop all threads and destruct the strand/grid."""
		self.backLock.set()
		self.completed = True
		self.backgroundThread.join()
		del self.grid

	def runBackground(self):
		nextParam = None
		while not self.completed:

			# wait until event is set (means params are done changing)
			if not self.backLock.is_set():
				self.backLock.wait()

			# keep history
			lastParam = nextParam
			# get the next procedure to run
			nextParam = next(self.procCycle)

			# special name to turn it all off
			if nextParam["name"].lower() == "off":
				self.grid.setAllColor(colors.Off)
				self.grid.showPixels()
				# short circuit
				continue

			# print("Running procedure: {}".format(nextParam["name"]))

			# no fading on repeats - only supported by twinkle right now
			if (lastParam is not None) and (lastParam["name"] == nextParam["name"]):
				nextParam["fade"] = True

			# start up the procedure
			self.procFlag.clear()
			targetFunction = self.functionMap[nextParam["name"]]
			# function returns a generator
			gen = targetFunction(self.strand, nextParam, self.procFlag)

			# how long to run
			useTime = nextParam["run_time"] is not None
			if useTime:
				endTime = time.time() + nextParam["run_time"]

			while not self.procFlag.is_set():
				# should we stop?
				if useTime and (time.time() > endTime):
					break
				# do the next operation
				nextIdx, nextColor, nextTime, show = next(gen)

				# decode index command
				if isinstance(nextIdx, str):
					# whole tree
					if nextIdx == "all":
						self.strand.setAllColor(nextColor)
					# random index
					elif nextIdx == "rand":
						nextIdx = self.strand.randIdx()
						self.strand.setPixelColor(nextIdx, nextColor)
					# setting columns
					elif nextIdx.startswith("c"):
						colIdx = int(nextIdx[1:])
						self.grid.setColumn(colIdx, nextColor)
					# setting rows
					elif nextIdx.startswith("r"):
						rowIdx = int(nextIdx[1:])
						self.grid.setRow(rowIdx, nextColor)
					else:
						print("Error, invalid encoding '{}'".format(nextIdx))
				else:
					# plain old number
					self.strand.setPixelColor(nextIdx, nextColor)

				# maybe flush the colors
				if show:
					self.strand.showPixels()
				# maybe sleep
				if nextTime > 0:
					time.sleep(nextTime)

			# if break from time,
			self.procFlag.set()

	def runProcedure(self, params):
		"""Params is a list of dictionaries with all of the required keys.

		All keys have been previously validated when read in.
		This will iterate through each item in the list indefinitely, doing one at a time.
		"""

		# event acts as semaphore
		self.backLock.clear()
		self.procList = params
		self.procCycle = cycle(params)
		self.backLock.set()
		# pre-empt the procedure
		self.procFlag.set()


# home page
@app.route('/')
def index():
	now = datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
		'time' : timeString
	}
	return render_template('index.html', **templateData)

# https://stackoverflow.com/a/20648053/12940429
@app.route('/scripts/<path:filename>')
def send_js(filename):
    return send_from_directory('scripts', filename)

# fun
@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)

# responds to HTTP requests that have JSON data
@app.route('/run', methods=['GET', 'POST'])
def runProcedure():
	try:
		if request.method == 'POST':
			# https://stackoverflow.com/a/23898949
			data = str(request.get_data(), encoding='utf-8')
			# format as json
			info = input_parser.sanitizePacket(data)

			# check for errors
			if isinstance(info, str):
				print(data)
				print(info)
				return info
			elif isinstance(info, list):
				ts.runProcedure(info)
				print(info)
				return "accepted"
			else:
				print(data)
				return "Error, invalid request"
	except Exception:
		pass
	finally:
		return "Failure!"


# names of options for getting
get_options = [
	"colors",
	"procedures",
	"presets",
]

@app.route('/get/<req>')
def getData(req):
	if req == "options":
		return json.dumps(get_options)
	elif req == get_options[0]:
		return json.dumps(colors.colorNameMap)
	elif req == get_options[1]:
		procList = list(ts.functionMap.keys())
		return json.dumps(procList)
	elif req == get_options[2]:
		presets = []
		presets.extend(twinkler.presets)
		presets.extend(strobe.presets)
		presets.extend(stripes.presets)
		return json.dumps(presets)
	else:
		return "Invalid request!"


if __name__ == '__main__':
	try:
		ts = TreeServer()
		app.run(debug=False, host='0.0.0.0')
	except KeyboardInterrupt as ki:
		# try to clean up nicely
		del ts
		print("Exiting...")

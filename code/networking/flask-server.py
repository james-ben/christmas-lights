import os
import sys
import json
import time
import threading
from itertools import cycle
from datetime import datetime
from flask import Flask, request, render_template

sys.path.append(os.path.abspath("../"))
from procedures import twinkler, stripes, strobe, columns
from networking import json_api
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
		self.processHandle = None
		self.grid = grid.Grid()
		# alias
		self.strand = self.grid

		# interrupt flags
		self.stopFlag = False
		self.timerInterrupt = False
		self.timerHandle = None

		# procedure objects
		self.twinkler = twinkler.TwinkleLights()
		self.striper = stripes.StripeLights()
		self.strobe = strobe.StrobeLights()
		self.column = columns.ColumnLights()

		self.functionMap = {
			"twinkle": self.twinkler.run,
			"stripes": self.striper.run,
			"strobe": self.strobe.run,
			"columns": self.column.run,
		}

		# init the state
		self.procList = [{"name" : "off"}]
		self.procCycle = cycle(self.procList)

		# background thread that runs all the things
		self.backLock = False
		self.completed = False
		self.backgroundThread = threading.Thread(target=self.runBackground)
		self.backgroundThread.start()

	def __del__(self):
		"""Stop all threads and destruct the strand/grid."""
		self.backLock = True
		self.completed = True
		self.backgroundThread.join()
		del self.grid

	def runBackground(self):
		while not self.completed:

			# spin lock to avoid race conditions
			while self.backLock:
				pass

			# get the next procedure to run
			nextParam = next(self.procCycle)

			# wait for old job to finish
			if self.timerHandle is not None:
				self.timerInterrupt = True
				# this could take a while TODO: make better
				self.timerHandle.join()
				self.timerHandle = None
			if self.processHandle is not None:
				self.stopFlag = True
				self.processHandle.join()
				self.processHandle = None

			# special name to turn it all off
			if nextParam["name"].lower() == "off":
				self.grid.setAllColor(colors.Off)
				# short circuit
				continue

			# print("Running procedure: {}".format(nextParam["name"]))

			# start up the procedure
			targetFunction = self.functionMap[nextParam["name"]]
			self.processHandle = threading.Thread(target=targetFunction, args=(
				self.strand, nextParam, lambda: self.stopFlag))

			# timer to finish if needed
			if "run_time" in nextParam:
				self.timerHandle = threading.Thread(target=self.timerCallback,
				                                    args=(nextParam["run_time"],))

			# start all the things
			if self.processHandle:
				self.stopFlag = False
				self.processHandle.start()

			if self.timerHandle:
				self.timerInterrupt = False
				self.timerHandle.start()

			if self.processHandle:
				# this will enforce waiting correctly
				self.processHandle.join()

	def runProcedure(self, params):
		"""Params is a list of dictionaries with all of the required keys.

		All keys have been previously validated when read in.
		This will iterate through each item in the list indefinitely, doing one at a time.
		"""

		self.backLock = True
		self.procList = params
		self.procCycle = cycle(params)
		self.backLock = False

	def timerCallback(self, timeout):
		# print("Timer sleeping for {} seconds".format(timeout))
		time.sleep(timeout)
		self.stopFlag = True


# home page
@app.route('/')
def index():
	now = datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
		'time' : timeString
	}
	return render_template('index.html', **templateData)

# fun
@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)

# responds to HTTP requests that have JSON data
# TODO: implement GET for getting lists of valid options
@app.route('/run', methods=['GET', 'POST'])
def runProcedure():
	try:
		if request.method == 'POST':
			# https://stackoverflow.com/a/23898949
			data = str(request.get_data(), encoding='utf-8')
			# format as json
			info = json_api.sanitizePacket(data)

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

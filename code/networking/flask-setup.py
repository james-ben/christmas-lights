import os
import sys
import time
import threading
from datetime import datetime
from flask import Flask, request, render_template

sys.path.append(os.path.abspath("../"))
from light_utils import grid
# from light_utils import fake_grid as grid
from procedures import twinkler, stripes, strobe
from networking import json_api


# perhaps this will be changed in the future
app = Flask(__name__)
ts = None


class TreeServer(object):
	def __init__(self):
		self.processHandle = None
		self.grid = grid.Grid()
		# alias
		self.strand = self.grid

		self.twGroup = 5
		self.stopFlag = False
		self.timerInterrupt = False
		self.timerHandle = None

		self.twinkler = twinkler.TwinkleLights()
		self.striper = stripes.StripeLights()
		self.strobe = strobe.StrobeLights()

		self.functionMap = {
			"twinkle": self.twinkler.run,
			"stripes": self.striper.run,
			"strobe": self.strobe.run,
		}

	def runProcedure(self, params):
		"""Params is a dictionary with all of the required keys.  All keys have been previously validated."""

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

		targetFunction = self.functionMap[params["name"]]
		self.processHandle = threading.Thread(target=targetFunction, args=(
											  self.strand, params, lambda: self.stopFlag))

		# timer to finish if needed
		if "run_time" in params:
			self.timerHandle = threading.Thread(target=self.timerCallback,
			                                    args=(params["run_time"],))

		if self.processHandle:
			self.stopFlag = False
			self.processHandle.start()

		if self.timerHandle:
			self.timerInterrupt = False
			self.timerHandle.start()

	def timerCallback(self, timeout):
		time.sleep(timeout)
		self.timerInterrupt = True


@app.route('/')
def index():
	now = datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
		'time' : timeString
	}
	return render_template('index.html', **templateData)

@app.route('/twinkle')
def twinkle():
	return "Twinkly star!"

@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)

@app.route('/run', methods=['GET', 'POST'])
def runProcedure():
	try:
		if request.method == 'POST':
			# https://stackoverflow.com/a/23898949
			data = str(request.get_data(), encoding='utf-8')
			print(data)
			# format as json
			info = json_api.sanitizePacket(data)

			# check for errors
			if isinstance(info, str):
				print(info)
				return info
			elif isinstance(info, dict):
				ts.runProcedure(info)
				print(info)
				return "accepted"
			else:
				return "Error, invalid request"
	except Exception:
		pass
	finally:
		return "Failure!"

# @app.route('/run/<major>/<minor>')
# def runProcedure(major, minor):
# 	if ts.runProcedure(major, minor):
# 		templateData = {
# 			'major' : major,
# 			'minor' : minor
# 		}
# 		return render_template('procedure.html', **templateData)


if __name__ == '__main__':
	ts = TreeServer()
	app.run(debug=False, host='0.0.0.0')

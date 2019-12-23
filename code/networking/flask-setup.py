import os
import sys
import threading
from datetime import datetime
from flask import Flask, render_template

sys.path.append(os.path.abspath("../"))
from light_utils import grid
from procedures import twinkler, stripes, strobe


majorChoices = [
	"twinkle",
	"stripes",
	"strobe"
]

minorChoices = {
	"twinkle" : [
		"color",
		"white"
	],
	"stripes" : [
		"up_ordered",
		"upDown_ordered",
	],
	"strobe" : [
		"upDown_ordered"
	]
}


# perhaps this will be changed in the future
app = Flask(__name__)
ts = None

class TreeServer():
	def __init__(self):
		self.processHandle = None
		self.grid = grid.Grid()
		# alias
		self.strand = self.grid

		self.twGroup = 5
		self.stopFlag = False

	def validateProcedure(self, major, minor):
		# validate major
		if major in majorChoices:
			if minor in minorChoices[major]:
				return True
		return False

	# TODO: add way to pass optional params
	def runProcedure(self, major, minor):
		valid = self.validateProcedure(major, minor)
		if valid:
			# cancel old thread
			if self.processHandle is not None:
				self.stopFlag = True
				self.processHandle.join()

			# new thread, target is the major/minor
			if major == majorChoices[0]:
				# twinkle
				if minor == minorChoices[major][0]:
					# color
					self.processHandle = threading.Thread(target=twinkler.colorLoop, args=(
							self.strand, self.twGroup, lambda: self.stopFlag))
				if minor == minorChoices[major][1]:
					# white
					self.processHandle = threading.Thread(target=twinkler.whiteLoop, args=(
							self.strand, self.twGroup, lambda: self.stopFlag))

			elif major == majorChoices[1]:
				# stripes
				if minor == minorChoices[major][0]:
					# up_ordered
					self.processHandle = threading.Thread(target=stripes.upLoopOrdered, args=(
							self.strand, lambda: self.stopFlag))
				elif minor == minorChoices[major][1]:
					# upDown_ordered
					self.processHandle = threading.Thread(target=stripes.upDownLoopOrdered, args=(
						self.strand, lambda: self.stopFlag))

			elif major == majorChoices[2]:
				# strobe
				if minor == minorChoices[major][0]:
					# upDown_ordered
					self.processHandle = threading.Thread(target=strobe.upDownLoopOrdered, args=(
						self.strand, lambda: self.stopFlag))

			# start the new thread
			if self.processHandle:
				self.stopFlag = False
				self.processHandle.start()

		return valid


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

@app.route('/run/<major>/<minor>')
def runProcedure(major, minor):
	if ts.runProcedure(major, minor):
		templateData = {
			'major' : major,
			'minor' : minor
		}
		return render_template('procedure.html', **templateData)


if __name__ == '__main__':
	ts = TreeServer()
	app.run(debug=True, host='0.0.0.0')

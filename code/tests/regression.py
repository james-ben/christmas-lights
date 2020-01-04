import json
import time
from urllib import request

from procedures import (twinkler, strobe,
                        stripes, columns,
                        blink)


pi_url = "http://192.168.0.102:5000/run"
local_url = "http://192.168.0.111:5000/run"

def createRequest(url, data):
	req = request.Request(url)
	req.add_header('Content-Type', 'application/json; charset=utf-8')
	jsondata = json.dumps(data)

	jsondatabytes = jsondata.encode('utf-8')
	req.add_header('Content-Length', len(jsondatabytes))
	return req, jsondatabytes

def sendRequest(req, data):
	return request.urlopen(req, data)

def makePiRequest(data):
	req, jsonData = createRequest(pi_url, data)
	resp = sendRequest(req, jsonData)
	return resp

def makeLocalRequest(data):
	req, jsonData = createRequest(local_url, data)
	resp = sendRequest(req, jsonData)
	return resp


def twinkleTest():
	print("\n --- Twinkle test --- ")
	aggregateRequest = []
	sleepTime = 0

	# default
	twinkleData0 = dict(twinkler.presets[0]["data"])
	aggregateRequest.append(twinkleData0)
	sleepTime += twinkleData0["run_time"]

	# white twinkle
	twinkleData1 = dict(twinkler.presets[1]["data"])
	twinkleData1["color_set"] = ["white"]
	aggregateRequest.append(twinkleData1)
	sleepTime += twinkleData1["run_time"]

	# off and on, just red
	twinkleData2 = dict(twinkleData0)
	twinkleData2["color_set"] = ["red", "off"]
	twinkleData2["brightness"] = "0.4"
	aggregateRequest.append(twinkleData2)
	sleepTime += twinkleData2["run_time"]

	# twinkle two colors
	twinkleData3 = dict(twinkleData0)
	twinkleData3["color_set"] = ["red", "green"]
	aggregateRequest.append(twinkleData3)
	sleepTime += twinkleData3["run_time"]

	makePiRequest(aggregateRequest)
	# makeLocalRequest(aggregateRequest)

	time.sleep(sleepTime)


def stripeTest():
	print("\n --- Stripe test --- ")
	aggregateRequest = []
	sleepTime = 0

	# default stripe pattern
	stripeData0 = dict(stripes.presets[0]["data"])
	aggregateRequest.append(stripeData0)
	sleepTime += stripeData0["run_time"]

	# random all
	stripeData1 = dict(stripes.presets[1]["data"])
	aggregateRequest.append(stripeData1)
	sleepTime += stripeData1["run_time"]

	# down
	stripeData2 = dict(stripeData0)
	stripeData2["color_set"] = ["green", "red"]
	stripeData2["direction"] = "backward"
	aggregateRequest.append(stripeData2)
	sleepTime += stripeData2["run_time"]

	# blink time range
	stripeData3 = dict(stripeData0)
	stripeData3["blink_time"] = [0.001, 0.05]
	aggregateRequest.append(stripeData3)
	sleepTime += stripeData3["run_time"]

	# bounce
	stripeData4 = dict(stripes.presets[2]["data"])
	aggregateRequest.append(stripeData4)
	sleepTime += stripeData4["run_time"]

	# TODO: num runs, see if exits

	makePiRequest(aggregateRequest)

	# wait for the things to run
	time.sleep(sleepTime)


def strobeTest():
	print("\n --- Strobe Test --- ")
	aggregateRequest = []
	sleepTime = 0

	# default strobe
	strobeData0 = dict(strobe.presets[0]["data"])
	aggregateRequest.append(strobeData0)
	sleepTime += strobeData0["run_time"]

	# strobe down, single color
	strobeData1 = dict(strobeData0)
	strobeData1["direction"] = "backward"
	strobeData1["color_set"] = "blue"
	aggregateRequest.append(strobeData1)
	sleepTime += strobeData1["run_time"]

	# random strobe time
	strobeData2 = dict(strobeData0)
	strobeData2["blink_time"] = [0.1, 0.6]
	strobeData2["direction"] = "bounce"
	strobeData2["color_set"] = "blue"
	aggregateRequest.append(strobeData2)
	sleepTime += strobeData2["run_time"]

	# strobe up
	strobeData3 = dict(strobeData0)
	strobeData3["direction"] = "forward"
	aggregateRequest.append(strobeData3)
	sleepTime += strobeData3["run_time"]

	makePiRequest(aggregateRequest)

	# wait for the things to run
	time.sleep(sleepTime)


def columnTest():
	print("\n --- Column Test --- ")
	aggregateRequest = []
	sleepTime = 0

	# default
	colData0 = dict(columns.presets[0]["data"])
	aggregateRequest.append(colData0)
	sleepTime += colData0["run_time"]

	colData1 = dict(columns.presets[1]["data"])
	aggregateRequest.append(colData1)
	sleepTime += colData1["run_time"]

	makePiRequest(aggregateRequest)
	time.sleep(sleepTime)


def blinkTest():
	print("\n --- Blink Test --- ")
	aggregateRequest = []
	sleepTime = 0

	for p in blink.presets:
		aggregateRequest.append(p["data"])
		sleepTime += p["data"]["run_time"]

	makePiRequest(aggregateRequest)
	time.sleep(sleepTime)


def main():
	# test a variety of things
	twinkleTest()
	stripeTest()
	strobeTest()
	columnTest()
	blinkTest()


if __name__ == '__main__':
	main()

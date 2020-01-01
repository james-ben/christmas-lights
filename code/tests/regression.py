import json
import time
from urllib import request


pi_url = "http://192.168.0.102:5000/run"
local_url = "http://192.168.0.114:5000/run"

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
	twinkleData0 = {
		"color_set": ["red", "green", "yellow", "white"],
		"color_ordered": False,
		"brightness": ["0", ".5"],
		"run_time": 30,
	    "blink_time": ["0", ".5"],
		"name": "twinkle",
		# "num_runs": "5"
	}
	aggregateRequest.append(twinkleData0)
	sleepTime += twinkleData0["run_time"]

	# white twinkle
	twinkleData1 = dict(twinkleData0)
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
	stripeData0 = {
		"color_set": ["green", "yellow", "red", "white"],
		"color_ordered": True,
		"brightness": "0.5",
	    "run_time": 5,
		"blink_time": "0.001",
		"name": "stripes",
		"direction": "forward",
	    # "num_runs": "5"
	}
	aggregateRequest.append(stripeData0)
	sleepTime += stripeData0["run_time"]

	# random all
	stripeData1 = dict(stripeData0)
	stripeData1["color_ordered"] = False
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
	stripeData4 = dict(stripeData0)
	stripeData4["direction"] = "bounce"
	stripeData4["blink_time"] = 0.001
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

	strobeData0 = {
		"name": "strobe",
		"color_set": ["green", "red", "white"],
		"color_ordered": True,
		"brightness": ["0.5", "0.5"],
	    "run_time": 10,
		"blink_time": ["0.2", "0.2"],
		"direction": "bounce",
		# "num_runs": "5"
	}
	# default strobe
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


def main():
	# test a variety of things
	twinkleTest()
	stripeTest()
	strobeTest()


if __name__ == '__main__':
	main()
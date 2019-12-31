import json
import time
from urllib import request


pi_url = "http://192.168.0.102:5000/run"

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


def twinkleTest():
	print("\n --- Twinkle test --- ")

	# default
	twinkleData = {
		"color_set": ["red", "green", "yellow", "white"],
		"color_ordered": False,
		"brightness": ["0", ".5"],
		"run_time": "2",
	    "blink_time": ["0", ".5"],
		"name": "twinkle",
		# "num_runs": "5"
	}
	print("Default twinkle")
	resp = makePiRequest(twinkleData)
	time.sleep(10)

	# white twinkle
	print("White twinkle")
	twinkleData["color_set"] = ["white"]
	resp = makePiRequest(twinkleData)
	time.sleep(10)

	# off and on, just red
	print("Red pulse")
	twinkleData["color_set"] = ["red", "off"]
	twinkleData["brightness"] = "0.4"
	resp = makePiRequest(twinkleData)
	time.sleep(10)

	# twinkle two colors
	print("Red green twinkle")
	twinkleData["color_set"] = ["red", "green"]
	twinkleData["brightness"] = ["0", ".5"]
	resp = makePiRequest(twinkleData)
	time.sleep(10)

	# TODO: twinkle num runs, see if exits


def stripeTest():
	print("\n --- Stripe test --- ")

	# default stripe pattern
	stripeData = {
		"color_set": ["green", "yellow", "red", "white"],
		"color_ordered": True,
		"brightness": "0.5",
	    "run_time": "5",
		"blink_time": "0.001",
		"name": "stripes",
		"direction": "forward",
	    # "num_runs": "5"
	}
	print("Default stripe")
	resp = makePiRequest(stripeData)
	time.sleep(8)

	# random all
	print("Random stripes")
	stripeData["color_ordered"] = False
	resp = makePiRequest(stripeData)
	time.sleep(10)

	# down
	print("Down stripes")
	stripeData["color_ordered"] = True
	stripeData["color_set"] = ["green", "red"]
	stripeData["direction"] = "backward"
	resp = makePiRequest(stripeData)
	time.sleep(5)

	# blink time range
	print("Testing variable blink time")
	stripeData["blink_time"] = [0.001, 0.05]
	resp = makePiRequest(stripeData)
	time.sleep(10)

	# bounce
	print("Bounce stripes")
	stripeData["direction"] = "bounce"
	stripeData["blink_time"] = 0.001
	resp = makePiRequest(stripeData)
	time.sleep(5)


def strobeTest():
	strobeData = {
		"name": "strobe",
		"color_set": ["green", "red", "white"],
		"color_ordered": True,
		"brightness": ["0.5", "0.5"],
	    "run_time": "10",
		"blink_time": ["0.2", "0.2"],
		"direction": "bounce",
		# "num_runs": "5"
	}

	# default strobe
	print("Default stripe")
	resp = makePiRequest(strobeData)
	time.sleep(8)

	# strobe down
	print("strobe down, single color")
	strobeData["direction"] = "backward"
	strobeData["color_set"] = "blue"
	resp = makePiRequest(strobeData)
	time.sleep(5)

	# random strobe time
	print("random strobe time")
	strobeData["blink_time"] = [0.1, 0.6]
	strobeData["direction"] = "bounce"
	strobeData["color_set"] = "blue"
	resp = makePiRequest(strobeData)
	time.sleep(10)

	# strobe up
	print("strobe up")
	strobeData["color_set"] = ["green", "red", "white"]
	strobeData["blink_time"] = 0.2
	strobeData["direction"] = "forward"
	resp = makePiRequest(strobeData)
	time.sleep(5)


def main():
	# test a variety of things
	# twinkleTest()
	# stripeTest()
	strobeTest()


if __name__ == '__main__':
	main()

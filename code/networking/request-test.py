from urllib import request
import json

twinkle0 = {"color_set":["red", "green"],"color_ordered":False,"brightness":["0.2",".5"],"run_time":"10","blink_time":["0.1",".5"],"name":"twinkle","direction":"forward","num_runs":"5"}
stripe0 = {"color_set":["green","yellow","red","white"],"color_ordered":True,"brightness":["0.5","0.5"],"run_time":"6","blink_time":["0.02","0.02"],"name":"stripes","direction":"forward","num_runs":"5"}
strobe0 = {"color_set":["green","red","white"],"color_ordered":True,"brightness":["0.5","0.5"],"run_time":"2","blink_time":["0.5","0.5"],"name":"strobe","direction":"bounce","num_runs":"5"}
cols0 = {"color_set":["green","red"],"color_ordered":True,"brightness":["0.5","0.5"],"run_time":"5","blink_time":["0.2","0.2"],"name":"columns","direction":"forward"}
crazy0 = {"color_set":["red","white","blue"],"color_ordered":False,"brightness":["0.3","0.6"],"run_time":"5","blink_time":["0.1","0.1"],"name":"crazy","direction":"forward"}
turnOff = {"name":"off"}

myurl = "http://192.168.0.102:5000/run"
# myurl = "http://192.168.0.114:5000/run"
req = request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(twinkle0)
# jsondata = json.dumps(turnOff)
# jsondata = json.dumps(strobe0)
# jsondata = json.dumps(cols0)
# jsondata = json.dumps(stripe0)

jsondatabytes = jsondata.encode('utf-8')
req.add_header('Content-Length', len(jsondatabytes))
response = request.urlopen(req, jsondatabytes)

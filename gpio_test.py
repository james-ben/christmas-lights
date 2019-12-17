import pigpio
import time
import sys

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)

try:
	#for _ in range(5):
	while True:
		pi.write(18, 1)
		time.sleep(1)
		pi.write(18, 0)
		time.sleep(1)
except KeyboardInterrupt as e:
	sys.exit(0)

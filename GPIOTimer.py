'''Basic Daily Timer Class 
Turns a GPIO pin on and off throughout the day.
LBC, 2020-01'''

import threading
from datetime import datetime as dt
import board
import digitalio as dio

class GPIOTimer:
	
	def __init__(self, GPIOPin, timesToggle, initialState = False, timeCheck = 5):
		"""To use GPIOTimer, CircuitPython must be installed. 
		GPIOPin is the board pin. 
		timesToggle is a dict of ~the times using datetime.time()~:~True~ or ~False~
		initialState is the state when initializing. 
		timeCheck is the period of time in seconds that the program checks the time."""
		#TODO: Check if time is synced correctly
		
		self.timesToggle = timesToggle
		self.timesKeys = sorted(timesToggle.keys())
		self.tL = len(self.timesKeys)
		#Initialize Pin
		self.state = initialState
		self.DIOPin = dio.DigitalInOut(GPIOPin)
		self.DIOPin.direction = dio.Direction.OUTPUT
		self.DIOPin.value = self.state
		#Schedule Next Loop
		self.nextTime = threading.Timer(1, self.operate)
		self.nextTime.start()
	
	def operate(self):
		
		now = dt.now().time()
		for i, k in enumerate(self.timesKeys):
			next_k = self.timesKeys[(i+1)%self.tL]
			if next_k < k:
					#Passing midnight in this condition. 
					if now > k or now < next_k:
						#Between the two times. Perform action.
						currentState = self.timesToggle[k]
						self.DIOPin.value = currentState
						print("Within " + "{:%H:%M:%S}".format(k) + " and " + "{:%H:%M:%S}".format(next_k) + " (Next day). ",
						" Toggling to " + repr(currentState) + ".")
			elif now > k and now < next_k:
					#Between the two times. Perform action.
					currentState = self.timesToggle[k]
					self.DIOPin.value = currentState
					print("Within " + "{:%H:%M:%S}".format(k) + " and " + "{:%H:%M:%S}".format(next_k) + ". ",
						" Toggling to " + repr(currentState) + ".")
				
					
		
		#Schedule Next Loop, in 5 seconds
		self.nextTime = threading.Timer(5, self.operate)
		self.nextTime.start()
	

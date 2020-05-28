'''Start a Timer'''


import board
import digitalio as dio
from GPIOTimer import *
from datetime import time

#PINS
#3  (BCM#2 : board.D2)  This Pin  
#5  (BCM#3 : board.D3)  Or This Pin

GPIOPin = board.D20		#CHANGE TO YOUR DESIRED PIN

#format: time(hr, min, sec, microsec)

toggleTimes = { time( 3,20, 0,0):True,
				time( 3,47, 0,0):False,
				time( 4, 5, 0,0):True,
				time( 4,11, 0,0):False
				}
				
GPIOTimer(GPIOPin, toggleTimes)

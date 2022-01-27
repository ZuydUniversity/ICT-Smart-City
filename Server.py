"""

"""

import sys
import os
import array
from grove_rgb_lcd import *
import grovepi

buzzer = 8
#Set pinmode.
grovepi.pinMode(buzzer,"OUTPUT")

sys.path.append(
	os.path.join(
		os.path.dirname(__file__),
		'..'
	)
)
	
import lib as pyrfm

conf={
	'll':{
		'type':'rfm95'
	},
	'pl':{
		'type':	'serial_seed',
		'port':	'/dev/ttyS0'
	}
}
ll=pyrfm.getLL(conf)

print('HW-Version: ', ll.getVersion())
if ll.setOpModeSleep(True,True):
	ll.setFiFo()
	ll.setOpModeIdle()
	ll.setModemConfig('Bw125Cr45Sf128');
	ll.setPreambleLength(8)
	ll.setFrequency(868)
	ll.setTxPower(13)
	
	#If the server recieves the data from the node, send a confirmation message.
	#If the distance is less than 6, set the lcd screen to red and activate the buzzer.
	while True:
		if ll.waitRX(timeout=3):
			data=ll.recv()
			header=data[0:4]
			msg=data[4:]
			ll.sendStr('Got your message!')
			message = int(array.array('B', msg).tostring())
			setText(str(message))
			if message < 6:
				setRGB(255,0,0)
				grovepi.digitalWrite(buzzer,1)
			else:
				setRGB(0,255,0)
				grovepi.digitalWrite(buzzer,0)

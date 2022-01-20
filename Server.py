"""

"""

import sys
import os
import array
from grove_rgb_lcd import *

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
		'port':	'/dev/ttyUSB0'
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
	
	while True:
		#ll.sendStr('Hello world!')
		#ll.waitPacketSent()
		
		if ll.waitRX(timeout=3):
			data=ll.recv()
			header=data[0:4]
			msg=data[4:]
			#print('header: ',header)
			#print('message:',array.array('B', msg).tostring())
			ll.sendStr('Got your message!')
            setText(array.array('B', msg).tostring())
			setRGB(0,255,0)
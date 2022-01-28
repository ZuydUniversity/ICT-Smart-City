import sys
import os
import time
import array
import grovepi 


ultrasonic = 4 #number of the port where the ultrasonic sensor is connected to.	

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
	
	#Send data from the Ultrasonice Distance sensor to the server and receive a message when the data has been succesfully received.
	while True:
		ll.sendStr(str(grovepi.ultrasonicRead(ultrasonic))) 
		ll.waitPacketSent()
		
		if ll.waitRX(timeout=3):
			data=ll.recv()
			header=data[0:4]
			msg=data[4:]
			print('header: ',header)
			print('message:',array.array('B', msg).tostring())

		time.sleep(1)
			
			
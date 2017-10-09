import winsound
import time

def beep():
	for i in [1,2,3]:
		winsound.Beep(3500,500)
		time.sleep(0.1)
		
beep()
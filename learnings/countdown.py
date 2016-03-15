#! python3
# countdown.py - A simple countdown script.

import time, subprocess
timeLeft = 5
while timeLeft > 0:
	print(timeLeft,'\n')
	time.sleep(1)
	timeLeft = timeLeft - 1

subprocess.Popen(['start', 'Alarm01.wav'], shell=True)
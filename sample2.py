import subprocess,time
proc=subprocess.Popen(['python','sample1.py'],shell=False,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
for i in range(5):
	proc.stdin.write('%d\n'%i)
	output = process.stdout.readline()
	print output
	time.sleep(1)

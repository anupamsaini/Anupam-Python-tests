#!/usr/bin/env python
import subprocess
import getpass

def main(brightness, password):
	proc = subprocess.Popen(
		['sudo', '-p', '', '-S', '/usr/bin/setpci', '-s', '00:02.0', brightness],
		 stdin=subprocess.PIPE)
	proc.stdin.write(password+'\n')
	proc.stdin.close()
	proc.wait()

if __name__ == "__main__":
	print "\n Enter brightness value between 44 to 99 "
	brightness = "F4.B=" + str(raw_input('brightness: '))
	password = getpass.getpass()
	main(brightness, password)

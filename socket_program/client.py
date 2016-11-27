import socket
#host = "www.google.com"
#port = 80
host = socket.gethostname()
port = 8889
s = socket.socket()
try:
	s.connect((host,port))
	ack = s.recv(1024)
	print ack
	data = raw_input("Enter number:")
	s.send(data)
	#s.send('12')
	resp = s.recv(1024)
	print resp
except Exception as err:
	print err
finally:
	s.close()


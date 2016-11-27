import socket
import db
host = socket.gethostname()
port = 8889

s = socket.socket()
try:
	s.bind((host,port))
	s.listen(6)
	print "waiting for the connection"
	#print s.accept()	
	client_obj,client_info = s.accept()
	client_obj.send("Connected sucessfully!!")
	clinet_data = client_obj.recv(1024)
	client_data = int(clinet_data)
	'''
	res = 'odd'
	if client_data%2 == 0:
		res = "even"
	'''
	res =db.browse(client_data)
	res = str(res)
	client_obj.send(res)
except Exception as err:
	print err
finally:
	s.close()

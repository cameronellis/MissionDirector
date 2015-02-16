import socket, threading
from Networking import ports


def send_msg(msg):
	#thread = threading.Thread(target=private___dispatch_msg, args=(msg))
	#thread.daemon = True
	#thread.start()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("localhost",ports.outport_MAVProxy))
	s.send(msg)
	s.close()



#---------------------------------------------------------------------

def private___dispatch_msg(msg):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("localhost",ports.outport_MAVProxy))
	s.send(msg)
	s.close()

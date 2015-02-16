#-----------------------------------------------------------------
# Listens for messages from a human operator (i.e. manual inputs/overrides)
#

import MissionDirector
from Clients import MAVProxyC


#-----------------------------------------------------------------------------
# Callback to process an incoming message or command from the human operator
#
def callback(data):
	print "received message from human operator: \"" + str(data) + "\""
	datastr = str(data)
	
	#--------------------------------------------------------------------------
	# If message starts with "mavproxy:", forward to MAVProxy
	#
	if len(datastr) > 10 and datastr[:9] == "mavproxy:":
		MAVProxyC.send_to_mdlink.send_msg(datastr[9:])
		print "sent message to MAVProxy mdlink"
	
	#--------------------------------------------------------------------------
	# Todo: other types of messages/commands that a human operator might want to send
	
	



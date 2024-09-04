import socket
import sys
import struct

# ARGS

ARG1 = sys.argv[1] # File to send, -> txt or binary

#User supplied file to import
with open(sys.argv[1], 'rb') as f:
    data_to_send = f.read()

#Syslog host and port to connect
HOST = '192.168.86.45'
PORT = 514

#Setting up the connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Connecting to " + HOST + " on port " + str(PORT))
s.connect((HOST, PORT))

#Send data from read the file
print("Sending data " + str(f.name))
s.send(struct.pack('>L', len(data_to_send)))
s.send(data_to_send)
#s.close()
print("Finished sending " + f.name)

#Set up main to call functions from above
#main () {
#}

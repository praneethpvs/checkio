import socket  # Import socket module
import sys

s = socket.socket()  # Create a socket object
host = str(sys.argv[2])  # Get local machine name
port = int(sys.argv[1])  # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', data)
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
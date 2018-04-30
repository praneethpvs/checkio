import socket  # Import socket module
import sys
import os
from traceback import print_exc

"""
The below line of code runs a system command which sets the bandwidth for particular network interface.
For executing below statement "tcconfig" package is required.
Link: http://tcconfig.readthedocs.io/en/latest/pages/introduction/index.html
It can be used to set the properties of the traffic control over network
The below command sets the bandwidth of the particular network device or server to 10 Mbps.
"""
os.system('tcset --device lo0 --rate 10M')


def get_size(f_name):
    """
    Function which returns the size of the file that is specified in the Argument.
    The current code takes the file specified from the location of the server.py file.
    :param f_name:
    :return:
    """
    st = os.stat(f_name)
    return int(st.st_size)


# Creating a TCP/IP Socket for establishing connection to the client.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Reserving a port for using the service.
port = int(sys.argv[1])
# Get local machine name
host = '127.0.0.1'
server_address = (host, port)
print('starting up on %s port %s' % server_address)
s.bind(server_address)  # Bind to the port
s.listen(5)  # Now wait for client connection.

print('Server listening....')

while True:
    print('waiting for a connection...')
    connection, client_address = s.accept()  # Establish connection with client.
    try:
        print('Got connection from', client_address)
        data = connection.recv(1024)
        print('Server received', repr(data))

        filename = sys.argv[2]
        print("Size of the file specified: {} Bytes".format(get_size(filename)))
        connection.send(filename)
        connection.send(str(get_size(filename)))
        print("Sending the file %s the the client %s" % (filename, client_address))
        packet_sent = 0
        if get_size(filename) < 10485760:
            try:
                f = open(filename, 'rb')
                file_data = f.read(1024)
                while file_data:
                    connection.send(file_data)
                    # print('Sent Data %s' % repr(file_data))
                    # received_data = s.recv(1024)
                    # print('Received data from client: %s' % received_data)
                    # while True:
                    #     print("Checking if the data sent is received correctly by the client side.")
                    #     if received_data == file_data:
                    #         break
                    #     else:
                    #         connection.send(file_data)
                    file_data = f.read(1024)
                    packet_sent += 1
            except Exception as e:
                print(e)
                print_exc()
            else:
                # connection.send(str(packet_sent))
                print("Number of packets sent: {}".format(packet_sent))
                f.close()
                print('Done sending')
                # connection.send('Thank you for connecting')
            finally:
                connection.close()
        else:
            print("Specified file size should be less than 10 Mb. Please choose a file again")
    except Exception as e:
        print(e)
        print_exc()
    # finally:
    #     connection.close()

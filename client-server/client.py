import socket  # Import socket module
import sys
import time

from traceback import print_exc

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a TCP/IP Socket.
host = str(sys.argv[1])  # Get local machine name
port = int(sys.argv[2])  # Reserve a port for your service.

client_addr = (host, port)
print('starting up on %s port %s' % client_addr)
s.connect(client_addr)
s.send("Hello server!")

file_name = s.recv(1024)
file_size = int(s.recv(1024))
print("File that is being sent from the server: %s" % file_name)
print("Size of the file that is being sent from the server: {} Bytes".format(file_size))
try:
    f = open(file_name, 'wb')
    print('receiving data...')
    total_size = 0
    prev_data = None
    start_data_transfer = time.time()
    packet_received = 0
    while True:
        current_data = s.recv(1024)
        if not current_data:
            break
        else:
            # print('Received Data: %s' % repr(current_data))
            total_size += 1024
            percentage_file = 100 if (total_size / float(file_size)) * 100 > 100 else (total_size / float(
                file_size)) * 100
            print("Percentage of the File received............... {}".format(percentage_file))
            packet_received += 1

        if current_data != prev_data:
            # write data to a file if the received packet is not duplicate.
            f.write(current_data)
        else:
            print("Duplicate packet has been received. Ignoring the packet...!!")
        prev_data = current_data
    end_data_transfer = time.time()
except Exception as e:
    print(e)
    print_exc()
else:
    f.close()
    print("Number of packets received: {}".format(packet_received))
    time_data_transfer = (end_data_transfer - start_data_transfer) * 1000
    print("Time taken to complete the data transfer: %s ms" % time_data_transfer)
    # through_put = round(1024 * packet_received * 0.001) / time_data_transfer
    # print("Throughput: {} K/sec".format(through_put))
    print('Throughput: {} K/sec'.format(
        round(1024 * packet_received * 0.001) / (end_data_transfer - start_data_transfer)))
    print('Successfully got the file sent from the server')
    # s.shutdown(socket.SHUT_RD)
finally:
    s.close()
    print('connection closed by the client')

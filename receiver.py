import socket
from check_sum import check_sum, check_sum_from_hex
from utility import *

DATA = 0x0
ACK = 0x1
FIN = 0x2
FIN_ACK = 0x3

# Create UDP socket
receiversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ask port to be binded
#port = int(input("Port number: "))

# bind to address and IP
receiversocket.bind(('localhost', 2000))

# Listen for incoming datagrams
print("Receiver is listneing on", receiversocket.getsockname())

while True:
    #accept connections from outside
    data, address = receiversocket.recvfrom(33000)

    # Show connection received information
    print(f"Connection from {address} has been established!")

    if data:
        TYPE_RECEIVED, ID_RECEIVED, SEQ_RECEIVED, LENGTH, CHECK_SUM, READ_DATA = extract_packet(data)
        ##### Check checksum ######
        data = data.decode()
        checksum_calculate = check_sum(data[:5] + data[7:])
        checksum_received = check_sum_from_hex(data[5:7])
        if checksum_calculate == checksum_received:
            if (TYPE_RECEIVED == DATA):
                TYPE_RECEIVED = ACK
            elif (TYPE_RECEIVED == FIN):
                TYPE_RECEIVED = FIN_ACK

            PACKET_BACK = build_packet(TYPE_RECEIVED, ID_RECEIVED, SEQ_RECEIVED, '')
            receiversocket.sendto(PACKET_BACK, address)
            print(f"Sending ACK Packet ID {ID_RECEIVED} SEQ {SEQ_RECEIVED}")

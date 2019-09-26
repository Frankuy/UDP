import socket
from check_sum import check_sum, check_sum_from_hex

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
type = 0

while True:
    #accept connections from outside
    data, address = receiversocket.recvfrom(32775)

    # Show connection received information
    print(f"Connection from {address} has been established!")

    if data:
        ##### Check checksum ######
        data = data.decode()
        checksum_calculate = check_sum(data[:5] + data[7:])
        checksum_received = check_sum_from_hex(data[5:7])


        # print(checksum_calculate)
        # print(data.decode()[0])
        # checksum_received = ord(data[5:7].encode())
        if checksum_calculate == checksum_received:
            type = (ord(data[0]) >> 4) + 1
            id = ord(data[0]) << 4 >> 4
            PACKET_BACK = chr(type) + chr(id)
            PACKET_BACK += data[1:7]

            receiversocket.sendto(PACKET_BACK.encode(), address)

    # message = bytesAddressPair[0]
    # address = bytesAddressPair[1]

    # clientMsg = "Message from Client:{}".format(message)
    # clientIP  = "Client IP Address:{}".format(address)

    # print(clientMsg)
    # print(clientIP)
    # # Sending a reply to client
    # serversocket.sendto(bytesToSend, address)

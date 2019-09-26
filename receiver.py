import socket
import binascii
def bytes_to_str(byt):
    return byt.decode("utf-8")


def strhex_to_int(str):
    return int(str, 2)


def extract(packet):
    packet = bytes_to_str(packet)

    type = packet[0:1]
    type = strhex_to_int(type)

    id = packet[1:2]
    id = strhex_to_int(id)

    seq_num = packet[2:6]
    print(seq_num)
    seq_num = strhex_to_int(seq_num)

    len = packet[6:10]
    len = strhex_to_int(len)


    checksum = packet[10:14]

    data = packet[14:]



    return (type, id, seq_num, len, checksum, data)



# Create UDP socket
receiversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ask port to be binded
port = int(input("Port number: "))

# bind to address and IP
receiversocket.bind(('localhost', port))

# Listen for incoming datagrams
print("Receiver is listneing on", receiversocket.getsockname())
while True:
    #accept connections from outside
    data, address = receiversocket.recvfrom(4096)

    # Show connection received information
    print(f"Connection from {address} has been established!")

    if data:
        sent = receiversocket.sendto(data, address)
        print('sent : {} ... {} bytes back to {}'.format(data, sent, address))
    # message = bytesAddressPair[0]
    # address = bytesAddressPair[1]

    # clientMsg = "Message from Client:{}".format(message)
    # clientIP  = "Client IP Address:{}".format(address)

    # print(clientMsg)
    # print(clientIP)
    # # Sending a reply to client
    # serversocket.sendto(bytesToSend, address)

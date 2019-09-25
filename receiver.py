import socket

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
import socket

MAX_FILES = 5

# Create UDP socket 
sendersocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ask receiver IP Address
receiver_ip = input('Receiver IP: ')

# Ask receiver Port Address
receiver_port = int(input('Receiver Port: '))

# Combine IP and Port to make Receiver Address
receiver_address = (receiver_ip, receiver_port)

# Connect to receiver
sendersocket.connect(receiver_address)

# Get Filenames that want to be sended
valid_files = False
while not valid_files:
    filenames = input('Send File : ')
    if filenames == '':
        print('Please input at least one file')
    else:
        filenames = filenames.split(' ')
        if (len(filenames) > MAX_FILES):
            print('Cannot send more than 5 files')
        else:
            valid_files = True

for filename in filenames:
    sendersocket.sendto(bytes(filename, "utf-8"), receiver_address)

while True:
    # Receive response
    print('Waiting to receive')
    data, receiver = sendersocket.recvfrom(4096)

    print('received {!r}'.format(data))
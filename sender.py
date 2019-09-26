from check_sum import check_sum
import socket

#################
# CONSTANT
#################
N_FILES = 1
N_PACKETS = 10
MAX_FILES = 5
LAST_DATA = 12
READ_DATA = ''

#################
# TYPE
#################
DATA = 0x0
ACK = 0x1
FIN = 0x2
FIN_ACK = 0x3
CHUNK_SIZE = 32768

# Create UDP socket
sendersocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ask receiver IP Address
#receiver_ip = input('Receiver IP: ')

# Ask receiver Port Address
#receiver_port = int(input('Receiver Port: '))

# Combine IP and Port to make Receiver Address
receiver_address = ('localhost', 2000)

# Connect to receiver
sendersocket.connect(receiver_address)

# Get Filenames that want to be sended
valid_files = False
while not valid_files:
    #filenames = input('Send File : ')
    filenames = 'test2.txt'
    if filenames == '':
        print('Please input at least one file')
    else:
        filenames = filenames.split(' ')
        if (len(filenames) > MAX_FILES):
            print('Cannot send more than 5 files')
        else:
            valid_files = True

#### LOOP PER FILES ####
ID = 0x0
packets = []
for filename in filenames:
    file = open(filename, 'rb')
    text = file.read(CHUNK_SIZE)
    chunks = []
    while text:
        chunks.append(text)
        text = file.read(CHUNK_SIZE)
    file.close()

    SEQ_NUM = 0x0
    TYPE = DATA
    N_PACKETS = len(chunks)

    #### LOOP PER PACKETS ####
    for i in range(0, N_PACKETS):
        ### Last Packets ###
        if (i == N_PACKETS-1):
            TYPE = FIN

        ##### Concat TYPE with ID #####
        PACKET = chr((TYPE << 4) + ID)

        ##### Concat with SEQUENCE #####
        PACKET += chr(0) + chr(SEQ_NUM)

        ##### Concat with Length #####
        PACKET += chr(0) + chr(len(chunks[i]))

        ##### Concat with Checksum #####
        for char in chunks[i]:
            READ_DATA += chr(char)
        PACKET += chr(0) + chr(check_sum(PACKET + READ_DATA))

        ##### Concat with Data #####
        PACKET += READ_DATA

        sendersocket.sendto(PACKET.encode(), receiver_address)
        print("Paket ke-",i+1," telah berhasil dikirim")
        SEQ_NUM += 1
    ID += 1

while True:
    data, address = sendersocket.recvfrom(32775)

    if data:
        print('Received ACK : ', data)

######################
# Write read file
######################
# file = open('coba.bin', 'wb')
# for packet in packets:
#     file.write(bytearray(packet[7:].encode()))
# file.close()

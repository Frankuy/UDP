import socket

MAX_FILES = 5
#type
DATA = 0x0
ACK = 0x1
FIN = 0x2
FIN_ACK = 0x3

def hex2bin(hex):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    return bin(int(hex, scale))[2:].zfill(num_of_bits)

print(hex2bin("x01"))

def string2bits(test_str):

    result = ''.join(format(i, 'b') for i in bytearray(test_str, encoding ='utf-8'))
    return result

def hex_to_str(hex, padding):
    return bin(hex)[2:].zfill(padding)

def str_to_bytes(s, n_bytes):
    return int(s, 2).to_bytes(n_bytes, 'big')

def binStrToInt(binary_str):

    length = len(binary_str)

    num = 0
    for i in range(length):
        num = num + int(binary_str[i])
        num = num * 2
    return num // 2

def int_to_bytes(x, n) -> bytes:
    return x.to_bytes(n, byteorder='big')

def makePacket(type, id, seq_numb, data ) : #in hhex
'''    type = type << 4
    packet = type + id

    print(packet)
    len = 7
    print(data)
    if(data != None):
        print(len(data))
        len = len+ len(data)

    len = int_to_bytes(len,2)
    print(len)
    #seq number
    seq_numb = hex_to_str(seq_numb,4)
    print(seq_numb)



#test = makePacket(0x1, 0x1, 0x1, 0x1011)

'''
    #type =
    len = length(data) + 7
    sum = check_sum(type, id,seq_numb, data)
    packet = type + id + seq_numb + data

    return packet #in binary

def check_sum(type, id, seq, l, data):

    arr = type+id+seq+l+data
    div = len(arr)//16

    checksum = arr[:16]
    temp = ""
    for i in range(1, div):
        arr_div = arr[16*i: 16*(i+1)]
        for j in range(16):
            xor = int(checksum[j]) ^ int(arr_div[j])
            temp = str(xor) + temp
        checksum = temp

    #print(checksum)
    sisa = len(arr)%16

    if(sisa!=0):
        sisa_arr = arr[16*div:]
        for i in range(len(arr)-sisa):
            sisa_arr = "0"+ sisa_arr

        temp =""
        for j in range(16):
            temp = str (int(checksum[j]) ^ int(sisa_arr[j])) + temp

        checksum = temp

#    result = binStrToInt(checksum)
#    print(result)
#    result = int_to_bytes(result,2)

    return result

test = check_sum("0001", "0001", "0000000000000001", "0000000000000011", "0000000000000001")
print(test)


'''
a = ACK << 4
print(a)
'''

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

import socket

MAX_FILES = 5
#type
DATA = 0x0
ACK = 0x1
FIN = 0x2
FIN_ACK = 0x3

def hex2bin(hex):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4
    return bin(int(hex, scale))[2:].zfill(num_of_bits)
def bin2hex(bin):
    return hex(int(bin,2))
def makebinary(str):
    temp =""
    for i in str:
        temp = temp + hex2bin(i)
    return temp

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

def int_to_hexstr(bil):
    return hex(bil)

def str_to_bytes(hex):
    return bytes(hex, 'utf-8')

def int_to_bytes(bil):
    return bytes([bil])


def read_file(filename): #nama.txt >> bytes
    with open(filename, "rb") as file:
        data = file.read()
    return data

def bytes_to_str(byt):
    return byt.decode("utf-8")



def makePacket(type, id, seq_numb, data ) : # (hex, hex, hex, bytes) >> bytes
#    id = int_to_hex(id)

#    seq_numb = int_to_hex(seq_numb)

    type = type << 4
    first_line = int_to_hexstr(type+id) #string hex
#    print(first_line)
    first_line = first_line[2:]

#    print(seq_numb)
    second_line = hex_to_str(seq_numb, 4)

#    print(second_line)

    l = 7
    l = len(bytes_to_str(data)) + l
    l = hex_to_str(l,4)
    #print(l)


    data = bytes_to_str(data)
#    print(makebinary(data))
#    print(makebinary(first_line))
    packet_temp = first_line+second_line+l+data
    packet_temp = makebinary(packet_temp)
#    print(packet_temp)

    div = len(packet_temp)//16

    checksum = packet_temp[:16]
#    print(checksum)

    for i in range(1, div):
        temp = ""
        arr_div = packet_temp[16*i: 16*(i+1)]
#        print(arr_div)
        for j in range(16):
            xor = int(checksum[j]) ^ int(arr_div[j])
#            print(int(checksum[j]), end = ' ')
#            print(int(arr_div[j]), end = ' ')
#            print()
            temp =  temp + str(xor)
        checksum = temp
#        print(checksum)

    sisa = len(packet_temp)%16
    if(sisa!=0):
        sisa_arr = packet_temp[16*div:]
        for i in range(16-sisa):
            sisa_arr = "0"+ sisa_arr

        temp2 =""
        for k in range(16):
            temp2 = temp2 + str (int(checksum[k]) ^ int(sisa_arr[k]))

        checksum = temp2
    #    print(checksum)

#    print(checksum)
    checksum = bin2hex(checksum)
#    print(checksum)
    checksum = checksum[2:]

#    print(first_line)
#    print(second_line)
#    print(l)
#    print(checksum)
#    print(data)

#    packet = first_line + second_line+ l + checksum + data
#    print(packet)
#    return str_to_bytes(packet)



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

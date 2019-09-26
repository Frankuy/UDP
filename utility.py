def hex_to_str(hexa, padding):
    return bin(hexa)[2:].zfill(padding)

def str_to_bytes(s, n_bytes):
    return int(s, 2).to_bytes(n_bytes, 'big')

# Testing
# Want 16 bits form from 0xFF 
# print(hex_to_str(0xFF, 16))

# Want to convert binary string to bytes
# print(str_to_bytes('111111111111111111111111', 12))
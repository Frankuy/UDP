def hex_to_str(hex, padding):
    return bin(hex)[2:].zfill(padding)

# Testing
# Want 16 bits form from 0xFF 
# print(hex_to_str(0xFF, 16))
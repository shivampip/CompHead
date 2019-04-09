import os
import struct

def write_bytes(data, name):
    #f= open('{}.bnr'.format(name), 'wb')
    #f.write(data)
    #print("Successfully written")
    #data= '101010101111111'
    print(data)
    int_value = int(data[::-1], base=2)
    print(int_value)
    bin_array = struct.pack('i', int_value)
    print(bin_array)
    with open("test.bnr", "wb") as f:
        f.write(bin_array)
        print("File written successfully")
import os
import struct
import math
from bitstring import BitArray

def bitstring_to_bytes(data):
    n= math.ceil(len(data)/8)
    return int(data, 2).to_bytes(n, byteorder='big')

def write_bytes(data, name):
    data= '1'+data 
    bydata= bitstring_to_bytes(data)
    with open('files/{}'.format(name), 'wb') as f:
        f.write(bydata)
        print("Successfully written")


def read_file(name):
    with open('files/{}'.format(name), 'r') as f:
        return f.read() 

def read_binary(name):
    with open('files/{}'.format(name), mode='rb') as file: 
        content= file.read()
        c= BitArray(content)
        return c.bin.lstrip('0')[1:]

def read_bytes(name):
    with open('files/{}'.format(name), mode='rb') as file: 
        content= file.read()
        c= BitArray(content)
        return c.bytes
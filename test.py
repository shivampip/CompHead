import ioman
from bitstring import BitArray

data= '0010111110010101010001101010'
#data= '1'+data 

print("Bytes: \t{}".format(ioman.bitstring_to_bytes('1'+data)))

ioman.write_bytes(data, 'ddd')
dbytes= ioman.read_bytes('ddd.bnr')
dbits= ioman.read_binary('ddd.bnr')

print("Bytes:\t{}".format(dbytes))

print("Data: \t{}".format(data))

#dbits= dbits.lstrip('0')[1:]
print('Bits:\t{}'.format(dbits))
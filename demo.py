from variable_length_code import VLC
import comp_test 
import ioman


def encode_huffman(text= None, filename=None, outfile='files/out.bnr'):
    model= VLC()
    if(text is None):
        text= ioman.read_file(filename)
    huff_enc= model.encode_huff(text)
    enc_tree= model.encode_tree()
    SPACE= '{:08b}'.format(32) *10 # SPACE ASCII 32
    enc_data = huff_enc+ SPACE+ enc_tree
    ioman.write_bytes(enc_data, outfile)
    return outfile

def decode_huffman(filename):
    model= VLC()
    read_out= ioman.read_binary(filename)
    SPACE= '{:08b}'.format(32) *10 # SPACE ASCII 32
    huff_data, huff_tree = read_out.split(SPACE)
    dec_tree= model.decode_tree(huff_tree)
    dec_data= model.decode_huff(dec_tree, huff_data)
    return dec_data


text= "Shivam Agrawal"
fname= 'shiv.bnr'
#encode_huffman(text, outfile=fname)
encode_huffman(filename='demo.txt', outfile= fname)
dtext= decode_huffman(fname)
print('DECODED: {}'.format(dtext))

'''
model= VLC()

# Direct Text
#text= 'aaabbbbbccccccddddee'
#text= 'My name is shivam agrawal. I live at pipariya. currently I am working at L & T Infotech, Mumbai, India'

# Read from file
text= ioman.read_file('demo.txt')

#Encoded Huffman data
huff_enc= model.encode_huff(text)

# Encoded Huffman Tree
enc_tree= model.encode_tree()

# Combining with delimiter
SPACE= '{:08b}'.format(32)  # SPACE ASCII 32
SPACE= SPACE*10
enc_data = huff_enc+ SPACE+ enc_tree

# Writing Bytes
ioman.write_bytes(enc_data, 'demo.bnr')

#################READING#################################

# Reading Binary
read_out= ioman.read_binary('demo.bnr')

# Splitting Table and Data
huff_data, huff_tree = read_out.split(SPACE)

# Decoded Huffman Tree
dec_tree= model.decode_tree(huff_tree)

# Decoded Huffman data
dec_data= model.decode_huff(dec_tree, huff_data)

# Testing
comp_test.test(text, huff_enc, dec_data, enc_tree)
'''


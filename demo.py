from variable_length_code import VLC

def fix_encoding(data):
    out= ''.join(format(ord(x), 'b') for x in data)
    return out 


model= VLC()

text= 'aaabbbbbccccccddddee'
#text= 'My name is shivam agrawal. I live at pipariya. currently I am working at L & T Infotech, Mumbai, India'

b_out= fix_encoding(text)
h_out= model.encodeHuff(text)

h_decoded= model.decodeHuff(h_out)

print("Binary: \t{}".format(len(fix_encoding(text))))
print("Huffman: \t{}".format(len(h_out)))
print("Score: \t\t{0:.2f}".format(len(h_out)*100.0/len(b_out)))

print("Encoded: \t{}".format(h_out))
print("Decded: \t{}".format(h_decoded))
print("Lossless: \t{}".format(text== h_decoded))
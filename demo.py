from variable_length_code import VLC
import comp_test 

print(format(ord('e'), 'b')) 
print(chr(int('1100101', 2)))

model= VLC()

text= 'aaabbbbbccccccddddee'
#text= 'My name is shivam agrawal. I live at pipariya. currently I am working at L & T Infotech, Mumbai, India'



h_eout= model.encode_huff(text)

en_tree= model.encode_tree()
dc_tree= model.decode_tree(en_tree)
h_dout= model.decode_huff(dc_tree, h_eout)

'''
en_tree= model.encode_tree()
print("Encoded Tree:\n{}".format(en_tree))

dc_tree= model.decode_tree(en_tree)

from tree import Node
nnn= Node()
nnn.print(dc_tree)
'''

comp_test.test(text, h_eout, h_dout)
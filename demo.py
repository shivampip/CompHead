from variable_length_code import VLC
import comp_test 
print(format(ord('a'),'b'))
model= VLC()

text= 'aaabbbbbccccccddddee'
#text= 'My name is shivam agrawal. I live at pipariya. currently I am working at L & T Infotech, Mumbai, India'



h_eout= model.encode_huff(text)
h_dout= model.decode_huff(h_eout)

treed= model.encode_tree()
print(treed)
model.decode_tree(treed)

comp_test.test(text, h_eout, h_dout)
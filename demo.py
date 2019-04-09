from variable_length_code import VLC
import comp_test 
import ioman

model= VLC()

#text= 'aaabbbbbccccccddddee'
#text= 'My name is shivam agrawal. I live at pipariya. currently I am working at L & T Infotech, Mumbai, India'
text= '''
Silicon Valley is an American comedy television series created by Mike Judge, John Altschuler and Dave Krinsky. The series focuses on five young men who founded a startup company in Silicon Valley.[1][2] The series premiered on April 6, 2014 on HBO,[3] and the fifth season premiered on March 25, 2018.[4] HBO renewed the series for a sixth season in April 2018.[5] In November 2018, it was announced that the sixth season would be delayed, with production beginning in summer 2019, with a projected premiere date of 2020.[6]
'''


#Encoded Huffman data
h_eout= model.encode_huff(text)

# Encoded Huffman Tree
en_tree= model.encode_tree()

final_en_out= h_eout+""+ en_tree

ioman.write_bytes(final_en_out, 'cdata')

# Decoded Huffman Tree
dc_tree= model.decode_tree(en_tree)

# Decoded Huffman data
h_dout= model.decode_huff(dc_tree, h_eout)



# Testing
comp_test.test(text, h_eout, h_dout, en_tree)
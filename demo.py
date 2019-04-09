from variable_length_code import VLC
import comp_test 
import ioman



out_file= 'hi2mb.bnr'

text= None
#text= "Shivam Agrawal"

in_file= None
in_file= 'its2mb.txt'


model= VLC()
_,_,_,enc_data = model.encode_huffman(text=text, filename= in_file, outfile=out_file)
dec_data = model.decode_huffman(out_file)
comp_test.test(text=text, in_file= in_file, enc_data= enc_data, dec_data= dec_data, out_file=out_file)




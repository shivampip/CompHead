from tree import Node 
from operator import attrgetter
import ioman


class VLC:

    def __init__(self):
        self.DELIMITER= '{:08b}'.format(ord('␜'))*2  # ␜ is file saperator

    def get_min_node(self, lst):
        node= min(lst, key=lambda inst: inst.value)
        lst.remove(node)
        return node, lst

    def make_huff_tree(self, data):
        moc= [(data.count(chr),chr) for chr in set(data)]
        #moc.sort(reverse= False)
        #print("Frequence tabel is {}".format(moc))
        
        dd= [Node(name= m[1], value= m[0]) for m in moc]
        
        while(len(dd)>=2):
            a, dd= self.get_min_node(dd)
            b, dd= self.get_min_node(dd)
            ab= Node(value= a.value+ b.value)
            #print('A is {} B is {} AB is {}'.format(a.value, b.value, ab.value))
            ab.left= a
            ab.right= b
            dd.append(ab)

        d= dd[0]
        #d.print(d)
        self.root= d 
        tab= d.traverse(d)
        #print('Table is {}'.format(tab))
        return tab 

    def encode_huff(self, data):
        self.tab= self.make_huff_tree(data)
        out= ""
        for dd in data:
            out+= self.tab[dd]
        return out

    def decode_huff(self, root, data):
        self.root= root 
        out= ""
        for bit in data:
            root= root.left if bit == '0' else root.right
            if(root.name!=None):
                out+= root.name 
                root= self.root 
        return out 

    def encode_tree(self, root= None, out= ""):
        if(root is None):
            root= self.root
        if(root.name is not None):
            out+= '1'
            #out+= format(ord(root.name), 'b') 
            out+= ''.join('{:08b}'.format(b) for b in root.name.encode('utf8'))
            return out 
        else:
            out+= '0'
            out= self.encode_tree(root.left, out)
            out= self.encode_tree(root.right, out)
            return out 


    def find_child(self, data):
        bit= data[0]
        del data[0]
        if(bit=='0'):
            node= Node()
            node.left= self.find_child(data)
            node.right= self.find_child(data)
            return node
        else:
            #pattern= "".join(data[:7])
            pattern= "".join(data[:8])
            ch= chr(int(pattern, 2))
            #del data[:7]
            del data[:8]
            node= Node(name=ch, value= ch) 
            return node 

    def decode_tree(self, data):
        data= list(data)
        return self.find_child(data)


    ################################################################

    def preprocess(self, data):
        # Original bitstring -> processed bits
        return data 

    def postprocess(self, data):
        # Processed bits -> Original bitstring
        return data 

    ################################################################


    def encode_huffman(self, text= None, filename=None, outfile='files/out.bnr'):
        if(text is None):
            text= ioman.read_file(filename)
        # Encode Huffman data    
        huff_enc= self.encode_huff(text)
        # Encode Huffman tree
        enc_tree= self.encode_tree()
        # Combining data and tree with delimiter
        enc_data = huff_enc+ self.DELIMITER + enc_tree
        enc_data= self.preprocess(enc_data)
        # Writing Bytes
        ioman.write_bytes(enc_data, outfile)
        return outfile, huff_enc, enc_tree, enc_data

    def decode_huffman(self, filename):
        # Reading binary
        read_out= ioman.read_binary(filename)
        read_out= self.postprocess(read_out)
        # Splitting Huffman data and tree/table
        huff_data, huff_tree = read_out.split(self.DELIMITER)
        # Decoding Huffmna tree
        dec_tree= self.decode_tree(huff_tree)
        # Decoding Huffman data with table/tree
        dec_data= self.decode_huff(dec_tree, huff_data)
        return dec_data








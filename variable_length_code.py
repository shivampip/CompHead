from tree import Node 
from operator import attrgetter


class VLC:

    def get_min_node(self, lst):
        node= min(lst, key=lambda inst: inst.value)
        lst.remove(node)
        return node, lst

    def make_huff_tree(self, data):
        moc= [(data.count(chr),chr) for chr in set(data)]
        #moc.sort(reverse= False)
        print("Frequence tabel is {}".format(moc))
        
        dd= [Node(name= m[1], value= m[0]) for m in moc]
        
        while(len(dd)>=2):
            a, dd= self.get_min_node(dd)
            b, dd= self.get_min_node(dd)
            ab= Node(value= a.value+ b.value)
            print('A is {} B is {} AB is {}'.format(a.value, b.value, ab.value))
            ab.left= a
            ab.right= b
            dd.append(ab)

        d= dd[0]
        d.print(d)
        self.root= d 
        tab= d.traverse(d)
        print('Table is {}'.format(tab))
        return tab 

    def encode_huff(self, data):
        self.tab= self.make_huff_tree(data)
        out= ""
        for dd in data:
            out+= self.tab[dd]
        return out

    def decode_huff(self, root, data):
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
            out+= format(ord(root.name), 'b') 
            out+= ""
            return out 
        else:
            out+= '0'
            out= self.encode_tree(root.left, out)
            out= self.encode_tree(root.right, out)
            return out 


    def find_child(self, data, pb= 0):
        bit= data[0]
        del data[0]
        if(bit=='0'):
            node= Node()
    
            left= self.find_child(data, pb= 0)
            right= self.find_child(data, pb= 1)
    
            node.left= left
            node.right= right
            return node
        else:
            pattern= "".join(data[:7])
            ch= chr(int(pattern, 2))
            del data[:7]
            node= Node(name=ch, value= ch) 
            return node 




    def decode_tree(self, data):
        data= list(data)
        return self.find_child(data)








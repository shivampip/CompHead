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
        print(moc)
        
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
        print('Table is {}'.format(tab))
        return tab 

    def encode_huff(self, data):
        self.tab= self.make_huff_tree(data)
        out= ""
        for dd in data:
            out+= self.tab[dd]
        return out

    def decode_huff(self, data):
        root= self.root 
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
            return out 
        else:
            out+= '0'
            out= self.encode_tree(root.left, out)
            out= self.encode_tree(root.right, out)
            return out 

    def decode_tree(self, data):
        b= data[0]
        if(b=='1'):
            value= data[1: 9]
            print("Leaf Next value is {} chr is {}".format(value, chr(int(value, 2))))
            #print(chr(int(value, 2)))
            data= data[9:]
            return Node(value= value)
        if(b=='0'):
            print("No Leaf")
            data= data[1:]
            left= self.decode_tree(data)
            if(left.left is None):
                data= data[8:]
            data= data[1:]
            right= self.decode_tree(data)
            if(right.right is None):
                data= data[8:]
            node= Node()
            node.left= left
            node.right= right
            return node 








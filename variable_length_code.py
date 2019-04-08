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

    def encodeHuff(self, data):
        self.tab= self.make_huff_tree(data)
        out= ""
        for dd in data:
            out+= self.tab[dd]
        return out

    def decodeHuff(self, data):
        root= self.root 
        out= ""
        for bit in data:
            root= root.left if bit == '0' else root.right
            if(root.name!=None):
                out+= root.name 
                root= self.root 
        return out 




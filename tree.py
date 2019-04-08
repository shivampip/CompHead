import time
class Node:
    def __init__(self, name= None , parent= None, value= None):
        self.name= name
        self.value= value
        self.left= None
        self.right= None 
        self.parent= parent 

    def __lt__(self, other):
        return self.value < other.value

    def print(self, root):
        if(root is not None):
            left, right= root.left, root.right
            if(left is None):
                print("Parent: {}".format(root.value))
            else:
                print("Parent: {} Left: {} Right: {}".format(root.value, root.left.value, root.right.value))
            self.print(root.left)
            self.print(root.right)
    
    def traverse(self, root, str="", tab= {}):
        if(root.name is not None):
            #print(" {} = {}".format(root.name, str))
            tab[root.name]= str 
            return tab 
        else:
            tab= self.traverse(root.left, str+"0", tab)
            tab= self.traverse(root.right, str+"1", tab)
            return tab 


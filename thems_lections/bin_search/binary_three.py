class ThreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
class BinThree:
    def __init__(self, root):
        self.root = root
        
    def add_node(self,value):
        
        cur_node = self.root
        while True:
                if value == cur_node.value:
                    return
                
                if cur_node.value < value:
                    if cur_node.right is None:
                        cur_node.right = ThreeNode(value)
                        cur_node = cur_node.right
                        break
                    else:
                        cur_node = cur_node.right
                else:
                    if cur_node.left is None:
                        cur_node.left = ThreeNode(value)
                        break
                    else:
                        cur_node = cur_node.left
        return cur_node
    
    def find_node(self, value):
        flag = None
        curr_node = self.root
        while flag is None:
            if value == curr_node.value:
                flag = True
                
            elif value < curr_node.value:
                if curr_node.left is not None:
                    curr_node = curr_node.left
                else:
                    flag = False
                
            else: # value > curr_node.value
                if curr_node.right is not None:
                    curr_node = curr_node.right
                else:
                    flag = False
        return flag
                    
            
    def find_minimum(self):
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.value
    
    def find_maximum(self):
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.value
    
    def get_bin_three(self, value):
        return [[self.get_bin_three(value.left),value.value, self.get_bin_three(value.right)] if value is not None else None]
             
    
    
root = ThreeNode(10)

bin_three = BinThree(root)
bin_three.add_node(2)
bin_three.add_node(11)
bin_three.add_node(12)
bin_three.add_node(115)
bin_three.add_node(100)

print(bin_three.get_bin_three(bin_three.root))

print(bin_three.find_node(114))

print(bin_three.find_minimum())
print(bin_three.find_maximum())


        
        
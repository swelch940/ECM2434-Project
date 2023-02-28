import barkbuddy,pickle

class BarkBuddyPickler:
    def __init__(self, id):
        self.id = id #ID of the tree owner
    
    def save(self, tree_object:barkbuddy): #CURRENTLY UNSAFE
        with open(self.id + "bin","wb") as f:
            #any additional hashing goes here. there needs to be *some* eventually
            pickle.dump(tree_object)
        
    def load(self): #CURRENTLY VERY UNSAFE
        with open(self.id+".bin","rb") as f:
            spam = pickle.load(f)
        #unhashing goes here !!!!!
        return spam
    
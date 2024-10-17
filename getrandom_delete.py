import random 

class RandomizedSet(object):
    random_set = []
    def __init__(self):
        ...
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.random_set: 
            return False
        else: 
            self.random_set.append(val)
            return True 
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.random_set: 
            self.random_set.remove(val)
            return True
        else: 
            return False 
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.random_set) 
        

import math 
x = math.acos(2/3)

y = x * 180 / math.pi 
z= 90 - y 

print(y, z)
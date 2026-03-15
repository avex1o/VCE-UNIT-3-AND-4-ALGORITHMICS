import math as mh
import random as rm

def Combs(set, n): # n = how many items we want to choose
    l = len(set) # l = number of items in set
    combinations = mh.factorial(l) / (mh.factorial(n) * mh.factorial(l-n)) # formula to figure out number of combinations of a set (order not important so [2,1] is same combination as [1,2])
    print(f"Number of combinations for this set when picking {n} items is: {combinations}.") 

def Perms(set, n):
    l = len(set)
    permutations = mh.factorial(l) / (mh.factorial(l-n)) # formula to figure out number of permutations of a set (order is important)
    print(f"Number of permutations for this set when picking {n} items is: {permutations}.")

nums = {1,2,3,4,5}

Combs(nums, 3)
Perms(nums, 3)


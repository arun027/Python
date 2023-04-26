from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def minPenalty(arr):
    
    # Write your code here.
    arr.sort()
    
    # Initialize the penalty to 0
    penalty = 0
    
    # While there are more than 1 elements in the array
    while len(arr) > 1:
        # Pick the two smallest elements in the array
        a = arr.pop(0)
        b = arr.pop(0)
        
        # Calculate the sum of the two elements
        sum_ab = a + b
        
        # Add the penalty to the sum
        penalty += sum_ab
        
        # Add the sum to the array
        arr.append(sum_ab)
        
        # Sort the array in ascending order
        arr.sort()
        
    return penalty
           
        

t = int(stdin.readline().rstrip())

while t > 0:
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(minPenalty(arr))
    t-=1

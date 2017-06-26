'''
Created on Jun 26, 2017

@author: rubynam
'''


def is_prime(x):
    if(x<2): return False    
    if(x==2 or x==3): return True
    if x>3:
        i =2
        while i<x:
            if x%i==0: 
                return False
            i+=1
    return True
def no_prime():
    i=2
    counter =0
    while i<=100:
        if is_prime(i):
            counter +=1
            #print(i)
        i+=1
    return counter

print(no_prime())






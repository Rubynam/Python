'''
Created on Jul 9, 2017

@author: hv
'''

#NewTon SquareRoot
def _sqrt(val):
    
    assert(val>0),'Error'  
    def f(x):
        return x**2-val
    def derf(x):
        return 2*x
    guess=val
    for i in range(1,16): # le 16 so
        guess = guess-f(guess)/derf(guess)
    return guess
    
print(_sqrt(2.5))
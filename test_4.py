'''
Created on Jul 15, 2017

@author: hv
'''


import re
s= 'e this is my book'
v = "aeiou"
lst= ['a','e','i','o','u']
c = "qwrtypsdfghjklzxcvbnm"
check = re.findall(r'[^'+c+'|'+c.upper()+']',s)
print(check)
a=set(lst).difference(set(check))
for i in a:
    print(i)
#vowel_pos = [ i for i,v in enumerate(s) if v.lower() in ('a','e','i','o','u','y') ]

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

str=''.join(check).replace(" ",'')
print(str)
result = re.findall(r'[^'+v+'|'+v.upper()+']', str)
print(result)
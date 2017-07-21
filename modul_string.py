import re

Vowel =['a','e','i','o','u']
c = "qwrtypsdfghjklzxcvbnm"

def check_vowel(str):
	lst = re.findall(r'[^'+c+'|'+c.upper()+']',str)
	result = set(Vowel).difference(set(lst))
	return result

def isVowel(str):
    for i in str:
        if i =='a' or i=='e' or i== 'o' or i=='u' or i=='i':
            return True
    return False




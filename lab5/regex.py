#ex1
import re

txt = "abbbbbb abb abbbb"
pattern = r'a*b'
print(re.search(pattern, txt))

#ex2
import re

txt = "abbb abb abbbb"

pattern = r'ab{2,3}'

print(re.findall(pattern, txt))

#ex3
import re

txt = "abbbbbb abb abbbb"

pattern = r'\w[a-z]+[_].+[a-z]'
# pattern = r'[a-z]+[_]+[a-z].*\s'

print(re.search(pattern, txt))

#ex4
import re

txt = "abbbbbb abb abbbb"

# pattern = r'[A-Z]+[a-z]*'
pattern = r'[A-Z]?[a-z].'

print(re.search(pattern, txt))

#ex5
import re

txt = "abbbbbb abb abbbb"

pattern = r'a.*b'

print(re.search(pattern, txt))

#ex6
import re

txt = "abbbbbb ,ab.b ab..bbb"
txt1 = "abbbbbb, abb ,abbbb"
txt2 = "........ksjsj"

pattern = r'[\s.,]'

# print(re.sub("\s", ":", txt))
# print(re.sub(",", ":", txt1))
# print(re.sub("[.]", ":", txt2))
print(re.sub(pattern, ':', txt))

#ex7
import re

def SnakeToCamelcase(text):
    modified_word=""
    pattern = r'[_]'
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            modified_word += word.capitalize()
        else: 
            modified_word += word
    return modified_word

#ex8
import re

def w_to_upper(text):
    wordd = ""
    pattern = r'[A-Z][a-z]+'
    words = re.findall(pattern,text)
    for i, word in enumerate(words):
        if i != 0:  
            wordd += " " + word
        else:
            wordd += word
    return wordd

#ex9
import re

def spaces(txt):
    result = ""
    pattern = r'[A-Z][a-z]+'
    words = re.findall(pattern,txt)
    for i, word in enumerate(words):
        if i != 0:
            result += " " + word
        else:
            result += word
    return result

#ex10
import re
def cameltosnake(text):
    res = ""
    pattern = r'[A-Z][a-z]+'
    words = re.findall(pattern,text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res
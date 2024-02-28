#ex1
import re

b_str = 'hydfdasd'

x = re.search("ab*", b_str)
if x:
    print("Matched -", x.group())
else:
    print("Didn't match")
#ex2
import re

q_str = 'clfslmfdss'

x = re.search(r"ab{2,3}", q_str)
if x:
    print("Matched -", x.group())
else:
    print("Didn't match")
#ex3
import re
k_str = 'berik_alibek74_add'
x = re.findall("[a-z]+_[a-z]+", k_str)
if x:
    print("Matched, sequences:", x)
else:
    print("Didn't match")
#ex4
import re
z_str = "dsBerik.;sAlibek4df"
x = re.findall("[A-Z][a-z]+", z_str)
if x:
    print("Sequences:", x)
else:
    print("Didn't match")
#ex5
import re
t_str = 'benfkofdsb'
x = re.search("a.*b$", t_str)
if x:
    print("Sequences:", x.group())
else:
    print("Didn't match")
#ex6
import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, ':', text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'[\s,.]'
test(pattern, 'my surname, dfl.,3', 1, 'my:surname::dfl::3')
#ex7
import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, lambda a: a.group('ch').upper(), text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'_(?P<ch>.)'
test(pattern, 'b_int_fdatf f_Ve_Vh_roz', 1, 'bIntFdAtf fVeVhRoz')
#ex8
import re

def test(pattern, text, testnum, result):
    res = re.split(pattern, text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = '[A-Z]'
test(pattern, 'iamAlibekDDsoCmy:G9qwXex', 1, ['i', 'am', 'alibek', '', 'so', 'my:', '5th', 'ex'])
#ex9
import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, r'\1 \2', text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'(?P<low>\w)(?P<upp>[A-Z])'
test(pattern, "MyMegaText", 1, "My Mega Text")
test(pattern, " MyMegaText IAmMachine", 2, " My Mega Text I Am Machine")
#ex10
import re

def test(pattern, func, text, testnum, result):
    res = re.sub(pattern, func, text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'.[A-Z]'
change_to = lambda a: f'{a.group().lower()[0]}_{a.group().lower()[1]}'
test(pattern, change_to, 'Facebook, Android and Ozon ', 1, 'Face_book, A_ndroid and O_zon')
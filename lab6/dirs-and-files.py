#ex.1
import os

print(os.listdir("."))

#ex.2
import os

print(os.access(".", os.F_OK))
print(os.access(".", os.R_OK))
print(os.access(".", os.W_OK))
print(os.access(".", os.X_OK))

#ex.3
import os

if os.path.exists("./"):
    print(os.listdir("./"))

#ex.4
with open('text.txt','r') as f:
    s = len(f.readlines())
    print(f"Num of lines :{s}")
    
#ex.5
numbers = [1, 2, 3, 4, 5, 6]
with open('text3.txt', 'w') as f:
    for i in numbers:
        f.write(f'{i}\n')
f.close()

#ex.6
import os

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in s:
    filename = f"{i.replace(':', '_').replace('/', '_')}.txt"
    f = open(filename, 'x')

#ex.7
import shutil

shutil.copy('text.txt', 'text2.txt')

#ex.8
import os

inp = input()

if os.access(f"./{inp}", os.F_OK):
    if os.path.exists(f'./{inp}'):
        os.remove(f'./{inp}')
        print(os.getcwd())

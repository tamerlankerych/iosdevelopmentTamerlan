#ex.1
l = list(map(int,input().split()))
result = 1
for i in l:
    result = result * i

print(result)

#ex.2
def cnt(inp):
    
    Upper_case = 0
    Lower_case = 0

    for i in inp:
        if i.isupper():
            Upper_case += 1
        elif i.islower():
            Lower_case += 1
    print(inp)
    print(f"The num of uppercase letters : {Upper_case}")
    print(f"The num of lowercase letters : {Lower_case}")


cnt(input())  

#ex.3
def palindrome(inp):
    if inp == inp[::-1]:
        return True
    else:
        return False
print(palindrome(input()))

#ex.4
import time

def squarerootAftertime(n, ms):
    time.sleep(ms/1000)
    print(f"Square root of {n} after {ms} milliseconds is {(n)**0.5}")
    print(time.time())
squarerootAftertime(int(input()), int(input()))

#ex.5
tp = tuple(input().split())
print(all(tp))
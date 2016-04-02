# coding: utf-8    #if we use python 2

d = 7
if 2!=3 \
    and d > 5:
    print()

# READ PEP 8!!!!!!!!!!!!!!

# function id() shaw identity of object, functional value ; copywrite semantica, унікальний ідентифікатор

a = 1
b = 1
a is b  #перевірка по ід, чи займають об*єкти одну комірку в пам*яті
#найчастіше викор для перевірки a is None

import sys

print(sys.getrefcount(1))  #показує скільки посилань на 1

import gc  #зборщик мусора
for i in range(10):
    d = {}
    d[0] = d

gc.collect() #show how much elements we delete from memory
gc.get_threshold()  # show when garbade collector runs


print(type(NotImplemented))     # ???
print(type(...))     # Ellipsis

# NaN   ділення на 0

#memoryview(l)

frozenset([1,2,3,4])

# EAPF !! read about

import builtins
print(dir(builtins))

print( 10/4**3.0)

# raise  remember

import random
i = 0
s = random.randint(1, 10)
while i < 5:
    try:
        ans = int(input('?'))
    except ValueError:
        continue
    if s == ans:
        print('ok')
        break
    elif s < ans:
        print('<')
    else:
        print('>')
        i += 1
else:
    print('You loose')

print(divmod(5,6))      #ціла частина і остача від ділення

#>pydoc -w ./module.py
#wrote module.html
#python



#--------------factorial-------
def text_prompt(msg):
    try:
        return input(msg)
    except NameError:
        return input(msg)

n = int(text_prompt('enter n: '))
if n >= 0:
    i = 0
    res = 1
    for i in range(n):
        i += 1
        res *= i
    print(res)
else:
    print('error! number < 0 do not have fact !')
'''
'''
#------------ triangle ---------
def text_prompt(msg):
    try:
        return input(msg)
    except NameError:
        return input(msg)

a = float(text_prompt('enter a'))
b = float(text_prompt('enter b'))
c = float(text_prompt('enter c'))

if a > 0 and b > 0 and c > 0:
    if a + b <= c :
        print('not triangle')
    elif a + c <= b :
        print('not triangle')
    elif b + c <= a :
        print('not triangle')
    else:
        print('triangle')
else:
    print('not triangle')

'''
'''
#----------------fibonachi--------

L = [0,1]
n = int(input('enter n:'))
for i in range(n):
    k = L[-1] + L[-2]
    L.append(k)
print(L[n])
'''
'''
#----------palindroms--------------
def test_prompt(msg):
    try:
        return input(msg)
    except NameError:
        return input(msg)

a = input('enter a: ')
a = a.lower()
a = a.replace(' ', '')
if a == a[::-1]:
    print('YES')
else:
    print("NO")

#-------------strings-1---------
a = input('enter a: ')
k = a.split(' ')
for i in k:
    l = k[::-1]
a = ' '.join(l)
print(a)

#--------------tickets-----------
a = int(input('enter a: '))
b = int(input('enter b: '))
j = 0

for i in range(a, b + 1):
    x = list(str(i))       # !!!!!!!!
    while len(x) < 6:
        x.insert(0, 0)
    if (int(x[0]) + int(x[1]) + int(x[2])) == (int(x[3]) + int(x[4]) + int(x[5])):
        j += 1
print(j)

#------------decoding------------
a = input(' enter text: ')
a = a.replace(' ', '')
for i in a:
    x = a[0:5] + ' '
    a.replace(a[0:5],'')
    print(x)




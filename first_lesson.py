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
'''
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
'''
#------------decoding------------
KEY = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

a = 'I canT DAnCE i CANt TAlK Hey'
a = a.replace(' ', '')
ab = ''
new = ''
for i in a:
    if i.islower():
        ab += 'a'
    else:
        ab += 'b'

for i in range(0,len(a),5):
    part = ab[i:i+5]
    if len(part) == 5:
        new += alphabet[KEY.find(part)]
print(new)

#------------countiog 0-------------
line = '2345'

def count_h(line):
    line = str(line)
    if line != '' and line[0] == '-':
        line = line[1:]
    if line is '':
        return 'ERROR'
    h = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}

    count = 0

    chars_allowed = h.keys()
    not_zero_char = chars_allowed[:]
    not_zero_char.remove('0')

    num_start = False
    for i in line:
        if not (i in chars_allowed):
            return 'ERROR'
        if i in not_zero_char:
            num_start = True
        if num_start:
            count += int(h[i])
    print(count)
    if not num_start:
        count = 188
    return count

#------------------------------
class Human:
    name = None
    sex = None
    birth_year = None

    def __init__(self, name, year, mother = None, father = None):
        self.name = name
        self.birth_year = year
        self.mother = mother
        self.father = father

    def get_age(self):
        if type(self.birth_year) == int:
            return 2016 - self.birth_year
        return None

    def say_parents(self):
        p1 = ''
        if self.mother:
            p1 = 'mother is ' + self.mother.name
        p2 = ''
        if self.father:
            p2 = 'father is ' + self.father.name
        if p2 and p2:
            return 'My ' + p1 + ' and my ' + p2
        return 'My ' + p1 + p2

    def say(self, msg):
        return self.name + ' says: ' + msg + '.'

sergey = Human('Sergey', 1998)
print(sergey.name)
print(sergey.get_age())

alena = Human('Alena', 1968)
taras = Human('Taras', 1966)
vova = Human('Vova', 1994, alena, taras)
print(vova.say_parents())
print(vova.say(vova.say_parents()))

class Student(Human):
    vuz = None
    marks = []

    def __init__(self, name, year, vuz, marks = [], mother = None, father = None):
        super(Student, self).__init__(name, year, mother, father)
        self.vuz = vuz
        self.marks = marks

    def aver_marks(self):
        if len(self.marks):
            return 1.0 * sum(self.marks) / len(self.marks)
        return 0

    def has_grand(self):
        return True

vlad = Student('Vlad', 1993, 'KPI', [3,4,5,5,5], vova, alena)
print(vlad.vuz)


class Student_KPI(Student):
    def __init__(self, name, year, marks = ''):
        super(Student_KPI, self).__init__(name, year, 'KPI', marks)

    def has_grand(self):
        return self.aver_marks() >= 4

class Student_KNU(Student):
    def __init__(self, name, year, marks = []):
        super(Student_KNU, self).__init__(name, year, 'KNU', marks)

    def has_grand(self):
        return min(self.marks) >= 4


sonya = Student_KNU('Sonya', 1994, [3,4,5,5,5,5,4,3])
print(sonya.has_grand())

nata = Student_KPI('Natalka', 1995, [3,4,5,5,4,5,])
print(nata.has_grand())
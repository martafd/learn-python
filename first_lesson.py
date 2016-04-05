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

import math

class Sphere:
    radius = 1
    x_0 = 0
    y_0 = 0
    z_0 = 0

    def __init__(self,r = 1., x = 0., y = 0., z = 0.):
        self.radius = r
        self.x_0 = x
        self.y_0 = y
        self.z_0 = z

    def get_volume(self):
        return 4.0/3 * math.pi * pow(self.radius, 3)

    def get_square(self):
        return 4 * math.pi * pow(self.radius, 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x_0, self.y_0, self.z_0)

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.x_0 = x
        self.y_0 = y
        self.z_0 = z

    def is_point_inside(self, x, y, z):
        if self.x_0 - x <= self.radius and self.y_0 - y <= self.radius and self.z_0 - z <= self.radius:
            return True
        else:
            return False

s = Sphere(0.5)
print(s.get_center())
print(s.get_volume())
print(s.is_point_inside(0, -1.5, 0))
s.set_radius(1.6)
print(s.is_point_inside(0, -1.5, 0))
print(s.get_radius())


#--------------------class student prometheus --------------
class Student_prom():
    name = ''
    marks = {}
    conf = {}


    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.marks = {}
        self.marks['exam'] = 0
        self.marks['labs'] = []
        for i in range(self.conf['lab_num']):
            self.marks['labs'].append(0)

    def make_lab(self, mark , number = None):
        mark = min(mark, self.conf['lab_max'])    # m cant be more than lab_max
        if number is None:                       # if n is not given; find the first task with no mark, set the mark and reload m
            if 0 in self.marks['labs']:
                self.marks['labs'][self.marks['labs'].index(0)] = mark
        elif number >= 0 and number < len(self.marks['labs']):        #if the task with n exist, reload m
                self.marks['labs'][number] = mark
        return self


    def make_exam(self,mark):
        self.marks['exam'] = min(mark, self.conf['exam_max'])
        return self

    def is_certified(self):
        total_max = self.conf['exam_max'] + self.conf['lab_max'] * self.conf['lab_num']     # possible maximum
        sum = 1.0* self.marks['exam']
        for i in range(len(self.marks['labs'])):
            sum = sum + min(self.conf['lab_max'], self.marks['labs'][i])
        return (sum, sum >= total_max * self.conf['k'])

oleg = Student_prom('Oleg', {'exam_max': 30, 'lab_max': 7, 'lab_num': 10, 'k': 0.61})
oleg.make_lab(1)  # labs: 1 0 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(8,0)  # labs: 7 0 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(1) # labs: 7 1 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(10,7) # labs: 7 1 0 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(4,1) # labs: 7 4 0 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(5)  # labs: 7 4 5 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(6.5)  # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 0
oleg.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.is_certified() )# (59.5, False)
oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.is_certified()) # (62.5, True)


#---------------class SuperStr-------------------------

class SuperStr(str):

    def __init__(self, s):
        self.s = s

    def is_repeatance(self,subs):
        if type(subs) == str and len(subs) != 0:
            multiply = int(len(self.s) / len(subs))
            if self.s == subs * multiply:
                return True
            else:
                return False
        else:
            return False

    def is_palindrom(self):
        if self.s.lower().replace(' ', '') == self.s[::-1].lower().replace(' ', ''):
            return True
        else:
            return False

s = SuperStr('123123123123')
print(s.is_repeatance('123')) # True
print(s.is_repeatance('123123')) # True
print(s.is_repeatance('123123123123')) # True
print(s.is_repeatance('12312')) # False
print(s.is_repeatance(123)) # False
print(s.is_palindrom()) # False
print(s) # 123123123123 (рядок)
print(int(s)) # 123123123123 (ціле число)
print(s + 'qwe') # 123123123123qwe
p = SuperStr('123_321')
print(p.is_palindrom()) # True


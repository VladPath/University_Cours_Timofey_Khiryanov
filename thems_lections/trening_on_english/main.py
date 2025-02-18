# variables are dynamucly typed
"""
a = 0
print(type(a))
a = '1'
print(type(a))

# Multyple assigments 
n,m = 0,'abc'
print(n,m)

# increment
n= n+1
n+=1
print(n)


n = 1
if n > 2:
----n -= 1
elif n == 2:
----n *= 2
else:
----n+=2
    
"""
"""
logical response
parentheses needed for 
multy-line conditions.

and == &&
or == ||

n,m = 1,2
if (n>2 and 
    n != m or n == m):
    n += 1

While loops are similar
a  = 0 
while a < 5:
    print(a)
    a += 1
for i in range(5, 1,-1):
    print(i)

Division is decimal vy default

print(5/2)

Double slash rounds down

print(5//2)
print(-3//2) = 2
print(int(-3 // 2)) = 1

Modding is similar to most languages

ten devided on three will give remain 1
print(10%3) = 1

"""
import math 
"""
print(-10%3)
print(math.fmod(-10,3))

modding = % 
modding is given remein for devide 

print(-10%3) = 2
print(math.fmod(-10,3)) =-1
round down
a = math.floor(10/3) = 3
round up
a = math.ceil(10/3) = 4
a = math.pow(10,9) power of 1 000 000 000
a = math.sqrt(1499) 
print(a*a)

infinity digits always will be bigger or less then ever digit

a = float('-inf')
a = float('inf') infinity
b = math.pow(2,100) very big digit
print(a)
print(b<a) True


Arrays (list in Python)
value inside bracets
you can pop,append or insert for exp
arr = [1,2,3]
arr.pop()
arr.append(3)

arr.insert(2,7)
print(arr)

arr[0] = 100
arr[3] = 0
print(arr)


initialize arr of size n with default value of 1

n = 3
arr = [1] * n

print(arr)

initialize with range
arr = [i for i in range(1,5)]

print(arr[0:4])

Loop through arrays
arr = [i for i in range(1,5)]

# index
for i in range(len(arr)):
    print(arr[i])
# value
for value in arr:
    print(value)

# index and value
for i, value in enumerate(arr):
    print(i, value)

Loop through multiple arrays simultaneously
with unpaking
    
nums1 = [i for i in range(1,11)]
nums2 = [i for i in range(11,21)]
for i,j in zip(nums1,nums2):
    print(i, j)
a = 'abc'
b = 'def'
c = list(zip(a,b))
print(c)

# reverse

arr = [1,2,3]
arr.reverse()
print(arr)

# sorting
arr = [2,1,3]

arr.sort(reverse=True)
print(arr)

# sorting list:str
a = ['Bob','Li','Anna']
a.sort() by alphabet
print(a)

by len of the str with using lamba func
a.sort(key=lambda x:len(x))
print(a)

List comprehension
arr = [i+i for i in range(1,10**2+1)]
# print(arr)

arr = [[0]*4 for i in range(4)]

arr_wrong = [[0]*4]*4


s = 'abc'
print(s[0])

but they are immutable!
s[0] = 'g'
# mutable is list,dict,set
# imutable is int, str, tupple, frozenset, complex, bool, float

a = set([1,2,3,4])
b = {2:'a'}

c = ('moscow')
a.add(4)
print(c)

if input() == c:
    print('Ok')

ascii(ord)
print(ord('a'))
import collections

a = collections.deque()
a.append(1)
print(a)
a.appendleft(0)
print(a)

# hash
a = set()
a.add(2)
b = set([3])
print(a)
print(b.union(a))
print(a.remove(2))
print(a)
# hash map aka dict

a = {}
b = {}

a['alice'] = 25
b['Max'] = 32

print('alice' in a)
print(a.pop('alice'))
a['alice'] = 26
a['alice'] = 27
print(a)

a = {'alice':27, 'bob': 33}

for i in a:
    print(i, a[i])

for v in a.values():
    print(v)

for k,v in a.items():
    print(k,v)


t = tuple([1,2,3])
print(t)

for i in t:
    print(i) 
    
print(t[0])

# imutable - str, int, tupple , bool, float, complex
# mutable - list, dict, set

# unique - dict,set

import heapq

min_heap = []

heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 0)
heapq.heappush(min_heap, 9)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 102)

print(min_heap[0])
while min_heap:
    print(heapq.heappop(min_heap))
"""
"""
a = 1
b = 1

print(a==b, a is b)
a = ['a']
b = ['a']
b.append('b')
print(a==b, a is b)

# filter принимает два аргумента функцию и итерируемый объект
# фильтрует итерируемый объект на основании функции
from functools import reduce, cache
from time import time

arr = [1,2,3,4,5,6,7,8,9,10]

filtered_arr = list(filter(lambda x: x%2==0, arr))
print(filtered_arr)

reduced_arr = reduce(lambda x,y: x+y, arr)
print(reduced_arr)

@cache
def factorial(n):
    return n* factorial(n-1) if n else 1

start_time = time()
print(factorial(20), time()-start_time)

start_time = time()
print(factorial(10), time()-start_time)

start_time = time()
print(factorial(30), time()-start_time)



Интрепритатор в пайтон производит компиляцию и только после 
интрепритирует компилятор не обращает внимание на мат ошибки
а только на синтаксические 
и только интрепритатор построчно увидит мат ошибку

print(123) !ф! - ошибка от компилятора тут
a = 2/0 ошибка от интрепритатора тут


глобальные и локальные переменные!

a = 2+2
b = 3
def f(x):
    z = 11
    global a
    print(a)
    # print(globals())
    print(locals())
    
print(f(7))


try:
    import no_such_module
except ImportError as err:
    print(f" 1 - ImportError: {err.__class__}")
except ModuleNotFoundError as err:
    print(f"2 - ModuleNotFoundError: {err.__class__}")



try:
    raise ExceptionGroup('Import group', [ModuleNotFoundError(), ImportError()])
except* ModuleNotFoundError:
    print("Handling ModuleNotFoundError")
except* ImportError:
    print("Handling ImportError")


a = ['1']
b = ['']
c = ['', 1]

print(all(a))
print(all(b))
print(all(c))

print(any(a))
print(any(b))
print(any(c))


value = 'mr. Иванов'
print(repr(value)) # 'mr. Иванов'
print(value) # mr. Иванов
print(ascii(value))  # mr. \u0418\u0432\u0430\u043d\u043e\u0432

a = 3

print(bin(a))


print(bytearray('Привет, Python!', 'utf-8') )

a = 1
b = int
c = list

print(callable(a))
print(callable(b))
print(callable(c))





# print(chr(97)) #a

# Компиляция

compileted = compile('print("Hello world")', '<string>', 'exec')
print(compileted)

# string = "Hello"
# print(string.index('e'))# HELLO

# delattr(string, '')
# string.upper() # AttributeError

# print(dir(str)) 

print(divmod(10.3,3))

x = 1
print(eval('x+1'))



arr = [1,2,3,4,5,6,7]

list1 = [i for i in arr if i>3 and i<7]
print(list1)

list2 = list(filter(lambda x: x%2==0, arr))
print(list2)

x = 10.10312412213123124 / 2
print(format(x,'.2f'))


print(getattr(str, 'upper'))
# print(globals())



a = 'Hello world'

# print(hash(a))



# print(int(1,base=2)) 
a = ["apple", "banana", "cherry"]

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

li = []
for user_str in iter(input, "exit"):
    li.append(user_str)
    
print(li)


print(isinstance(1,int))

class MyClass(list):
    print('my class')
    
a = MyClass([1,2,3])

print(issubclass(MyClass, list))



a = {'a':1,'b':2}

b = {1,2,3,4,5}

iters = iter(b)


for i in range(len(b)):
    print(next(iters))



def my_decorator(arg1,arg2):
    def actual_decorator(function):
        def wrapper():
            # здесь можно использовать arg
            print(arg1,arg2)
            result = function()  # вызов оригинальной функции
            return result
        return wrapper
    return actual_decorator
        


@my_decorator('info',10)
def say_helo():
    return ("hello")

a = say_helo()
print(a)

class MyClass:
    def __init__(self):
        self._value = None
 
    @property
    def value(self):
       
        return self._value
 
    @value.setter
    def value(self, value):
        self._value = value
 
    @value.deleter
    def value(self):
        del self._value

a = MyClass()
a.value = 10
print(a.value)
delattr(a,'value') # value Удален!
b = a
print(b)

a = 10
b = a
print(b)
a = 11
print(a)
b = 'Одинадцать'



"""






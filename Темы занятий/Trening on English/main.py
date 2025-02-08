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







    


    















    
# Решение контеста 2
# Task a - пренадлежность точки к окружности

x = 0
y = 0

# (x-x0)^2+(y-y0)^2 < = R^2
def point_in_radius(x:int,y:int,r:int) -> bool:
    """Функция которая отвечает на вопрос является ли точка с координатами x,y
    внутри окружности которая стоит в центре графика с окружностью r
    """
    return 'YES' if (x-0)**2 + (y-0)**2 <= r**2 else 'NO'


def test_point_in_radius(func):
    'test point_in_radius'
    x1,y1,r1 = 0, 0, 1
    res = func(x1,y1,r1)
    if res == 'YES':
        print('test 1 - True')
    else:
        print('test 1 - False')

    x2,y2,r2 = -1, 3, 1
    
    res = func(x2,y2,r2)
    if res == 'NO':
        print('test 2 - True')
    else:
        print('test 2 - False')

# test_point_in_radius(point_in_radius)
# x,y,r = list(map(int,input().split()))
# print(x,y,r)

# задание b
# через сколько лет наберется r денег на счету вклад с суммой x увеличивающийся на r процент

# a = list(map(int,input().split()))

# if a[0] == 0:
#     print(0)
# else:
#     x,y,r = a
#     print(x,y,r)

# x,y,r = map(int,input().split())


def get_sum(*,x:int,y:int,r:int) -> int:
    
    year = 0
    while x < r:
        x += int((x/100 * y) * 100) / 100
        
        year += 1
        
    print(year)
    # return year
        
    
# get_sum(x,y,r)
def test_get_sum(func):
    print('TEST GET_SUM')
    x1,y1,r1 = 100, 10, 200
    res = get_sum(x=x1,y=y1,r=r1)
    ans = 8
    print('test 1 -True' if res == ans else 'test1 - False')
    
    x2,y2,r2 = 1, 1, 2
    res = get_sum(x=x2,y=y2,r=r2)
    ans = 100
    print('test 1 -True' if res == ans else 'test1 - False')

# test_get_sum(get_sum)

# task c


    
    
def count_one():
    m = 0
    cur = 0
    for i in range(int(input())):
        if int(input()) == 1:
            cur += 1
        else:
            m = max([m,cur])
            cur = 0
    m = max([m,cur])
    print(m)
    return m

# count_one()
    




def test_count_one(func):
    print('test count'.upper())


    x = [0,1,0,1,1,0,1,1,1,0,1,1,1,1,1]
    res = count_one(x)
    ans = 5
    print('test1- Yes' if ans == res else 'test1 - No')
    
    x = [1,1,0,1]
    res = count_one(x)
    ans = 2
    print('test2- Yes' if ans == res else 'test2 - No')
    
    x = [0,0,0,0]
    res = count_one(x)
    ans = 0
    print('test3- Yes' if ans == res else 'test3 - No')
    
    
# test_count_one(count_one)


# task d

def arr_func():
    res = []
    x = input()
    maximum = minimum = int(x)
    su = lenth = 0
    threeths = []
    tmp_threeths = []
    while x != '#':
        
        x = int(x)
        
        minimum = min((minimum, x))
        maximum = max((maximum, x))
        su += x
        lenth += 1
        if len(tmp_threeths)<3:
            tmp_threeths.append(x)
        else:
            threeths.append(tmp_threeths)
            tmp_threeths = [x]
            
        x = input()
    
    threeths.append(tmp_threeths)
    
    three = sum([(sum(i)%i[2])%i[2] for i in threeths])
    
    res = [round(su/lenth,3), maximum, minimum, three]  
    return ' '.join(list(map(str,(res))))
# print(arr_func())


# task e

a = ['@','***', '##']
a.sort(key=lambda x:len(x),reverse=True)
print(a)

def f():
    n = int(input())
    d = {}
    while True:
        s = input()
        if s == '#':
            break
        a, b = map(int, s.split())
        if a in d:
            d[a][0] += b
            d[a][1].append(b)
        else:
            d[a] = [b, [b]]
    lists = (i[1] for i in sorted(d.values(), reverse=True))
    out = sum((sorted(i, reverse=True) for i in lists), [])
    print(*out)
 
# f()

# n = int(input())
# res = 0
# all_date = [0] * (n+1)
# if n != 0 and not(n % 2):
#     all_date[0] = 1
#     all_date[2] = 3
#     if n > 2:
#         all_date[4] = 11
#     for i in range(6, n+1, 2):
#         all_date[i] = 4 *all_date[i-2] - all_date[i-4]
    
#     res = all_date[n]
# print(res)
            
        
# task
# a = input()
# x = int(input())
# print(a[:x])

# Решение контеста 2

# D-Сколько надо денег?


price, delta, m = [10, 1, 1]
# price, delta, m = list(map(int, input().split()))

# def how_much_money(price,delta,m):
#     week = 1
#     day = 1
#     total_money = 0
#     while week <= m:
#         total_money += price
#         price+=delta
#         day += 1
#         if day == 8:
#             day = 1
#             week += 1
#     return total_money

# print(how_much_money(price,delta,m))

# E-Скобочные выражения
# m = input() 
# def is_correct(m):
#     l = []
#     r = []
#     for i in range(len(m)):
#         if m[i] == '(':
#             l.append(i)
#         else:  #i == ')'
#             r.append(i)
#     if len(l) != len(r):
#         return 'NO'
    
#     for i in range(len(l)):
#         if l[i] > r[i]:
#             return 'NO'
#     return 'YES'

# print(is_correct(m))
            
            
# F-Число вхождений цифры
# digit,num = list(map(str,input().split()))

# def count_digit(digit, num):
#     count  = 0
#     for i in num:
#         if i == digit:
#             count+=1
#     print(count)
    
    
# count_digit(digit,num)

#  G-Отсортированные символы


# m = input()
# def sort_ascii(m):
#     m = sorted(m[:-1])
#     print(''.join(m) + '.')
# sort_ascii(m)

# n = int(input())
# m = [[1.8, 70.0], [1.75, 70.0], [1.8, 69.5]]
# m = []

# for i in range(n):
#     m.append(list(map(float,input().split())))

# a = sorted(m, key= lambda x:(x[0]))
# a = sorted(m, key= lambda x:(x[1]))

# for i in a:
    
#     print(round(i[0], 2), round(i[1], 2))


# J-Словарь для блондинки



n = 3
m = ['eucharis', 'fittonia', 'tagetes']
# n = int(input())
# m = []
# for i in range(n):
#     m.append(input())
    
# res = {}
# for i in range(n) :
#     if len(m[i]) not in res:
#         res[len(m[i])] = [[m[i][::-1], m[i]]]
#     else:
#         res[len(m[i])].insert(-1,[m[i][::-1], m[i]])
# s = sorted(res)
# # print(res)
# # print(s)
# for i in s:
#     print(i)
#     for j in  res[i]:
#         print(j[0], j[1])


# Скобочная система
a = '((((())'
def is_ok(a):
    n = 0
    for i in a:
        if i == '(':
            n+=1
        else:
            n -= 1
        if n < 0:
            return 'False'
    if n == 0:
        return 'True'
    return 'False'
# print(is_ok(a))


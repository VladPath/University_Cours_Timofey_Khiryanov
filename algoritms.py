


# Алгебралогики

# задача -> вернуть истину если хоть одно число делится без остатка на 10
# Bool
# flag = False
# x = int(input())
# for i in range(x):
#     # if i%10==0:
#     #     flag = True
#     flag = (i%10==0) or flag
# print(flag)
# задача -> вернуть истину если все числа делятся без остатка на 10

# flag = True 
# x = int(input())
# for i in range(x):
#     flag = flag and i%10 == 0
# print(flag)

# задача -> вернуть I,II,III,IV четверти 

# x = 1
# y = -1

# if y > 0:
#     if x > 0:
#         print('I')
#     else:
#         print('II')
# else:
#     if x < 0:
#         print('III')
#     else:
#         print('IV')
# Задание turtle
import turtle as t
# t.shape('turtle')
# Упражнения с черепахой 
# 1)
# while True:
    
#     t.shape('turtle')
#     t.forward(50)
#     t.left(90)
#     t.color('red')
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.right(90)
#     t.forward(50)
#     t.right(90)
#     t.forward(50)
#     t.penup()
#     t.goto(0,0)

# 2 - квадрат
# while True:
#     t.shape('turtle')
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.left(90)

# 3 - круг
# while True:
#     t.shape('turtle')
#     t.forward(10)
#     t.left(10)

# 4 - 10 вложенных квадратов
# point = 5
# len = 10
# n = 0
# while n < 10:
#     t.shape('turtle')
#     t.forward(len)
#     t.left(90)
#     t.forward(len)
#     t.left(90)
#     t.forward(len)
#     t.left(90)
#     t.forward(len)
#     t.left(90)
#     t.penup()
#     t.goto(-point,-point)
#     t.pendown()
#     len += 10
#     point +=5
#     n +=1

# 5 паутина с 12 лепестками
# n = 0
# while n<12:
#     t.shape('turtle')
#     t.forward(100)
#     t.stamp()
#     t.penup()
#     t.goto(0,0)
#     t.pendown()
#     t.left(30)
#     n+=1
    
# 6 - круг
# l = 10
# x,y = 1,1
# while True:
#     t.shape('turtle')
#     t.forward(10)
#     t.left(l)
#     t.forward(10)

# спираль
# import turtle
# for i in range(1000):
#     turtle.forward(i * 0.040)
#     turtle.left(10)

# квадратная спираль 
# long = 10
# for i in range(1000):
#     t.forward(long)
#     t.left(90)
#     long+=10

# функция для создания правильных многоугольников
# x=0
# y = 7
# def regylar_polygon(n, long,x,y):
#     for i in range(n):
#         t.forward(long)
#         t.left(360/n)
#     t.penup()
#     y -= 10
#     t.goto(x,y)
#     t.pendown()
#     return regylar_polygon(n+1, long,x,y)
# print(regylar_polygon(3, 50,x,y))

# def flower(radius,long,tern):
#     for i in range(73) :
#         t.forward(long)
#         t.left(radius)
#         t.forward(long)
        
#     for i in range(73) :
#         t.forward(long)
#         t.right(radius)
#         t.forward(long)
#     t.right(45)
#     return flower(radius,long,tern)

# flower(5,2,90)
# задание - бабочка 
def float(long,radius):
    r = 360//radius
    for i in range(1,r):
        t.forward(long)
        t.left(radius)
    return 

# for i in range(1,10):
#     float(i,3)
#     float(-i,3)


# # задание - пружина 

def half_float(long,radius):
    a = (360//radius)//2
    for i in range(a):
        t.forward(long)
        t.right(radius)
        t.forward(long)
    return 
# half_float(2,3)
# t.left(90)
# t.penup()
# t.goto(-100,0)
# t.pendown()
# for i in range(10):
#     half_float(2,5)
#     half_float(0.2,5)
# def paint_cirle_fill(x,y,color, long, radius):
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.begin_fill()	
#     float(long,radius)
#     t.color(color)
#     t.end_fill()
#     t.color('black')
    
# задание - Смайлик 
# t.speed(100)
# paint_cirle_fill(x=0,y=0,color='yellow', long=5, radius=3)
# paint_cirle_fill(x=-40,y=120,color='blue', long=2, radius=8)
# paint_cirle_fill(x=40,y=120,color='blue', long=2, radius=8)
# t.penup()
# t.goto(0,100)
# t.pendown()	
# t.right(70)
# t.width(10)
# t.forward(40)
# t.penup()
# t.goto(60,70)
# t.pendown()
# t.color('red')
# half_float(2,4)

# функция для создания звезды 
# def star(n):
#     for i in range(n):
#         t.forward(100)
#         t.left(180-180/n)

# n = 5

# рисуем 11 конечную звезду!
# star(11)

 
# e = int('a',base=36)

# print(e)

# def max2(x, y):
#     if x>y:
#         return x
#     else:
#         return y
# def max3(x,y,z):
#      return max2(x,max2(y,z))
 
# print(max3('ab','abc','abd '))

import turtle as t
from random import randint


# Постройка здания 

# Для этого необходимо
# заказчик - который предоставляет менеджеру местоположение здания, высоту здания, площадь здания 
#   Менеджер - обращается к подгрупам
#       1) архитектору с высотой и плоадью здания, а получает стопку бумаг с точными данными будущего здания 
                # архитекор создает размеры и данные будущего здания и возвращает их менеджеру
#       2) Прорабу который будет строить дом дает финансы и размеры и данные будущего здания от архитектора. 
            # К работникам для созведения фундамента точное место и площадь здания, возвращают готовый фундамент 
            # к работникам для возведения стен, высоту здания и расположение всех деталей, возвращаеют готовые этажи
            # к работникам для возведения крыши детали крыши и её размеры, возвращают готовую крышу
#          
#       !В случае недочетов вновь обращаются к прорабу для исправления работы
#       3) Тестировщик здания 
            # к работникам для тестировки здания готовое здание для проверки, возвращают все недочеты
            # В случае недочетов вновь обращаются к тестировщику, и если все хорошо возвращают здание менеджеру
        
        # Менеджер возвращает готовое здание заказчику 


# def manager_of_bilding(*,place:list,height:int, a:int, b:int)-> str:
#     """Функция получает локацию, разрешенную высоту и максимальную площадь будущего здания,
#     производит работу с этими данными и возвращает готовый и проверенное здание!

#     Args:
#         place (list): геолокация здания
#         height (int): Максимальная высота будущего здания
#         area (list): Максимальная площадь будущего здания

#     Returns:
#         str: Возвращает сообщение о том, что здание построено и готово!
#     """
#     maket = archetector_of_bilding(height=height,a=a,b=b)
#     bilder_ground(x=maket[0],place=place)
#     bilder_wall(x=maket[0], h=maket[1],place=place)
#     bilder_roof(x=maket[0])
    
    
    
#     print('Здание готово!')

# def archetector_of_bilding(*, height:int,a:int,b:int) -> str:
#     """Функция получает высоту и площадь здания и создает её макет 

#     Args:
#         height (int): Высота будущего здания
#         a (int): Длина места будущего здания
#         b (int): ширина места будущего здания

#     Returns:
#         list(x,h): длина и высота будущего здания
#     """
#     x = randint(10,a)
#     y = randint(10,b)
#     h = randint(10,height)
#     print('Макет здания готов')
#     return [x,h]


# def bilder_ground(*, x:int,place:list) -> str:
#     """Закладывет фундамент будущего здания и делает пол

#     Args:
#         x (int): длина будущего здания
#         place (list): Координаты здания
#     """
#     t.penup()
#     t.goto(place[0],place[1])
#     t.pendown()
#     t.forward(x)
#     print('Фундамент готов!')

# def bilder_wall(*, x:int, h:int, place: list):
#     """Эта функция получает высоту и длину здания и строит стены

#     Args:
#         x (int): Длина здания от архитектора
#         h (int): Высота здания от архитектора
#         place (list): Координаты здания
#     """
    
#     t.left(90)
#     t.forward(h)
#     t.penup()
#     t.goto(place[0],place[1])
#     t.pendown()
#     t.forward(h)
#     print("Стены готовы!")
    
# def bilder_roof(*,x:int):
#     """Функция получает длину здания и строит крышу!

#     Args:
#         x (int): Длина здания и крыши

#     """
#     t.right(90)
#     t.forward(x)
    
#     print("Крыша построена!")
        
    
    
    
    

# # x,h = archetector_of_bilding(height=100,a=70,b=70)

# manager_of_bilding(place=[randint(-200,200),randint(-200,200)], height=100,a=100, b=50)
# t.done()







# Простейший стек 

# a = [0]*1000
# top = 0

# x = int(input())
# while x != 0:
#     a[top] = x
#     top+=1
#     x = int(input())

# for i in range(top-1,-1,-1):
#     print(a[i])


# def array_search(*, a:list,n:int, x:int) -> int:
#     """Осуществляет поиск числа x в массиве a  от 0 до n-1
#        Возвращает индекс элемента x в массиве a.
#        Или -1 если элемента x нет.
#        Если в массиве несколько одинаковых элементов x,
#        То возвращает индекс первого по счету

#     Args:
#         a (list): Массив с числами
#         n (int): Длина массива a
#         x (int): Число которое необходимо найти

#     Returns:
#         int: индекс элемента x первого по счету!
#     """
#     for i in range(n):
#         if a[i] == x:
#             return i
#     return -1

# def test_array_search():
#     a1 = [1,2,3,4,5]
#     x = array_search(a=a1, n=len(a1), x=6)
#     if x == -1:
#         print("Test1 - it`s OK")
#     else:
#         print("Test1 - False")
#     a2 = [-1,-2,-3,-4,-5]
#     x = array_search(a=a2, n=len(a2), x=-3)
#     if x == 2:
#         print("Test2 - it`s OK")
#     else:
#         print("Test2 - False")
#     a3 = [10,1,2,3,4,5,10]
#     x = array_search(a=a3, n=len(a3), x=10)
#     if x == 0:
#         print("Test3 - it`s OK")
#     else:
#         print("Test3 - False")
    
    
    
# test_array_search()

# LIST COMPRECENTIONS 
# Совершение перебора внутри листа 

# a = [i**2 for i in range(10)]
# print(a)

# b = [0 if x<0 else x**2 for x in a if x%2==0]
# print(b)
# 
# 
# 

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

test_point_in_radius(point_in_radius)
    
x,y,r = list(map(int,input().split()))

print(x,y,r)

# задание b
# через сколько лет наберется r денег на счету вклад с суммой x увеличивающийся на r процент

x,y,r = list(map(int,input().split()))





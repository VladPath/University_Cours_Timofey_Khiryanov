# exam1
# a - trac


# def trac():
#     weight_trac = int(input())
#     height_truc = int(input())

#     weight_piano = int(input())
#     height_piano = int(input())

#     weight_ref = int(input())
#     height_ref = int(input())

#     max_weight = int(input())
#     max_height = int(input())
    
#     total_weight = weight_trac+weight_piano+weight_ref
#     total_height = max(height_piano,height_truc,height_ref)

#     print('YES' if total_height<=max_height and total_weight<=max_weight else "NO")
    

# trac()

# b-tungel

# def trang():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     tr = [a,b,c]
#     tr.sort()
#     if tr[0]+tr[1]<=tr[2] or tr[1]+tr[2]<=tr[0] or tr[0]+tr[2]<=tr[1]:
#         print('impossible')
#     elif tr[0]**2 + tr[1]**2 > tr[2]**2:
#         print('acute')
#     elif tr[0]**2 + tr[1]**2 < tr[2]**2:
#         print('obtuse')
#     elif tr[0]**2 + tr[1]**2 == tr[2]**2:
#         print('right')

# trang()

# c - average value

def average():
    a = []
    while True:
        value = int(input())
        if value == 0:
            print(round(sum(a)/len(a),2))
            return
        else:
            a.append(value)
# average()

# d - max even number

def max_even():
    max = 0
    while True:
        value = int(input())
        
        if value == 0:
            print(max)
            return 
        if value % 2 == 0 and value > max:
            max = value
# max_even()

# e - tribonacchi
def threebonacci():
    res = 2
    x = int(input())
    zero = 0
    first = 0
    second = 1
    while x >= second:
        curr = sum((zero,first,second))
        zero = first
        first = second
        second = curr
        res+=1
    print(res)

# threebonacci()

# f - Great common devisior
# x = int(input())
# y = int(input())

def gcd(x,y):
    while x!=y:
        if x > y:
            x = x-y
        else:
            y = y-x 
    print(x)
# gcd(x,y)  

# g - frequent number

def offen_numver():
    len = int(input())  
    max = 0
    max_cty = 0
    li = []
    for i in range(len):
        li.append(int(input()))
    for i in li:
        if li.count(i) > max_cty:
            max = i
            max_cty =  li.count(i)
    
    print(max)
    
# offen_numver()

#  H-Скалярное произведение

def dot_product(N, vector1, vector2):
    x = 0
    for i in range(N):
        x += vector1[i] * vector2[i]
    return x
        
    
    
    

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# n = len(a)
# print(dot_product(n, a, b))


# I - Максимум неполного массива

def max_not_full_arr():
    arr = []
    x = int(input())
    while True:
        if x == 0:
            print(sorted(arr[:-5])[-1])
            return
        arr.append(x)
        x = int(input())

        
        
# max_not_full_arr()

def max_not_full_arr_v2():
    x = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    max_x = x 
    while True:
        if e == 0:
            # print(x,a,b,c,d,e)
            
            print(max_x)
            return
        elif x > max_x:
            max_x = x
            
        x = int(a)
        a = int(b)
        b = int(c)
        c = int(e)
        d = int(e)
        e = int(input())


max_not_full_arr_v2()





def boards():
    n = int(input())
    colors = []
    
    for i in range(n*3):
        colors.append(int(input()))
    m = int(input())
    days = []
    
    for i in range(m):
        days.append(int(input()))
        
    res = []
    colors = [colors[i:i + 3] for i in range(0, len(colors), 3)]
    
    for j,v in enumerate(days):
        tmp = 0
        for i in range(len(colors)):
            if colors[i][0]<v and colors[i][1]>v:
                tmp = colors[i][2]
        res.append(tmp)
                
    print(' '.join(list(map(str,res))))
                 
        
# boards()
# Задание 1: найти число х входящее от 1 до 100
x = 99


# def ans(x,answer):
#     if x >= answer:
#         return True
#     return False

def bin_search(x:int):
    l = 1
    r = 100
    while l<r:
        m = (l+r) // 2
        
        if x <= m:
            r = m
        else:
            l = m+1
    return l

print(bin_search(x))


res = [1,3,4]
print(type(max(res)))
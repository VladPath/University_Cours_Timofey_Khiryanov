# нельзя использовать изменяемые объекты как стандартное значение функции
# так как оно присваивается единыжды при создании


def my_wrong_func(x:int, arr:set=set()):
    arr.add(x)
    return arr

def my_not_wrong_func(x:int, arr:set=None):
    if not arr:
        arr = set()
    
    arr.add(x)
    return arr

print(my_wrong_func(10))
print(my_wrong_func(20))
print(my_not_wrong_func(30))
print(my_not_wrong_func(40))


# ключем может быть любой неизменяемый объет или объект имеющий хеш функцию

a  = {1: 'a'}
b  = {(1,2): 'a,b'}
c  = {'a': 1}

print(b[(1,2)])

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


obj1 = MyClass(1, 2)
obj2 = MyClass(2, 3)
obj3 = MyClass(1, 2)

my_dict = {obj1: 1, obj2: 2}
my_dict[obj3] = 15
print(my_dict) # {<MyClass x=1, y=2>: 15, <MyClass x=2, y=3>: 2}
obj1.x = 20


print(obj3.x)

    
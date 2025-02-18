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

"""
### Задача: Реализация однонаправленного связного списка

Создайте класс `Node`, который будет представлять узел списка, и класс `LinkedList`, который будет представлять сам однонаправленный связный список. 

**Требования:**

1. **Класс Node:**
   - Имеет два атрибута:
     - `data`: значение, хранящееся в узле.
     - `next`: ссылка на следующий узел (по умолчанию `None`).

2. **Класс LinkedList:**
   - Имеет один атрибут:
     - `head`: ссылка на первый узел списка (по умолчанию `None`).
   - Реализуйте следующие методы:
     - `append(data)`: добавляет новый узел с заданным `data` в конец списка.
     - `prepend(data)`: добавляет новый узел с заданным `data` в начало списка.
     - `delete(data)`: удаляет узел с заданным `data` из списка. Если узел не найден, ничего не делать.
     - `find(data)`: ищет узел с заданным `data` и возвращает `True`, если узел найден, и `False` в противном случае.
     - `display()`: выводит все значения узлов в списке в виде строки.
        
        
3. **Дополнительные требования:**
   - Напишите метод `__str__` в классе `LinkedList`, который будет возвращать строковое представление списка для удобного отображения.

"""

class Node():
    def __init__(self, data, next=None) -> None:
        self._data = data
        self._next = next
    def __str__(self) -> str:
        return str(self._data)
        
class LinkedList():
    def __init__(self, head=None) -> None:
        self._head = head
        
    
    def append(self, node):
        cur = self._head
        while cur._next != None:
            cur = cur._next
        cur._next = node
        
        
    
    def prepend(self,node):
        link_list2 = self._head 
        self._head = node
        node._next = link_list2
    
    def delete(self, node):
        cur = self._head   
        if cur is node:
            self._head = cur._next
        else: 
            while cur._next != None and cur._next != node:
                cur = cur._next
            
        if cur._next is node:
            cur._next = cur._next._next
        else:
            print(f'Ошибка! Узел со значением {node} для удаления не найден')
        
            
            
    
    def find(self, node):
        cur = self._head 
        while cur._next != None and cur != node:
            cur = cur._next
        
        if cur == node:
            print(f"Найден узел - {cur}")
        else:
            print(f"Ошибка! Узел - со значением {node} не найден")
            
    
    def display(self):
        res = ''
        cur = self._head
        while cur != None:
            res += str(cur._data)+' '
            cur = cur._next
        return res
    
    def __str__(self) -> str:
        return str(self.display())
        
        
        
a = Node(2)
b = Node(1)
c = Node(3)
linked_list1 = LinkedList(a)
linked_list1.prepend(b)
linked_list1.append(c)
linked_list1.delete(c)
linked_list1.delete(c)

linked_list1.find(c)
print(linked_list1.display())
print(linked_list1)
        
        
        
        
        
        
        
        
    
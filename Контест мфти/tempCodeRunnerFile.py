x = []
y = []
for i in range(2):
    x.append(int(input()))
    y.append(int(input()))

# print(x)
# print(y)

def moves(x,y):
    return (([x[0]-2],[y[0]-1]),([x[0]-2],[y[0]+1]),([x[0]-1],[y[0]+2]),([x[0]+1],[y[0]+2]),
         ([x[0]+2],[y[0]-1]),([x[0]+2],[y[0]+1]),([x[0]+1],[y[0]-2]),([x[0]-1],[y[0]-2])
         )
    
desk = [[0] * 8 for i in range(9)]
# desk[x[0]][y[0]] = 1
# print(desk)
def chess_knight(x,y):
    """
    Программа которая может проверить сможет ли дойти конь допрыгать до желаемой точки 
    максимум за 2 хода и вернет необходимое колличество ходов если может и -1 если не сможет!
    
    >>> x = [1,8]
    >>> y = [1,8]
    >>> chess_knight(x,y)
    -1
    >>> x = [1,1]
    >>> y = [1,3]
    >>> chess_knight(x,y)
    2
    >>> x = [1,3]
    >>> y = [1,2]
    >>> chess_knight(x,y)
    1
    """
    for i in moves(x,y):
        if i[0][0] in list(range(1,9)) and i[1][0] in list(range(1,9)):
            if i[0][0] == x[1] and i[1][0] == y[1]:
                return 1
            else:
                for j in moves(i[0], i[1]):
                    if j[0][0] == x[1] and j[1][0] == y[1]:
                        return 2
                    
    return -1 
            
print(chess_knight(x,y))
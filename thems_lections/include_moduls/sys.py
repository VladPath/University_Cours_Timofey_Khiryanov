import sys
import pytest


print("start")

# print('Путь к модулям python', sys.path)
# print(sys.exit(404))
print(sys.stdin)
print(sys.stdout.write('Hello'))
print(sys.stderr.write('404'))
print("finis")

a = set(i for i in range(100000))

print(sys.getsizeof(a)//1002400)

print(sys.platform)


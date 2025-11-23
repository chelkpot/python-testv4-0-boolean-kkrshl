# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    x, y, z=map(int,input().split())
x = x ** 2
y = y ** 2
z = z ** 2
print((x + y) == z or (z + y) == x or (x + z) == y)
   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
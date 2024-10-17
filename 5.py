a, b = 1
c = 0
n = int(input())
print(a)
print(b)
for i in range(n):
    c = a + b
    a = b 
    b = c 
    print(c)
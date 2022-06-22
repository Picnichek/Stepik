a = int(input())
b = int(input())
c = int(input())

if a > b > c or c > b > a:
    print(b)
elif a > c > b or b > c > a:
    print(c)
elif b > a > c or c > a > b:
    print(a)

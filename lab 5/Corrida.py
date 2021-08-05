n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

if d1/v1 > d2/v2:
    print(n2)
else:
    print(n1)

n = int(input())
tot = 0
for i in range(n):
    l, c = map(int, input().split())
    if (l > c):
        tot += c

print(tot)
vals = []

val = int(input())
while val >= 0:
    vals.append(val)
    val = int(input())

print(*vals[::-1])

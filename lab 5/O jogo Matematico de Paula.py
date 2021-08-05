for i in range(int(input())):
    val1, op, val2 = input().strip()
    val1, val2 = map(int, (val1, val2))

    if val1 == val2:
        print(val1*val2)

    elif op == op.upper():
        print(val2-val1)

    else:
        print(val1+val2)
n = int(input())
for i in range(n):
    aux = False
    val = ''
    nums = []
    texto = input()
    for i in texto:
        if ord(i) < 58:
            aux = True
        else:
            aux = False
        if aux:
            val += i
        else:
            aux = False
            if val:
                nums.append(int(val))
                val = ''
    if val:
        nums.append(int(val))

    print(sum(nums))

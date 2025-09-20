n = int(input("number: "))

if n == 0:
    print("0")

if n > 0:
    remainderlist = []
    while n > 0:
        remainder = n % 2
        remainderlist.append(remainder)
        n = n // 2

    binaryoutput = ""
    i = len(remainderlist) - 1
    while i >= 0:
        binaryoutput = binaryoutput + str(remainderlist[i])
        i = i - 1

print(binaryoutput)

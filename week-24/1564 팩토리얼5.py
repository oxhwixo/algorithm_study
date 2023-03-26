n = int(input())
factorial = 1

for i in range(2, n + 1):
    factorial *= i

    while True:
        if str(factorial)[-1] == "0":
            factorial //= 10
        else:
            break
    factorial %= 100000000000000000 # 이유?
print(str(factorial)[-5:])
fib_num1, fib_num2, fib_sum = 0, 1, 0
while fib_num2 < 4000000:
    fib_num1, fib_num2 = fib_num2, fib_num2 + fib_num1
    if fib_num2 % 2 == 0:
        fib_sum += fib_num2
print(fib_sum)

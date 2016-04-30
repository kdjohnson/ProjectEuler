def fibonacci(n):
    a, b = 1, 2
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


sum = 0

for i in range(0, 33):
    if fibonacci(i) < 4000000:
        if (fibonacci(i) % 2) == 0:
            sum += fibonacci(i)
print(sum)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b
lcm = 1
divisor = 2

while x > 1 or y > 1:
    if x % divisor == 0 or y % divisor == 0:
        lcm *= divisor
        if x % divisor == 0:
            x //= divisor
        if y % divisor == 0:
            y //= divisor
    else:
        divisor += 1

print(f"lcm of {a} and {b} is: {lcm}")

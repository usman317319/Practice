def lcm(a, b):
    factors = []
    num1, num2 = a, b
    divisor = 2
    isinstance (num1, int) and isinstance (num2, int)
    while num1 != 1 or num2 != 1:
        if num1 % divisor == 0 or num2 % divisor == 0:
            factors.append(divisor)
            if num1 % divisor == 0:
                num1 = num1 // divisor
            if num2 % divisor == 0:
                num2 = num2 // divisor
        else:
            divisor = divisor+1

    lcm = 1
    for f in factors:
        lcm = lcm*f

    return lcm

first = int(input("enter first number:"))
second = int(input("enter second number:"))
print("lcm is", lcm(first, second))


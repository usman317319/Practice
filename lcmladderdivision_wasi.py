def LCM(num1,num2):
    divisor = 2
    arr =[]

    while num1 > 1 or num2 >1:
        if num1 % divisor == 0 or num2 % divisor == 0:
            arr.append(divisor)

            if num1 % divisor == 0:
                num1 //= divisor
            if num2 % divisor == 0:
                num2 //= divisor
        else:
            divisor +=1
    lcm = 1 
    for i in arr:
        lcm = lcm * i
    return lcm            

print(LCM(12,18))
    
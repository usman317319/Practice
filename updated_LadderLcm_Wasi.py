
def LCF(n1,n2):
    arr1 = []
    lcf1 = 0
    for i in range(2,n1+1):
        if n1 % i == 0:
            arr1.append(i)
        i += 1                       
    lcf1 = arr1[0]
    # print(f"LCF of n1 is {lcf1}")
    
    arr2 = []
    for i in range (2,n2+1):
        if n2 % i == 0:
            arr2.append(i)
        i += 1         
    # print(f"Lcf of n2 is {arr2[0]}")

    newarr = []
    newlcf = 0
    for i in range(2,max(n1,n2)+1,1):
        if n1 % i == 0 and n2 % i == 0:
            newarr.append(i)

        

    if newarr:    
        newlcf = newarr[0]
    else:
        # print(f("{n1} and {n2} have only common lcf 1"))
        newlcf = 1
    
    return newlcf

def LCM(n1, n2):
    lcmArr = []

    while True:
        if n1 > 1 and n2 > 1:
            lcf = LCF(n1, n2)

            if lcf == 1:
                lcmArr.append(n1)
                lcmArr.append(n2)
                break

            lcmArr.append(lcf)
            if n1 % lcf == 0:
                n1 //= lcf
            if n2 % lcf == 0:
                n2 //= lcf

        elif n1 == 1 and n2 > 1:
            lcmArr.append(n2)
            n2 = 1

        elif n2 == 1 and n1 > 1:
            lcmArr.append(n1)
            n1 = 1

        elif n1 == 1 and n2 == 1:
            break

    result = 1
    for num in lcmArr:
        result *= num

    return result



n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(f"LCM of {n1} and {n2} is: {LCM(n1, n2)}")

print(f"LCF of {n1} and {n2} is: {LCF(n1, n2)}")
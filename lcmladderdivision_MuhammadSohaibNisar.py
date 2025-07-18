
def cal_LCM(denum1, denum2):
    b=[]
    maximum=max(denum1, denum2)
    for i in range(2,maximum):
        if denum1%i==0 and denum2%i==0:
            x=i
            while denum1!=0 and denum2!=0:
                if denum1%x==0 and denum2%x==0:
                    denum1//=x
                    denum2//=x
                    print(f"divided by {x} :{denum1}, {denum2}")
                    b.append(x)

                    if denum1%x!=0 or denum2%x!=0:
                        for i in range(2, maximum):
                            if denum1 % i == 0 and denum2 % i == 0:
                                x = i
                                break

                    if denum1==0 or denum2==0:
                        break

                else:
                    den=denum1//denum1
                    print(f"divided by {denum1}: {den} {denum2}")
                    den2=denum2//denum2
                    print(f"divided by {denum2}: {den} {den2}")
                    break
            b.append(denum1)
            b.append(denum2)
            lcm1=(b)
            result=1
            for i in range(len(b)):
                result*=b[i]
            print(f"lcm1: {result}")
            return lcm1
        else:
            lcm = denum1 * denum2
            print(f"LCM of {denum1}, {denum2} is {lcm}")
            return lcm
cal_LCM(3,4)




def least_common_factor(a, b): 
    
    for i in range(2, min(a, b) + 1): 
        if a%i == 0 and b%i == 0: 
            return i 
    return 1 

def ladder_division(a, b): 
    
    x = 1 
    while True: 
        lcf = least_common_factor(a, b) 
        if lcf == 1: 
            print("No common factor found, stopping process")
            break
        print(f"least_common_factor = {lcf}") 
        a1 = a // lcf 
        b1 = b // lcf 
        print(f"Divide numbers: {a} / {lcf} = {a1}, {b} / {lcf} = {b1}")
        print(f"New numbers = {a1}, {b1}") 
        
        if a1 > 1 and b1 > 1: 
            print("repeat the process") 
        else: 
            print("stop the process") 
            a = a1 
            b = b1 
            break 
        
        a = a1 
        b = b1 
        x += 1 

    if a == 2 and b == 3: 
        lcf = 3 * 5 
        print(f"LCF = 3 * 5 = {lcf}") 
    else: 
        print("calculation completed") 

ladder_division(30, 45)  


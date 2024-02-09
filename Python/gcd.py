def findGCD(a,b):
    while(b != 0):
        a , b = b, a % b
    return a 

n1,n2 = int(input("Enter the N1: ")),int(input("Enter the N2: "))
print("The GCD of {} and {} is {}".format(n1,n2,findGCD(n1,n2)))
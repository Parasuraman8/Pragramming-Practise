a,b = int(input("enter the a :")),int(input("enter the b  :"))

if a<b:
    smaller = a
else:
    smaller = b

for i in range(1,smaller+1):
    if( (a%i == 0) and (b%i == 0) ):
        hcf = i
        print(hcf)

print("The H.C.F of ",a ," and ", b  ," is ", hcf)
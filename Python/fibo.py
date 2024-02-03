def fibo(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
print("Enter num limit : ")
n = int(input())
print("fibonacci series ", end= "\n")
for n in range(0,n) :
    print(fibo(n),end="\n")

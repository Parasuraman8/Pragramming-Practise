n = int(input("Enter the no:"))
i = 1
sum = 0
if (n <= 0):
    print("Enter the Positive number")
else:
    while(i<n):
        sum = sum + (i * i)
        i = i + 1
    print("The result of Natural number square : ",sum)
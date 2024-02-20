arr = []
n = int(input("Enter the no element : "))
print("Enter the element:")
for i in range(0,n):
    ele  = int(input())
    arr.append(ele)
sum = 0
for i in  arr:
    sum = sum + i
print("The Result : ",sum)
def large(arr, num):
    lar = arr[0]
    for i in range(1,num):
        if lar < arr[i]:
            lar = arr[i]
        return lar
arr = []
num = int(input("Enter the element:"))
if(num <= 0):
    print("pls enter positive number")
else:
    print("Enter the number:")
    for i in range(0,num):
        ele = int(input())
        arr.append(ele)
    print(arr)
print("the largest : ",large(arr,num))
s, e = int(input("Enter the start point: ")), int(input("Enter the End: "))

for num in range(s, e + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

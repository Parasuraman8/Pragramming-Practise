print("Control Flow In Python Programming language!!!")

'''
if
if else
elif - ladder
nested if
'''

isContinue = True

while(isContinue):
    age = int(input("Enter your age : "))

    if (age > 18):
        print("your able to vote in the election!")
        if (age < 100):
            print("our terms only for below 100")

    elif (age == 18):
        print("your age is 18 on  the border")

    else:
        print("sorry your not able to vote!!!")

    n = int(input("If YOu continue press 1 else 0"))
    if(n == 1):
        isContinue = True
    else:
        isContinue = False

for i in range(10):

    if(i == 0 ) :
        continue

    if(i == 5):
        break
    print(i)
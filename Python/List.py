print("***************************finding the length of list********************")
list1 = [1,2,3,4,'h']
print(len(list1))
list2 = [1,2,3,4,['h']]
print(len(list2))
list3 = [1,2,3,4,5,['h',2,3,3.4],4,5,6]
print(len(list3))

print("******************List Concatenate*****************")
print(list1 + list2)

print("********************List Repeatiton*******************")
print(list1 * 2)

print("****************List using Membership*****************")
print('f' is list1)

print("************list Built - in - method****************")
list1.append("hello world")
print(list1)
list1.extend("red")
print(list1)

print("****************List Copying********************")
temp = list1.copy()
print(temp)

print("***************list sorting************************")
lis4 = [4,456,4,5,1,2,3,4,5,67,8,909,2,34,56]
lis4.sort()
print(lis4)

print("*************list reverse******************")
list1.reverse()
print(list1)

print("**************clear List*****************")
list1.clear()
print(list1)
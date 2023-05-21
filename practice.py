# #String concatenations
# num =5
# print(str(num) + " is called Five")

# #abs() - absolute function minus value converted to positive 
# print(abs(-5))
# print(abs(5))

# =============================================================================
# # #max() and min()
# # #input 3 valuse and find the maximum number
# # num1 = int(input("Enter 1 number : "))
# # num2 = int(input("Enter 2 number : "))
# # num3=  int(input("Enter 3 number : "))
# # maximum_number =max(num1, num2, num3)
# # minimum_number =min(num1, num2, num3)
# # print("Maximum number is : {} and Minimum number is : {} ".format(maximum_number,minimum_number))
# 
# =============================================================================

#lists
# =============================================================================
# fruits = ["Apple", "Banana", "Cherry", "Grapes"]
# 
# for fruit in fruits:
#     print("Fruit name is : {} \nindex is : {}".format(fruit,fruits.index(fruit)))
#  
# print("\n------------------\nBefore Modifiable\n-------------------\n ")
# #mutable
# fruits[1] = "Mango"
# 
# for fruit in fruits:
#     #index()
#     print("Fruit name is : {} \nindex is : {}".format(fruit,fruits.index(fruit)))
# =============================================================================


# =============================================================================
# 3Name = "Asardeen"
# print(3Name)
# #Syntax Error - Naming convention
# =============================================================================


# =============================================================================
# # fruits = ["Apple", "Banana", "Cherry", "Grapes"]
# # #fruits.clear()
# # number = [1,2,3,4]
# # number.extend(fruits)
# 
# # print(number)
# =============================================================================

# =============================================================================
# num = [1,2,3,4,5,6]
# #      0 1 2 3 4 5
# #how to find the index value of 2
# print(num.index(2))
# 
# #Remove the value of 2
# #pop() - given index value
# num.pop(1)
# print("After Remove the value of 2")
# print(num)
# 
# 
# 
# =============================================================================

# =============================================================================
# lists_number = [10,60,30,50,70,89]
# new_list = []
# for list in lists_number:
#     new_list.append(list)
# print(new_list)
# delete_value = int(input("Enter value : "))
# insert_pop=lists_number.index(delete_value)
# lists_number.pop(insert_pop)
# print(lists_number)
# =============================================================================

# =============================================================================
# 
# lists_number = [10,60,30,50,70,89,60,60]
# print(lists_number)
# print(id(lists_number))
# 
# lists_number.append(65)
# print(lists_number)
# print(id(lists_number))
# 
# num = 10
# print(id(num))
# 
# num = num + 1
# print(id(num))
# 
# 
# 
# 
# =============================================================================

#extend()
# =============================================================================
# A = [1,2,3]
# B = [4,5,6]
# C = [8,9,10]
# A.extend(B) # A= [1,2,3 extend 4,5,6 ]--> A = [1,2,3,4,5,6]
# print(A)
# print(B)
# B.extend(C)
# print(B)
# 
# =============================================================================

# =============================================================================
# 
# #append() add data from end of the Lists
# A = [1,2]
# A.append(3)
# A.append(4)
# A.append(7)
# A.append(5)
# print(A)
# 
# #Sort method default Ascending
# A.sort()
# print(A) 
# 
# #Descending Order
# A.sort(reverse=True)
# print(A)
# 
# 
# B = [1,2,3,4]
# print(B)
# 
# B.insert(1,6)
# print(B)
# 
# # Remove data one by one from end of the list
# B.pop()
# B.pop()
# print(B)
# =============================================================================

# =============================================================================
# stu_name = ["Asardeen","Sara","Dave","Venu"]
# 
# # getting name for remove
# 
# name =input("Enter Student name : ")
# total=stu_name.count(name)
# if(total > 0):
#     stu_name.remove(name)
#     print("You are entered name is totally : {}".format(total))
#     print("Successfully remove name is : {}".format(name))
#     print(stu_name)
#     
# =============================================================================
    

# =============================================================================
# name = ["A", "C", "B", "D"]
# name.sort()
# print(name)
# 
# name.sort(reverse=True)
# print(name)
# 
# name1 = ["Asardeen", "Car", "Bulkeriya", "Donkey" ,"Cat"]
# 
# name1.sort()
# print(name1)
# 
# name1.sort(reverse=True)
# print(name1)
# 
# print("------------------------------------------------------")
# 
# 
# name2 = ["Asardeen", "Car", "Bulkeriya", "Donkey" ,"Cat"]
# print(name2)
# name2.reverse()
# print(name2)
# 
# =============================================================================


print(len(123))













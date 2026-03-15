#  CREATE CLASS
# class preson:
#     def __init__(self, name,age,place):
#         self.name = name
#         self.age = age
#         self.place= place
# p1 = preson("Bhanu",25,"hathoda")
# print(p1.name)
# print(p1.age)
# print(p1.place)



# class car:
#     def __init__(self, name , speed , color):
#         self.name = name
#         self.speed = speed
#         self.color = color
# car = car('BMW',250,'blue')
# print(car.name)
# print(car.speed)
# print(car.color)



# class student:
#     def __init__(self,name,roll_no,Class,marks,phone_no):
#         self.name = name
#         self.roll_no = roll_no 
#         self.Class = Class
#         self.marks = marks
#         self.phone_no = phone_no
# student = student('Mohan',70,6,75,72482136)
# print(student.name)
# print(student.roll_no)
# print(student.Class)
# print(student.marks)
# print(student.phone_no)
  

# class person:
#     def __init__(self,name,age,place):
#         self.name = name
#         self.age = age
#         self.place = place
        
#     def greet(self):
#         print("My name is " + self.name +' ' "and i am from " + self.place)
# person = person("Bhanu pratap",25,"Mathura")
# person.greet()

# class person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return "hello, "+ self.name
    
#     def welcome(self):
#         message = self.greet()
#         print(message + " ! welcome to our home.")
# person = person("Bharat")
# person.welcome()

# num = input("Enter a number: ")
# if num == num[::-1]:
#     print("number is palandorome")
# else:
#     print("number is not palandorome")

# str = "hello"
# str1 = " "
# for i in str:
#     str1 = i +str1
# print(str1)

# num = int 
# for  i in range(2,num):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")


# x = 5
# y = 10
# x = x + y  # x is now 15
# y = x - y  # y is now 5 (15 - 10)
# x = x - y  # x is now 10 (15 - 5)
# print("x:", x)
# print("y:", y)

# num = int (input("enter a number: "))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
# print("factorial of", num, "is",factorial)
 #slicing
str ="bhanu pratap"
print(str[0:4])

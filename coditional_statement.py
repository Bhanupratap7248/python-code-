age = int(input("enter your age:   "))
if(age>=21):
    print("you can drive the car")
elif(age>=18):
    print("you can drive the car with supervision")
elif(age>=16):
    print("you can drive the car with supervision and you need to have a learner's permit")
else:
    print("you cannot drive the car")
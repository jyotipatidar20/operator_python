age_1=int(input("enter a age_1:"))
age_2=int(input("enter a age_2:"))
age_3=int(input("enter a age_3:"))
if(age_1>age_2>age_3):
    print("age_1 younger hai")
elif(age_1 < age_2 < age_3):
    print("age_3 oldest hai")
elif(age_1 < age_2 > age_3):
    print("age_2 youngest hai")
else:
    print("young nahi hai")
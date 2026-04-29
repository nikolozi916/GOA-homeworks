# if-ამოწმებს პირობას.
# else-მუშაობს მაშინ,როცა პირობა არ შესრულდა.


num = int(input("Enter number: "))

if num > 0:
    print ("num > 0")
elif num < 0:
    print ("num < 0")
else:
    print ("num = 0")


password = input ("Enter password")

if password == "goal123":
    print ("password is correct!")
else:
    print ("Incorrect password!")


import random 

num = random.randint(1, 10)

print("Generated number is:", num)

if num > 5:
    print ("number > 5")
else:
    print ("number <= 5")
    
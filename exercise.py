from pprint import pprint
import getpass

'''
fruits = ["apple", "pawpaw", "orange", "pear", "mango"]
x = x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [ {"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1} ]
}

maginumber = [(1,2),(23,4),(23,8)]
hello = "My name if koji Bello and i'm the lead Devops Engineer at plastig"


for fruit in fruits:
    print(fruit)

##list comprehension
fruit = [fruit for fruit in fruits]
print(fruit)

'''



# name = "maryya mennen"
# count = 0
# for i in name:
#     if i != 'n':   
#         continue
#     else:
#         count = count + 1 
#         print(count)

'''
name = "mariya mennmbellm men"
count = 0
for m in name:
    if m != 'm':
        continue
    else:
        count =  count + 1    
print("The amount of time m occured is:", count)

'''

# number = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in number:
#    # print(i)

# name = "hallelujah hallelujah"
# count =0
# for i in name:
#     if i != 'l' :
#            continue
#     else:


password = "kojitechs123"
user_guess = ""
user_atempt = 3 

# first condition "if user_atempt not == 0", user_guess!=password
'''
while user_guess != password and user_atempt !=0:
    user_guess = getpass.getpass("Enter password: ")
    user_atempt -=1
    if user_atempt==0: 
        print("Sorry you have exhausted the limit of 3")  
        
    if user_guess == password:
        print("Login succesful!")
        
    else:
        print(f"You have {user_atempt} attempt left")
'''
# number = eval(input("Enter number: "))
# count = 1
# while count <= 10:
#     product = number * count
#     print(number, "x", count, "=", product)
#     count = count + 1

# count = 1
# while count<11:
#     pprint(dir (count))
#     count += 1


count=0
while(count <=100):
    if (count % 2 == 0 and count<=100):
            print(f"{count} is an even number")
    count = count+1
    if (count % 2 != 0 and count<100):
        print(f"{count} is an odd number")
    count  += 1
else:
    print(f"{count} is out of range")
    

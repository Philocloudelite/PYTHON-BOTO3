
from pprint import pprint

#string casting
x = 1
y = 2
''' 
x,y = 1,2
print(x)
print(y)
print(x,y)

#list casting
fruits, *second_var = ["apple", "pawpaw", "plum", "orange"]
print(fruits)
print(second_var)

fruits, second_var, *third_var = ["apple", "pawpaw", "plum", "orange"]
print(third_var)

'''



## Dictionary casting

#my_dict = {"name": "philo", "country": "Cameroon", "age": 24, "sex": "female"}
my_dict_1 = dict(name= "philo", country= ["cameroon","Ghanna", "nigeria", "Italy"], age= 24)
# print(my_dict_1.items())

## iterate over the keys

for key, value in my_dict_1.items():
    pass 
    # print(key)
    # print(value)
    # print(key,value)
    # print(f"the keys are: {key}: {value}")

'''
hello = "my name is koji\nmy age is 24\nmy i'm African"
print(hello)
'''


## extending the dict
thisdict = { "brand": "Ford", "model": "Mustang","year": 1964}
thisdict["country"] = ["Nigeria", "Cameroon", "Ghanna"]
#print(thisdict)

keys = {'a','e', 'i', 'o', 'u'}
vowels = thisdict.fromkeys(keys,value )
#print(vowels)

keys = {'a','e', 'i', 'o', 'u'}
value = 1  # or it could still be [1,3] as value
vowels = thisdict.fromkeys(keys,value )
#print(vowels)


new_dict = { "brand": "Ford",
 "model": "Mustang",
 "year": 1964, 
 "country": ["Nigeria", "Cameroon", "Ghanna"]}
#print(new_dict('country'))


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}
new = people.get(4)
#print(f"mr. peter's age is {new.get('age')},\nhis name is {new.get('name')}")

# Assignment 

# print out all the prouct that is greater than 500
#pprint(dir(products))
#print(products)
#print(products[3])

# append takes just one argument and it adds a new item to the existing list
# sub_product = products.append(2000)  # or put in "product_5"
#print(products)

# products = [
#     ("product_1", 200),
#     ("product_2", 400),
#     ("product_3", 900),
#     ("product_4", 1000)
# ]

# products.append(("product_5", 2300))
# print(products)


# for i in products:
#     if i[1] >=500:
#         print(i)


# #OR
# result = [item for item in products if item[1] > 500]

# #OR
# # the foor_loop expression
# for item in products:
#     if item[1] >= 200:
#         print(item)

# #OR
# # for filter builtins method
# pprint(dir(builtins))
# x = [item for item in products]
# print(products)

# filter(lambda item:item[1] >=200, products)
# # will come out in a generated object

## Arithmetic operator
hundreds = list(range(1,100))
for i in hundreds:
    if i %2!=0:
        pass
        #print(i)
    #else:
        #print(f"Even: {i}")
        #print(f"Odds: {i}")


  ## comparison operator
# credit applicant must not be a student and the applicant must b above 18 and have a job

working_stutus = input("Are you working?: ")
age_of_applicant = eval(input("what is your age: "))
JobTittle = input("what is your occupation: ")

if (age_of_applicant > 18 and working_stutus.lower() =='yes' and JobTittle.lower() !='student'):
    print("Congrats koji\nYou were APPROVED!")
else:
    print("Opps!, Sorry we don't give out loans to students")    

 #identity operator 


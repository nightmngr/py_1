# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#
#%%
# import libraries
from datetime import date
#
#%%
# get name
def get_name():
    name = input("name: ").capitalize()
    return name
#%%
# get age
def get_age():
    try:
        age = int(input("age: "))
        if (age>100):
            raise Exception("You are too old!")
        return age
    except ValueError:
        print("Invalid number for age!")

# get years to 100
#%%
def years_to_100(age):
    res = datetime.date.today().year + (100-age)
    return res



#%%
# get values
name = get_name()
age = get_age()
to_100 = years_to_100(int(age))
rep = int(input("how many times? "))

# print
print("Name is: " + name)
print("age is: " + str(age))
print(rep * (name + ", you will turn 100 in " + str(to_100) + "\n"))
#%%
years_to_100(90)
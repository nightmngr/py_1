#
# hotel
def hotel_cost(nights):
  return 140 * nights

# plane
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  
# rent a car  
def rental_car_cost(days):
  day_cost = 40
  if days>=7:
    return days*day_cost - 50
  elif days>=3:
    return days*day_cost - 20
  else:
    return days*day_cost
  
# total trip  
def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)




# arrays /
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("swim suit")
suitcase.append("regular suit")
suitcase.append("jeans")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase


suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2] # pocnuva od prviot index ama go isklucuva vtoriot

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last =  suitcase[4:6] # zatoa tuka vtoriot index len(suitcase) + 1
# za do kraj mozes da go ispustis vtoriot index
# za skroz od pocetok mozes da go ispustis prviot index
animals = "catdogfrog"
# The fourth through sixth characters
dog = animals[3:6]
# From the seventh character to the end
frog = animals[6:]

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
# Use index() to find "duck"
duck_index = animals.index("duck") 
# Your code here!
animals.insert(duck_index, "cobra")
# Observe what prints after the insert operation
print animals 


start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number ** 2)

square_list.sort()
print square_list


# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number
print residents["Sloth"]
print residents["Burmese Python"]

menu = {} # Empty dictionary
# Adding new key-value pair
menu['Chicken Alfredo'] = 14.50 
print menu['Chicken Alfredo']

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

# / arrays
#
#
#
#
# lists /

shopping_list = ["banana", "orange", "apple"]
stock = { "banana": 6, "apple": 0, "orange": 32, "pear": 15 }
prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3 }

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total = total + prices[item]
      stock[item] -= 1
  print total
  return total

# smetka
compute_bill(shopping_list)
print stock

# / lists
#
#
#
#
# vezba so studenti /

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers);
  return float(total)/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  
print get_letter_grade(get_average(lloyd))

def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)

students = [alice, lloyd, tyler]
class_avg = get_class_average(students)
print class_avg
print get_letter_grade(class_avg)

# / vezba so studenti
#
#
#
#
# range (lists) /
"""
### Iterating over a list in a function ###

Now that we've learned about range, we have two ways of iterating through a list.

Method 1 - for item in list:

for item in list:
  print item

Method 2 - iterate through indexes:

for i in range(len(list)):
  print list[i]

Method 1 is useful to loop through the list, but it's not possible to modify the list this way.
Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed. 
"""
# / range (lists)
#
#
#
#
# loops /

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"

# strings in loobs:

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  print key, " ", d[key]

# zapirka znaci da prodolzi vo istiot red
# vo slucajov se koristi kako konkatanacija




# enumerate dava indeksi na lista
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index+1, item



# zip se koristi za vrtenje na 2 ili povekje listi
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if a >= b:
    print a
  else:
    print b

# / loops
#
#
#
#
# advanced topics /

# list comprehension
# pr: parni od 0 do 50

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print "Parni od 0 do 50:"
print evens_to_50

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]


# list slicing
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message


# lambda (anonymous functions)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message

# / advanced topics
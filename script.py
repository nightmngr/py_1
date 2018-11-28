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
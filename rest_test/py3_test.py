# hotel
def hotel_cost(nights):
    return 90 * nights

# print(hotel_cost(3))

# plane
def plane_ride_cost(city):
    if city == "Skopje":
        return 180
    elif city == "Malta":
        return 220
    elif city == "Hamburg":
        return 400

# print(plane_ride_cost('Malta'))

# rent a car
def rental_car_cost(days):
    day_cost = 40
    if days >= 7:
        return days * day_cost - 50
    elif days >= 3:
        return days * day_cost - 20
    else:
        return days*day_cost

# print(rental_car_cost(2))

# total trip
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

final_cost = trip_cost("Hamburg", 4, 1000)

# print("Patuvanjeto ke cini: %d €" % (final_cost))

# arrays /
suitcase = []
suitcase.append("sunglasses")
# print(suitcase)

list_length = len(suitcase)

# print("There are %d items in the suitcase." % (list_length))

lettrs = ["a", "b", "c"]
if lettrs.#check if lettrs has "d"
    print(lettrs.index("d"))
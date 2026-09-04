#Welcoming Statements
print("Wlecome to the Disneyland Trip Budget Calculator")
print("Im going to ask you some questions about your upcoming trip")
print("Then i will ask some questions to calculate your budget")

#Code used to Gather trip info
name = input("What is your name")
number_of_people = int(input("How many people will be on the trip?"))
number_of_park_days = int(input("How many Days will you be at the Park?"))
number_of_hotel_nights = input("How many nights will you spend at a hotel")
hopper_ticket_price = float(input("Whats the price per park hopper ticket?"))
total_ticket_price = number_of_people * hopper_ticket_price
three_meal_cost_per_person = float(input("How much will each person spend daily on food?"))
total_meal_cost_per_person = float(three_meal_cost_per_person * number_of_park_days)
souvenir_cost_per_person = float(input("How much will each person spend on Souvenirs"))
total_souvenir_cost_per_person = float(souvenir_cost_per_person * number_of_people)
hotel_room_cost_per_night = float(input("How much does each hotel room night cost?"))
hotel_room_amount = int(input("How many hotel rooms will you need?"))
daily_room_cost = hotel_room_cost_per_night * float(hotel_room_amount)
total_hotel_cost = daily_room_cost * int(number_of_hotel_nights)
one_way_distance = input("How many miles do you live from disneyland?")
vehicle_MPG = input("How many miles per gallon does your car get?")
gas_charge = float(input("What is the current gasoline cost in your city"))
total_round_trip_distance = int(one_way_distance) * 2
total_gas_needed = total_round_trip_distance / int(vehicle_MPG)
total_gas_cost = total_gas_needed * gas_charge
parking_cost = float(input("How much does Disneyland parking Cost Per day?"))
total_parking_cost = parking_cost * number_of_park_days
final_trip_cost = total_ticket_price + total_meal_cost_per_person + total_souvenir_cost_per_person + total_hotel_cost + total_gas_cost + total_parking_cost
cost_per_person = final_trip_cost / number_of_people
cost_per_day = final_trip_cost / number_of_park_days
trip_budget = float(input("What is your Budget for your Disneyland trip?"))
#Assortment of floats used to gather monetary values


#Final Report
print("TRIP INFO")
print("Name:" + name)
print("People going:" + str(number_of_people))
print("Park days:" + str(number_of_park_days))
print("Hotel Nights:" + number_of_hotel_nights)
print("")
print("PARK HOPPER TICKETS")
print("price per park hopper ticket: " + str(hopper_ticket_price))
print("Total Ticket Price:" + str(total_ticket_price))
print("")
print("FOOD & SOUVENIERS")
print("Total meal price: " + str(total_meal_cost_per_person * number_of_park_days))
print("Total souvenir cost: " + str(total_souvenir_cost_per_person))
print("")
print("HOTEL COSTS")
print("total_hotel_cost: " + str(total_hotel_cost))
print("")
print("DRIVING")
print("One-way-trip Distance: " + str(one_way_distance))
print("Round-Trip Distance: " + str(total_round_trip_distance))
print("Vehicle MPG: " + str(vehicle_MPG))
print("Gas Price: " + str(gas_charge))
print("Gallons needed: " + str(total_gas_needed))
print("Total Gas Cost: " + str(total_gas_cost))
print("Total Parking Price: " + str(total_parking_cost))
print("")
print("TRIP TOTAL")
print("Final Disneyland Trip Cost: " + str(final_trip_cost))
print("Cost per person: " + str(cost_per_person))
print("Cost per day: " + str(cost_per_day))
print("")
print("BUDGET")
print("Trip Budget: " + str(trip_budget))
print("Budget Difference: " + str(trip_budget - final_trip_cost))
print("")
print("Thank you for your time and remeber, have a wonderful day at the worlds most happiest place!")
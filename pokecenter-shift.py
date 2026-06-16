# Pokecenter Shift Simulation
import random
nurse_name = input("Welcome! What is your name? ")
if nurse_name != "Joy":
	import sys
	exit("It's not your shift today!")
else:
	print("Good morning, Nurse " + str(nurse_name) + "!")
	print("Let's get started! We don't want to leave our patients hanging!")

nurse_capacity = 5
pokemon_waiting = 0
pokemon_arrivals = 0
pokemon_healed = 0
grand_total = 0

for shift in range (1, 13):
	pokemon_arrivals = random.randint(0, 8)
	pokemon_waiting = pokemon_waiting + pokemon_arrivals
	pokemon_healed = min(nurse_capacity, pokemon_waiting)
	pokemon_waiting = pokemon_waiting - pokemon_healed
	grand_total += pokemon_healed
	print("Hour " + str(shift) + ": " + str(pokemon_waiting) + " are still waiting in line.")

if pokemon_waiting >= 20:
	print("Nurse " + str(nurse_name) + ", the lobby is getting crowded! Lock in!")
print("Shift over! Total Pokemon healed today: " + str(grand_total) + "." + " Pokemon left in line: " 
	+ str(pokemon_waiting) + ".")

import random, sys

class Collectibles:

	coll_points = 0

	def collect(self, points):
		print("Collected {} points".format(points))
		 
	def levelUp(self, total):
		if total == 300:
			print("You have leveled UP!!!!")
		


class Coins(Collectibles):

	def __init__(self):
		typeOfcoin = ["gold", "silver"]
		# randomising the type of coin at the construct stage
		self.name = typeOfcoin[random.randint(0, 1)]


	def collect(self, points):

		## our implementation of the parent collect() method as
		## we need to change it by adding the total coin points

		# calling the parent collect(self) method for that print of collected points
		super().collect(points)
		# Increasing the Collectibles coll_points (Coins class implementation. 
		# Notice how we don't declare coll_points again because it is a Class variable 
		# of the Collectibles class and we implement it for Coins.
		Coins.coll_points += points
		print("Total Coin points {}".format(Coins.coll_points))

		# Check if we have leveled up yet
		self.levelUp(Coins.coll_points)



class Potions(Collectibles):

	global greenPotion 


	def __init__(self):
		typeOfpotion = ["magic", "health"]
		colourofPotion = ["green", "pink"]
		# randomising the type and colour of potion at the construct stage
		self.name = typeOfpotion[random.randint(0,1)]
		self.colour = colourofPotion[random.randint(0,1)]

	def collect(self, points):

		## our implementation of the parent collect() method as
		## we need to change it due to the collect green potion functionality

		super().collect(points)

		if self.colour == "green":
			if Potions.coll_points != 50 and Potions.coll_points != 0: 
				Potions.coll_points -= 100
				print("Green potion! You lost 100 points. You now have {} Potion points.".format(Potions.coll_points))
				# increase Collectible coll_points (Potions class implementation)
				# Potions.coll_points += points - 100
				print("Total potion points {}".format(Potions.coll_points))

			else:
				print("Green potion! You lost 100 points. Your Potions points are 0")
				Potions.coll_points = 0

			greenPotion = True
				
		else:
			Potions.coll_points += points
			print("Total potion points {}".format(Potions.coll_points))
			
			self.levelUp(Potions.coll_points)
			

### End of Classes declaration
		


# GLOBAL VARIABLES
total_sum = 0
# greenPotion boolean is used to flag up green potion collection
greenPotion = False
# A list for coins and potions. If your game demands it you could have also two different lists
# one for coins and one for potions.
list_of_collectibles = []


# Main Loop
while True:

	while total_sum <= 600:

		# Try/Except to capture unwanted input
		try:

			pl = int(input("Enter a number between 1 and 6: "))
		
			if pl in range(1,4):
				# append a coin
				list_of_collectibles.append(Coins())
				# we get the last entered collectible - the one we just appended
				# and add the corresponding points  
				list_of_collectibles[len(list_of_collectibles) - 1].collect(20)
				total_sum += 20


			elif pl in range(4,7):
				# append a Potion
				list_of_collectibles.append(Potions())
				# as above
				list_of_collectibles[len(list_of_collectibles)-1].collect(50)
					
				if greenPotion and total_sum > 100:
					total_sum -= 100
					greenPotion = False
				elif greenPotion:
					total_sum = 0
					greenPotion = False
				else: 
					total_sum += 50

			else:
				print("Only numbers between 1 and 6 please!")


			print("Total points:{}".format(total_sum))
			 
			 # If the user inputs anything else but a number between 1-6
		except ValueError:
			print("Only numbers please!")

			# If the user inputs a CTRL+C to exit (or Windows equivalent exit shortcut) capture 
			# this and exit
		except KeyboardInterrupt:
			print("Bye Bye")
			sys.exit()

		
	# Game continues....
	input("Where next ? s/n/e/w")


	 

 
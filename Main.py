# Marvins Rochemont, Prof. Osheroff, COP1500
# A simple program for math functions, basically a calculator

# Main issue of code currently is that every input is being used with the selection, which leads to confusion.
# Could have simple operations scrapped for more "higher learning" formulas. This would be the prototype, essentially.


# Main Intro
def main():
	print("Welcome to the Math Manager!")
	start = input("Would you like to start?: ")
	if start.startswith("Y"):
		print("Great!")
		menu1()
	else:
		print("Goodbye!")
# Menu


def menu1():
	usr_select = input("Add, Subtract, Multiply, Divide or more?: ")

	if usr_select == "Add" or "add":
		add1 = int(input("What's the first number you want to add?: "))
		add2 = int(input("What's the second number you want to add?: "))
		calculateSum(sum)
	elif usr_select == "Subtract":
		sub1 = int(input("What's the number you want to subtract?: "))
		sub2 = int(input("What's the number you want to subtract it by?: "))
		calculateDiff(sub1 - sub2)
	elif usr_select == "Multiply":
		factor1 = int(input("What's the first factor?: "))
		factor2 = int(input("What's the second factor?: "))
		calculateProduct(factor1 * factor2)
	elif usr_select == "Divide":
		dividend = int(input("What's the dividend?: "))
		divisor = int(input("What's the divisor?: "))
		calculateQuotient(dividend / divisor)
	elif usr_select == "more" or "More":
		menu2()
	elif usr_select == "back" or "Back":
		main()
	else:
		print("Invalid choice. Try again or enter 'back' to leave the menu.")


def menu2():
	usr_select2 = input("Mass, Density, Volume, or more?: ")
	if usr_select2 == "Mass" or "mass":
		density = int(input("What's the density of the object?: "))
		volume = int(input("What's the volume of the object?: "))
		calculateMass(density * volume)
	elif usr_select2 == "Density" or "density":
		mass = int(input("What's the mass of the object?: "))
		volume = int(input("What's the volume of the object?: "))
		calculateDensity(mass / volume)
	elif usr_select2 == "Volume" or "volume":
		mass = int(input("What's the mass of the object?: "))
		density = int(input("What's the density of the object?: "))
		calculateVolume(mass / density)
	elif usr_select2 == "More" or "more":
		menu3()
	else:
		print("Invalid choice. Try again or enter 'back' to leave the menu.")

# Calculation Hub


def calculateSum(sum):
	sum = add1 + add2


# Call to Main


main()
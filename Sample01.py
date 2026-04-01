#!/usr/bin/python3


number = int(input("Enter a number:"))
def calculation(number):
	if number < 5:
		print(number,"is less than 5")
	elif number >= 5:
		print(number,"is  greater than or equal to 5")
	else:
		print("Error")
	return

calculation(number)

#!/usr/bin/python3


def calculation (num):
	if num < 5:
		print(num,"is less than 5")
	elif num >= 5:
		print(num,"is greater than or equal to 5")
	else:
		print("Error")
	return
number = int(input("Enter a number:"))
calculation (number)

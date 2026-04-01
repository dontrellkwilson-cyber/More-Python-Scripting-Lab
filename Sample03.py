#!/usr/bin/python3


def calculation(num):
	if num < 5 and number > 0:
		print(num,"is between 0 and 5")
	elif num >= 5 and num < 10:
		print(num,"is equal or greater than 5 less than 10")
	elif num > 10 or num < 0:
		print(num,"That number is not between 1 and 10!")
	else:
		print("out of range")
	return
number = int(input("Enter a number: "))

calculation(number)

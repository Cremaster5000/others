"""In this exercise i tried to translate binary numbers to decimal without
using explicit builded in functions."""

def translate(number):
	digit = 0
	for i in range(len(number)):
		digit += int(number[-i])*(2**i)
	print(f'Decimal: {digit}')

number = str(input("Introduce a number in binary format: "))
translate(number)
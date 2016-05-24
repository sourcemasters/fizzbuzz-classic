# Dirty Dozen Challenge, Entry 1 of 12
#  solution to the "Fizz Buzz Test":
def fizzBuzz():
	for i in range(1, 101):
		print i,

		if (i % 3 == 0):
			print " Fizz",
		if (i % 5 == 0):
			print " Buzz",

		print ""

if (__name__ == "__main__"):
	fizzBuzz()

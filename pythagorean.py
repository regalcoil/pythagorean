def pt():
	print(" ")
	print("Please enter the dimensions of your triangle?")
	print(" ")
	a = float(input("How many units is side a of your triangle? "))
	print(" ")
	b = float(input("How many units is side b of your triangle? "))
	print(" ")
	c = (a*a) + (b*b)
	c = c**0.5
	print("The hypotenuse of your triangle is: " + str(c) + " units^2")
	print(" ")
	print("*****************")
	pt()
pt()
def factorial(num):
  if num == 1:
	return num
  else:
	return num * factorial(num-1)
Number = int(input("Enter the number to find Recurdion:"))
#result=recursion(Number)

result = factorial(Number)
print "recursion factorial is ", result
	


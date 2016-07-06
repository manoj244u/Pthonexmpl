def recursion(num):
	if num==1:
		return num
	else:
		return num*recursion(num-1)
Number=int(input("Enter the number to find Recurdion:"))
#result=recursion(Number)

result=recursion(Number)
print("recursion factorial is ", result)
	


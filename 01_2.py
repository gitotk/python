v = False

for i in range(5):
	for j in range(5):
		if v is False:
			print("*", end="")
			v = True
		else:
			print("_", end="")
			v = False
	print()

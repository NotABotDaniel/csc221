print("fibinachi sequence")
x = 1
y = 1
print(x)
print(y)
for a in range(20):
	z = x + y
	x = y
	y = z
	print(z)
print("done")

# cases

sky_is_blue = True

squared = 0

def square(x):
	global squared
	squared = x * x
	# using function variable IN function
	print "(inside function) squared is equal to %d" % squared
	return squared	

if sky_is_blue:
	y = 24
	# using block variable INSIDE block
	print "(inside block) y is equal to %d" % y	
else:
	y = 5
	print "(inside block) y is equal to %d" % y	

# using block variable OUTSIDE block
print "(outside block) y is equal to %d" % y

# using function variable OUTSIDE function
answer = square(y)
print "(outside function) answer is equal to %d" % answer
print "(outside function) squared is equal to %d" % squared

##Test Print Hello World
print "Hello World"

#C-ish Syntax 
print 'This string has a number {}'.format(10)

#iteration
tee = ('apple', 'orange', 'banana')
i = iter(tee)
i.next()
i.next()
i.next()

def infinity():
	count = 0
	yield count
	while True:
		count += 1
		yield count
		
inf = infinity()
inf.next()

for i in inf:
	print i
	if i % 3 == 0:
			break
	
#range
print(range(10))

print(range(3, 10))

#skip
print(range(3, 10, 3))

#xrange
#for i in xrange(200):
	#print(i)
	

"""
fp = open('test.txt', 'w')
fp
fp.write("some value hey there!")
fp.close()
"""

#everything is a class in Python
#sum.__class__

#sets only list unique values 
#set([1, 1, 2, 2, 3, 3])

"""
name = 'Krystal Maughan'
first, last = name.split()
"""

#if else expression for boolean evaluation
print(0 if 1 == 1 else 2)

#Lambdas
even_or_odd = lambda x: 'even' if x % 2 == 0 else 'odd'
print(even_or_odd(23))

scores = (('Krystal', 123), ('Nz0', 256), ('DG', 1024))
print(list(sorted(scores,key=lambda x: x[1], reverse=True)))
print(list(sorted(scores,key=lambda x: x[1], reverse=False)))

age = 99
if age <= 10:
	print 'Hey kiddo'
elif age > 10 and age <= 18:
	print 'sup buddy'
elif age > 18 and age <= 30:
	print 'hey you can drive'
else:
	print 'age is just a number'

##while loop
counter = 10	
while counter >= 0:
		print 'Counting down..{}'.format(counter)
		counter -= 1
###
		

"""
		#for loop
		l = range(10)
		for i in l:
			print 'Item: {}'.format(i)
			"""

divider = lambda x, y: x / (y - 1)
divider(3, 2) == 3 / 1

try:
	value = divider(3, 1)
except ZeroDivisionError, e:
	print 'Slow down there L\'Hopital'
	value = None

#### add ten
def add_ten(x):
	"""Returns the number x plus 10, given x is a number"""
	return x + 10 if isinstance(x, int) else None

print(add_ten(10))
print(add_ten('Krystal'))

## add two
def add_two(first, second):
	return first + second
	
##args function
def print_args(*args):
	for arg in args:
		print 'Argument: {}'.format(arg)
		
print_args()
print_args(1, 2, 3)

###
def mix(one, *args):
	mixed = 0
	for arg in args:
		mixed += arg * one
	return mixed
	
print(mix(1,2,3))
print (mix(1))

##args and kwargs
def print_args(*args, **kwargs):
	for arg in args:
		print 'Argument: {}'.format(arg)
	for key in kwargs:
		print 'key: {} Value: {}'.format(key, kwargs[key])
		
print_args(1,2,3,name='Krystal',location='Nullspace',powerlevel=9001)

#####
#locals() --> lists all your local variables
#dir() --> directly methods and attributes available

#all

numbers = [1,3,5,9,10]
oddp = lambda x: x % 2 == 1
print(oddp(1))

all_odd = True
for num in numbers:
	if not oddp(num):
		all_odd = False
		break
		
####any
any([True, False, True, True, True])
		
#you can call any on Infinity, but not all on Infinity (which would be endless loop)
#callable: indicates if something is a function or not eg callable(add_two)

#classes
class Point(object):
	x = None
	y = None
	def __init__(self, x, y):
			self.x = x
			self.y = y 
			
p = Point(3, -3)
print(p)
print(p.x)
print(p.y)

#enum --> more efficient than looping through
names = ['Name','Hello','Pancake']
for i, name in enumerate(names):
	print '{} is #{}'.format(name, i)
	
###hash order

##
def point_init(self, x, y):
	self.x = x
	self.y = y
	
class Point:
	x = None
	y = None
	def __init__(self, x, y):
			self.x = x
			self.y = y 
			
Point2 = type('Point2', (), {'x':None, 'y':None, '__init__':point_init})

#####
#vars gives you values
print(vars(p))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#map, filter, reduce
print(map(add_ten, l))

print(filter(oddp, l))

print(reduce (lambda x, y: x + y, l, 0))

##sum((map(add_ten, filster(oddp, l)))
##[add_ten(i) for i in l if oddp(i)]
##sum([add_ten(i) for i in l if oddp(i)])

#dictionary comprehension

for name, score in scores:
	print name, score
	
print({name:key for name, key in scores})

print(dict(scores))

#seed is automatically set in Python
#itertools

#cpickle
#csv
#getpass
#subprocess











			
		
		
		
	






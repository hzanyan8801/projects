"""from random import shuffle
from random import randint

mylist = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist)

print(mylist)


#random number

num = randint(1,1000)

print(num)

#append

mystring = "hello"

mylist = []
for letter in mystring:
    mylist.append(letter)
    print(mylist)

mystring2 = "hello"

mylist2 = [letter for letter in mystring2]

print(mylist2)


mylist3 = [num for num in range(1,10)]
print(mylist3)

mylist4 = [num**2 for num in range(0,10)]
print(mylist4)

mylist5 = [x for x in range(0,11) if x%2==0]
print(mylist5)

celcius = [0,10,20,30,32]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]

print(fahrenheit)

fahrenheit2 = []

for temp in celcius:
    fahrenheit2.append((9/5)*temp +32)
    print(fahrenheit2)

results = [x if x%2==0 else 'OOD' for x in range(0,11)]
print(results)

mylist6 = []

for x in [2,4,6]:
    for y in [1,10,100]:
        mylist6.append(x*y)
        
print(mylist6)"""


mylist7 = [x*y for x in [2,4,6] for y in [1,10,100]]

print(mylist7)

help(mylist7.insert)
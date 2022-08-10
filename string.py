"""
print('This is a string {}'.format('INSERTED'))

print('The {0} {2} {1}'.format('fox', 'brown', 'quick'))

print('The {b} {q} {f}'.format(f='fox', b='brown', q='quick'))

#float formatting follows "{value:width.precision f}"

result = 100/777
print("The result was {r:2.3f}".format(r=result))

"""

name = "Jose"

print('Hello, his name is {}'.format(name))
print(f'Hello, his name is {name}')

name1 = 'SAM'
age = 4
print(f'{name1} is {age} years old.')
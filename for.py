"""
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    #Check for even
    if num % 2 == 0:
        print (num)
    else:
        print(f'Odd number: {num}')


list_sum = 0

for num in mylist:
    list_sum = list_sum + num 

print(list_sum)

mystring = "Hello World!"

for letter in mystring:
    print(letter)




mylist2 = [(1,2),(3,4),(5,6),(7,8)]

#print(len(mylist2))

#for item in mylist2:
 #   print(item)

for a,b in mylist2:
    print(a)
 #   print(b)

 """

d = {"k1":1, 'k2':2, 'k3':3}

#for item in d.items():
 #   print(item)

for key,value in d.items():
    print(value)
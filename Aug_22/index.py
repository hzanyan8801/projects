print(list(range(0,11,2)))

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count +=1


word = 'abcde'

for item in enumerate(word):
    print(item)

mylist1 =[1,2,3]
mylist2 =['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)
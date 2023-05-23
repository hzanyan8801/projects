def lesser_of_two_evens(a,b):

    if a%2 ==0 and b%2 ==0:
        #Both numbers are even!
        return min(a,b)
        #-2result = min(a,b)
       #-1 "if a < b:
        #-1   result = a
       #-1 else: 
       #-1     result = b
    else:
        #One of Both numbers are Odd!
        return max(a,b)
        #-2result = max(a,b)
        #-1  if a > b:
         #-1   result = a
       #-1 else:
       #-1     result = b

    return result


print(lesser_of_two_evens(2,4))
#print(lesser_of_two_evens(7,5))
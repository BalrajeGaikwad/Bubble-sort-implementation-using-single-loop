"""
num = [5,3,8,6,2,7,4,1]
i = 0  
while True:   
    if i < len(num) - 1:
        if num[i] > num[i + 1]: 
            num[i], num[i + 1] = num[i + 1], num[i]
            i = 0 
        else:
            i += 1  
    else:
        break  
print("Sorted array:", num)

"""

num = [5,3,8,6,2,7,4,1]
i = 0  
while True:   
    if i < len(num) - 1:
        if num[i] > num[i + 1]: 
            #num[i], num[i + 1] = num[i + 1], num[i]
            temp=num[i]
            num[i]=num[i + 1]
            num[i + 1]=temp
            i = 0 
        else:
            i += 1  
    else:
        break  
print("Sorted array:", num)



























"""num = [5,3,8,6,2,7,4,1]
i = 0  
while True:  
    #swapped = False  
    if i < len(num) - 1:
        if num[i] > num[i + 1]: 
            num[i], num[i + 1] = num[i + 1], num[i]
      #      swapped = True 
            i = 0 
        else:
            i += 1  
    else:
    #    if not swapped:  
        break  
print("Sorted array:", num)"""
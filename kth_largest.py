import random
import copy

def seperate(l, k):
    
    referance = l[random.randrange(0, len(l))] # l[4]
    
    left_basket = []
    right_basket = []
    
    for i in range(len(l)):
        
        if l[i] <= referance:
            left_basket.append(l[i])
            
        else:
            right_basket.append(l[i])
    
    if len(right_basket) == k-1:
        return [referance], 1
    
    if len(left_basket) < k:
        return right_basket, k
    
    else:
        k = k - len(right_basket)
        return left_basket, k       

def create_list(n):
    l = []
    for i in range(n):
        a = random.randint(1, 100)
        
        while(a in l):
            a = random.randint(1, 100)
        
        l.append(a)
        
    return l
        
        
l = create_list(10)
a = l.copy()
a.sort()

print('unsorted list ', l)
print('Sorted List', a)

k = 4

while(len(l) != 1):
    l, k = seperate(l, k)
    
print('Greatest kth Element is :', l[0])

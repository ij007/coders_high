import random
import copy

def seperate(l, k):
    
    referance = l[0] # l[4]
    
    left_basket = []
    right_basket = []
    
    
    
    for i in range(1, len(l)):
        
        if l[i] < referance:
            left_basket.append(l[i])
            
        else:
            right_basket.append(l[i])
   
    if len(left_basket) == k:
        return [referance], 1
    
    if len(left_basket) > k:
        return left_basket, k
    
    if len(left_basket) < k:
        k = k - (len(left_basket) + 1)
        return right_basket, k
    
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

k = 1
k = len(l) - k

while(len(l) != 1):
    l, k = seperate(l, k)


print('greatest element is', l[0])
    
print('Greatest kth Element is :', l[0])

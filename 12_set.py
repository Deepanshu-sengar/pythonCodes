e = set()   # don't use s = {} to create an empty set as it will create an empty dictionary

s = {1 , 5 , 32, 5 , 5 , "Harry"}  
print(s,type(s))  

s.add(566)
print(s)

print(len(s))

s.remove(1)
print(s)

s.pop()   # it removes a random element from set..
print(s)

# UNION and INTERSECTION
s1={1,2,4,6,7,8}
s2={2,3,5,7,8}
print(s1.union(s2))
print(s1.intersection(s2))

#DIFFERENCE OF SETS
print(s1-s2)     
print(s2-s1)

#SUBSET
print({2,4}.issubset(s1))

s2.pop()
print(s2)

s1.clear()
print(s1)   
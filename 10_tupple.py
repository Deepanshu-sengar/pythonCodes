# tupple is immutable..
a=()   # empty tupple
b=(1,) # having only one element
c= (1) # int 
d=(1,2,3,4,5)
print(type(a),type(b),type(c),type(d))


# methods of tupple.. 

e = (1,45,342,3424,45,False,"Rohan","Shivam")
print(e)
print(len(e))

no = e.count(45)  
print(no)

idx = e.index(45)
print(idx)
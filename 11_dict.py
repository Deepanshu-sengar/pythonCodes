d = {} # empty dict
marks = {
    "Key" : "Value",
    "Harry" : 100 ,
    "Shubham" : 56 ,
    "Rohan" : 23 ,
    67 : "Raman"
    }

print(marks, type(marks))
print(len(marks))
print(marks.items())
print(marks.values())
print(marks.keys())

marks.update({"Harry" : 99})  # dictionary is mutable
print(marks)

print(marks.get("Harry"))  # if key does no exist in the dict then return none
print(marks["Harry"])     # if key does no exist in the dict then return an error

print(marks.get("shruti"))  
# print(marks["shruti"])     # it gives error

print(marks.pop("Harry"))
print(marks)

print(marks.popitem())  # removes and return last key pair..
print(marks)


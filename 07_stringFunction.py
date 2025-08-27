name = "deepanshu"

print(len(name)) # it gives lenght of string
print(name.endswith("sh"))  # return false 
print(name.endswith("shu"))  # return true

print(name.startswith("d"))  # return true
print(name.startswith("D"))  # return false  (case sensitive)

print(name.capitalize())  # capitalize only first char

print(name.find("deepanshu"))  # it finds the word and return starting idx 

print(name.replace("deepanshu","sengar")) 

print(name.count("e")) # it returns the no of occurance of char in string 

print(f"Good Morning {name}")


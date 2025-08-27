# slice 

name = "Deepanshusengar"  
firstName = name[0:9]  # start from index 0 to 9 (excluding 9)
print(firstName)
secondName = name[-6:] # negative indices start from -1 from end of string
print(secondName)

name1 = "ABESEngineeringCollege"
print(name1[0:4])
print(name1[:4])  # is same as print(name1[0:4])
print(name1[1:4])
print(name1[4:])  
print(name1[-7:])  

# slicing with skin value
word = "amazing"
print(word[0:7:3])  # [starting_idx : end_idx (excluded) : jump]


a = {
    "harry": 100,
    "anil" : 56, 
    "Rohan" : 23,
    "list" : [1,2,9]

}

print(a.keys()) #gives a list containing dictionary's keys. // left side data 
print(a.items())#gives all the key values in the form of tupples
a.update({"harry":99})#updates the dictionary , if we add a string that is not present then that will also get added 
print(a.values())#gives value of the right side of the dictionary 
print(a.get("harry"))#returns the value of the right side of dictionary
#it is gives none as output if the name is not present in the dictionary whereas any other will return an error 
 
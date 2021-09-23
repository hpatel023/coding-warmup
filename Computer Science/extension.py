from random import randint

names = input("Input a list of sumaes (seperate by commas and spaces): ")
name = names.split(', ')
value1 = randint(1,len(name) - 1)
value2 = randint(1,len(name) - 1)
print(value1)
print(value2)
newlist = name[value1] + ', ' + name[value2]
print(newlist)

print(name)

#Defitions to know 
#preconditions what mush be ture for inputs or paramets 
#postconditions what is the state of program when it is done
#stage 1 
'''
tinput =  input("enter a three digit integer: ")

tlist =  list(tinput) 

tadd = int(tlist[0]) + int(tlist[1]) + int(tlist[2])

print(tadd)
'''
#stage 2 
tadd = 0

tinput = input("enter an integer: ")

tlist = list(tinput)

for i in range(len(tlist)):
    tadd = tadd + int(tlist[i])

print(tadd)
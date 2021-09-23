''''
numbers = [1, 2, 3, 4, 5, 6]

sum = 0 

evensum = 0 

for i  in numbers:
    sum = sum + i
    if i % 2 == 0:
        evensum = evensum + i

print(sum)
print(evensum)
'''
### Input.py

newList = []

n = int(input('Enter an integer: '))

for i in range (n): 
    s = input("Enter a String: ")
    newList.append(s)

newList = sorted(newList)

print(newList)
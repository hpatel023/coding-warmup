''''
import math

x1 = input("Please input the first x value: ")
x2 = input("Please input the second x value: ")
y1 = input("Please input the first y value: ")
y2 = input("Please input the second y value: ")

v =  math.sqrt( ((y1-y2)**2)+((x1-x2)**2) )

print(v)
'''
'''
import math

p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)
'''

import math 

x1=int(input('What is the value of x1?: '))
x2=int(input('What is the value of x2?: '))
y1=int(input('What is the value of y1?: '))
y2=int(input('What is the value of y2?: '))

radius = math.sqrt((y2-y1)**2+(x2-x1)**2)
result = 3.14159*(radius**2)
result = round(result,3)

print (result)
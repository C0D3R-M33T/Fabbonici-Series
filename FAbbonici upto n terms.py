#Fabbonici Series
print ("Fabbonici Series")
#Inputting limit of Fabbonici from the user
num1 = int (input ("Enter the limit upto you want to print Fabbonici series:- "))
#Printing the Fabonicci Series as per the Limit inputted by the user
first  = 0
second = 1
print (first)
print (second)
for i in range (1,num1+1):
    third = first + second
    print (third)
    first, second = second, third
print ("Fabbonici Series upto 10 :--->")
first = 0
second = 1
print (first)
print (second)
for i in range (1,6):
    third = first + second
    print (third)
    first, second = second, third
    















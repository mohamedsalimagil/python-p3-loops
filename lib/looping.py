#!/usr/bin/env python3

def happy_new_year():
    n = 10
    while n > 0:
        print(n)
        n -= 1
    print("Happy New Year!")
happy_new_year()
        

def square_integers(int_list):
    return [x**2 for x in int_list]
print(square_integers([1, 2, 3, 4, 5]))


 
    
    

def fizzbuzz():
    for i in range(1, 101):
     if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
     elif i % 3 == 0:
        print("Fizz")
     elif i % 5 == 0:
        print ("Buzz")
     else:
        print(i)
fizzbuzz()    

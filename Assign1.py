#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program
x = 0
for i in range(5):
    y = float(input("Please enter your number> "))
    x = x + y
    if i >= 4:
        z = x / 5
        print(f"The sum of the 5 numbers is {x} and the average is {z}")
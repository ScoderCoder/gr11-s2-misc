#!/usr/bin/python

# My First Python Program
# By Mr. Klimowski
# September 11, 2021

counter = 0   #initialize the variable counter as 0

#the following line of code does the following:
#creates a variable called firstName
#prompts the user
#gets input from the keyboard - all in just one line...amazing
firstName = input("Please enter your first name: ")
age = input("Please enter your age: ")

#start of a while loop
while counter < 10: #repeat as long as counter is less than 5
    print (f"NAME: {firstName}, AGE: {age}") #display the firstName
    counter = counter + 1 #add one to the variable counter

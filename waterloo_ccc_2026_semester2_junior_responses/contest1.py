#!/usr/bin/python

# 18/02/2025

# bea wants 
b = int(input())

# tickets available
t = int(input())

# tickets other people purchased
p = int(input())

if b < 0:
    print(f"Error, integer b is negative.")
    quit()
if p > t:
    print("Error, P cannot be greater than T.")
    quit()

tfb = t - p

if tfb >= b:
    print(f"Y {tfb - b}")
else:
    print("N")

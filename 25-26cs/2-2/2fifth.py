#!/usr/bin/python

# 06/02/2026
# Sougato

# SINGLE PRINT
print("PRINTED")

print("  /\\\n //\\\\\n///\\\\\\\n\n")

# Loop
print("LOOPED")

count = 3 # HOW MANY ROWS?

for i in range(1, 1 + count):
    if i < count: # THIS IS TO CENTRE THE LAYERS THAT AREN'T THE BOTTOM, BY ADDING SPACES
        print(" " * (count - i) + "/" * i + "\\" * i)
    else:
        print("/" * i + "\\" * i)


import random as r
names, feelings = ["Sougato", "Jonah", "Kiran", "Aubai", "Yuvaansh"], ["loves", "hates", "wants to kiss", "wants to kick", "despises seeing"]
for i in names: print(i, feelings[r.randint(0, len(names) - 1)], names[r.randint(0, len(names) - 1)])


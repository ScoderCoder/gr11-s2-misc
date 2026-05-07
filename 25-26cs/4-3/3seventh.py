word = input("Enter a word: ")
wordlist = list(word)

for i in range(0, len(wordlist)):
    print(word)
    wordlist.append(wordlist[0])
    wordlist.pop(0)
    word = "".join(wordlist)

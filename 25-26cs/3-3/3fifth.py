location = input("Please enter the country you are mailing your letter to: ")

canada = "0.85"
usa = "1.20"
international = "2.50"

if location == "Canada":
    print(f"Your postage will cost ${canada}.")
elif location == "America" or location == "United States of America":
    print(f"Your postage will cost ${usa}.")
elif location == "International":
    print(f"Your postage will cost ${international}.")
else:
    print("Your input was invalid, please enter one of the following:\n'America', 'Canada', 'International'")
    

# Madlibz
# This is a program that engages the user with a short prose and is required to fill in the placeholders according to their desire


# This is a short prose
proseString = """
Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME
"""
# newProseString = proseString # assigns the prose string to a new variable

# userInput = input("Please provide an example of an occupation.")
# newProseString = newProseString.replace("OCCUPATION", userInput)# prompts the user to input their occupation
# #  the rest are quite straight forward but incase you want some elaboration hit my github page I will get back to you
# userInput = input("Please provide a country.")
# newProseString = newProseString.replace("COUNTRY", userInput)

# userInput = input("Please provide a plural noun.")
# newProseString = newProseString.replace("PLURAL_NOUN", userInput)

# userInput = input("Please provide  a verb.")
# newProseString = newProseString.replace("VERB", userInput)

# userInput = input("Please provide an objective.")
# newProseString = newProseString.replace("OBJECTIVE", userInput)

# userInput = input("Please provide an example of a personal item.")
# newProseString = newProseString.replace("PERSONAL_ITEM", userInput)

# userInput = input("Please provide a holiday.")
# newProseString = newProseString.replace("HOLIDAY", userInput)

# userInput = input("What's is your name?.")
# newProseString = newProseString.replace("NAME", userInput)

# print(newProseString)

#This program was ment to teach me about iteration. 
#It might not be the best way to go around this problem but I chose to use it to learn.
# As iteration is about refinement I am not stopping at this for I need to find a solution
# to work with larger pieces of data and more iterations but this is the end of this scope for now.

replacements = [
    ["An occupation", "OCCUPATION"],
    ["A country", "COUNTRY"],
    ["A plural noun", "PLURAL_NOUN"],
    ["A verb, like 'run,' 'eat' or 'think'", "VERB"],
    ["An adjectiv, like 'friendly,' 'long,' or 'warm'", "ADJECTIVE"],
    ["A title that someone might have in an organization, like 'manager,' 'captain,' or 'trainer'", 'TITLE'],
    ["A personal item"," PERSONAL_ITEM"],
    ["A holiday, like Christmas or Labor Day", "HOLIDAY"],
    ["Your name", "NAME"]
]

for prompt,placeHolder in replacements:
    userInput = input(prompt)

    proseString = proseString.replace(placeHolder,userInput)
    
print(proseString)
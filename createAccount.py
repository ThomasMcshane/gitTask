'''
Prog: createAccount.py
Name: Jodie, Allen, Elyse, and Denny
Date: 2018-01-29
Desc: This program handles the creation of new user accounts on the dating app. Users will complete a user profile to help them match with others.
'''

# Initialise list of users.
users = []

# User must choose a username.
username=input("Choose a user name: ")

# If the username is taken, ask for a different one.
while username in users:
    print("That username is already taken!")
    username=input("Choose a different user name: ")
users = users.append(username)

# User must choose a password.
password = input("Set a password: ")

# If the user's password isn't long enough, ask them to choose a different one.
while len(password) < 8:
    print("Password must be at least 8 characters!")
    password = input("Set a longer password: ")

# Here, the user indicates his/her species and gender.
userSpecies = input("Please enter your species: ")
userGender = input("Please enter your gender: ")

# Initialise user's list of interests (animal species and gender).
userInterests = []

# Instruct user on how to answer yes/no questions.
print("Please answer each of the following questions with y or n so we can narrow the options to your interests.")

# This series of questions allows users to indicate interest in different species. Choices are added to their list of interests.
speciesList = ["dogs", "cats", "birds", "fish", "bunnies", "other species"]
for s in speciesList:
    interest = input("Are you interested in meeting " + s + "? ")
    if interest and interest[0].lower() == "y":
        userInterests.append(s)

# This series of questions allows users to indicate interest in different genders. Choices are added to their list of interests.
genderList = ["good girls", "good boys", "any gender"]
for g in genderList:
    interest = input("Are you interested in meeting " + g + "? ")
    if interest and interest[0].lower() == "y":
        userInterests.append(g)

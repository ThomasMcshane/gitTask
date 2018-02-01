'''
Prog: createAccount.py
Name: Jodie, Allen, Elyse, and Denny
Date: 2018-01-29
Desc: This program handles the creation of new user accounts on the dating app. Users will complete a user profile to help them match with others.
'''
#initialises list of users.
users = []

#User must choose a username
username=input("Choose a user name: ")

#If the username is taken, asks for a different one.
while username in users:
    print("That username is already taken!")
    username=input("Choose a different user name: ")
users = users.append(username)

#user must choose a password.
password = input("Set a password: ")

#If the user's password isn't long enough, this will ask them to choose a different one.
while len(password) <= 8:
    print("Password must be at least 8 characters!")
    password = input("Set a longer password: ")

#Here, the user indicates his/her species and gender
userSpecies = input("Please enter your species.")
userGender = input("Please enter your gender.")

#initialise user's list of interests (animal species and gender)
userInterests = []

#Instructs users on how to answer yes/no questions.
print ("Please answer each of the following questions with y or n so we can narrow the options to your interests.")

#This series of questions allows users to indicate interest in different species. Choices are added to their list of interests.
speciesList = ["dogs", "cats", "birds", "fish", "bunnies", "other species"]
for s in speciesList:
    interest = input("Are you interested in meeting " + s + "?")
    if interest = "y":
        userInterest.append(s)

#This series of questions allows users to indicate interest in different genders. Choices are added to their list of interests.
genderList = ["good girls", "good boys", "any gender"]
for g in genderList:
    interest = input("Are you interested in meeting " + g + "?")
    if interest = "y":
        userInterest.append(g)

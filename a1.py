#The following program is a Party List Assistant designed to not only help you stay organized when planning your next big event
#but most importantly, helps keep track of the allergies of your invitees to help you make better catering decisions. The perfect tool
#for bakers, chefs, or stressed out party planners!
invitees = [] #global variable 
def addToInviteList(friendName, allergies):
    isAlreadyInvited = False     
    for invited in invitees:
        if friendName == invited["Name"]: #checks if named invitee is already on the list.
            print('Looks like', friendName, 'is already on the list!')
            isAlreadyInvited = True #boolean variable to keep track of who is and isnt already on the list
    if not isAlreadyInvited: #if the named invitee is not on the list, they will be added. 
        invitees.append({"Name": friendName, "Allergies": allergies})
    
def removeFromInviteList(friendName):
        for invited in invitees: #iterates through dictionary
            if friendName == invited["Name"]: #compares given name to names in the list
                invitees.remove(invited) #removes the friend from the invitees
                print(friendToRemove, 'has been removed from the Party List sucessfully!\n ')

def allergicTo(food):
    allergicFriends = [] #an empty list is created to store all the friends allergic to specific allergen
    for friend in invitees: #iterates through the invitees 
        friendAllergies = friend["Allergies"] #creates a list of all allergies of all invitees
        for allergy in friendAllergies: #iterates through this list 
            if allergy == food: #if the food allergen mentioned happens to be in the list of all allergies
                allergicFriends.append(friend["Name"]) #the names of all invitees with this allergy is added to a new list for that particular allergy
    if len(allergicFriends) == 0:
        print('Looks like no one is allergic to', food, '!')
    return allergicFriends

if __name__ == '__main__': 
    print("Welcome to your Virtual Party List Assistant!\n")
    while True: #continuously shows options menu to user until user chooses to quit. 
        action = int(input("What Would You Like To Do?\n1. Add an Invitee to the List\n2. Uninvite an Invitee\n3. View Invitees\n4. Check Allergies\n5. Quit\nEnter your Choice: "))
        if action == 1:
            friendToAdd = input("Please enter the Full Name of Invitee: ")
            print('Does', friendToAdd, 'have any allergies?\n1. Yes\n2. No\nEnter your Choice: ')
            choice = int(input())
            while choice != 1 and choice != 2:
                choice = int(input('Please enter a valid option: ')) #continues to ask user for a valid input 
            if choice == 1:
                FriendAllergies = input('Please Enter All Allergies for Invitee, separated by a COMMA AND a SPACE: ') #food allergies are noted in a string
                allergyList = FriendAllergies.split(', ') #a new list is created with all the allergies as elements of the list
                addToInviteList(friendToAdd, allergyList) #invitee is added 
            else:
                addToInviteList(friendToAdd, []) #invitee is added with out allergy 
            print(friendToAdd, 'has been added to the list!\n')
        elif action == 2: 
                if len(invitees) == 0:
                    print('\nOops! Seems like there is no one on the Party List! Try adding a friend!\n') #informs user that the party list is empty
                else:
                    print(invitees)
                    friendToRemove = input("\nPlease Provide the Name of the Invitee you Wish to Remove: ")
                    removeFromInviteList(friendToRemove) #removes friend from list using function
        elif  action == 3:
            print(invitees)
        elif action == 4:
                allergy = input('What Allergy are you Searching for?\n')
                print(allergicTo(allergy)) #searches for allergies in list using function
        elif action == 5:
            print("Thanks for using the Virtual Party List Assistance App!") 
            exit() #quits the program
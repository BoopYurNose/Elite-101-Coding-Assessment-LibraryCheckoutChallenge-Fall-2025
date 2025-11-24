import libraryBooksList as libraryBooksList
from datetime import date, timedelta



# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

# PSEUDO Code
''''
I will define a list in this script to equal to the LibraryBookList in the module script
I would define a simple function that doesn't take any arguements
inside this function I will run a for loop that will iterate through each dictionary in the table
in each iteration of this for loop I will index the string key "available" which will reference the fourth index in each dictionary 
which is referencing to the Available Bolean value
if it is equal to true I will print the book values in the dictionaries and only include the book ID, title, and author
'''
LibraryList = libraryBooksList.libraryBooksList
#PLEASE UNCOMMENT THIS BEFORE YOU SUBMIT IT ZACHARY 

# sorry I'm a dumbass (⩾﹏⩽)
def BookAvailabilityCheck():
    for Dictionaries in LibraryList:
        if Dictionaries["available"] == True:
            print(Dictionaries["id"], Dictionaries["title"], Dictionaries["author"])

BookAvailabilityCheck()




# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

'''old code (it's funny how much I over complicated this. I could've literally just used SubString Search..)

def SearchBook(UserSearch):
    for Dictionaries in LibraryList:
        if UserSearch == Dictionaries["title"]: #Checking if the user entered the full name in
            print(f"{Dictionaries["title"]} We found this relating to your search of: {UserSearch}")
        for TitleCharacters in Dictionaries["title"]: #Checking if the user entered in characters relating to the book title like a single character in the title
            if UserSearch == TitleCharacters: # issue here is that it only searches by single character I guess I'll add another if statement but I know
                print(f"{Dictionaries["title"]} We found this relating to your search of: {UserSearch}") #There is a better way to code this I'll do more research and learn more          

UserInput = input("\nType in a search term to search for a book:")
SearchBook(UserInput)

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

PSEUDO Code (second version)
1. I created a function that takes in a arguement that being the UserInput Variable
2. for now I put a pass in the function as I created the UserInput input variable that allows you to input a value
3. I called the function passing the UserInput variable into it
4. I removed the pass that is nested inside the SearchBook function and got to work on the function. First I made the UserSearch variable all lowercase characters so it doesn't matter if a character has lower
or upper case it will still find it if it's the same character
5. I made a for loop that iterates thru each dictionary in the LibraryList List
6. in this for loop I run a if statement that uses SubString Search the (in) keyword that checks if UserSearch is equal to any of the characters in the title string key author string key and genre string key
7. if it is I will print the dictionaries title, genre, and author 
'''

def SearchBook(UserSearch):
    UserSearch = UserSearch.lower()

    for Dictionaries in LibraryList:
        if UserSearch in Dictionaries["title"].lower() or UserSearch in Dictionaries["author"].lower() or UserSearch in Dictionaries["genre"].lower():
            print(f"These are the results for titles: {Dictionaries["title"]}")
            print(f"These are all the results for genre: {Dictionaries["genre"]}")            
            print(f"These are all the results for author: {Dictionaries["author"]}")

UserInput = input("\nSearch for a book by it's title, author name, or genre: ")
SearchBook(UserInput)

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out




CurrentDate = date.today()

def UserCheckout(IdInput):

    for DictionaryValue in LibraryList:
        if IdInput.lower() == DictionaryValue["id"].lower():
            if DictionaryValue["available"]:
                print(f"{DictionaryValue["id"]} is available for checkout \n")

                DictionaryValue["due_date"] = CurrentDate + timedelta(days=14)
                print(f"{DictionaryValue["title"]} is due on {DictionaryValue["due_date"]} \n")

                DictionaryValue["available"] = False
                print(f"{DictionaryValue["id"]} has been checked out and it is {DictionaryValue["available"]} not available for checkout anymore")
                return
            else:
                print(f"{DictionaryValue["id"]} is not available for checkout sorry")
                return
    
    print("Sorry no id's found with that search")
    return




UserIDInput = input("Type in a id to checkout a book: ")
UserCheckout(UserIDInput)


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def ReturnBookID(UserID):

    for DictionaryValues in LibraryList:
        if UserID.lower() == DictionaryValues["id"].lower():
            if DictionaryValues["available"] == False:
                print(f"Thank you for returning {DictionaryValues["title"]} to the library (⩾﹏⩽)")
                DictionaryValues["available"] = True
                DictionaryValues["due_date"] = None

                #print(DictionaryValues["available"])
                #print(DictionaryValues["due_date"])
                return 
            
            
            print("This book is already returned")
            return        


UserReturnInput = input("Type the id of the book you'd like to return:")
ReturnBookID(UserReturnInput)

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
''' WORK IN PROGRESS
def DisplayAllOverDue():
    for Dictionaries in LibraryList:
        if Dictionaries["available"] == False:

            DueDates = CurrentDate.strptime(CurrentDate, "%d-%b-%y").date()
            if DueDates > CurrentDate:
                print(f"These are all the books that are overdue. \n {Dictionaries["title"]}")

DisplayAllOverDue()
            

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

#if __name__ == "__main__":
    # You can use this space to test your functions
#    pass
'''
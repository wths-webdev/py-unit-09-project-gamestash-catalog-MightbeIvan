games = {
    "GTA V": 2013,
    "Ratchet & Clank": 2021,
    "Spider-Man: Miles Morales": 2020,
    "God of War Ragnarok": 2022,
    "The Legend of Zelda: Tears of the Kingdom": 2023,
    "Super Mario Odyssey": 2017,
    "Princess Peach": 2024,
    "Mario Kart 8 Deluxe": 2017
}

# get_inventory_count(): Returns how many total games there are in a readable format.
def count_inv():
    print("There is currently ", len(games), "games in your inventory")    

# add_game(title, year): Adds a game to the inventory.
def addgame(title, year):
    games.update({title : year})

def display_inv():
             # function 2:
        count = 1
        for game in games:                         
            # for key in games, games[key] returns the value
            print(f"   {str(count)}. {game} by {games[game]}")
            count += 1
        print()

# remove_game(title): Removes a game from the inventory.
def RemoveGame(game):
    games.pop (game)


# display_inventory()
def display_inventory(inventory):
    print()

# search_year(year)
def search_year(year):

    year = int(input("What year would you like to search for?"))

    print(f"All games from {year}:")
    for game in games:
            if games[game] == year:
                print(f"   {game}")

def search_title(title):
    title = input("Which title would you like to search for? ")

# search_title(title)
def SearchYear(year):
    year=int(input("What year was the book released?"))

    print("All  the games from", year)

    for game in games:
        if games[game] == year:
            print ( f" {game}")
    


# Welcome message
print("\nWelcome to...")
print(" _____________________________  \n"
    "/        _____________        \\\n"
    "| == .  |             |     o |\n"
    "|   _   |             |    B  |\n"
    "|  / \\  |   Game      | A   O |\n"
    "| | O | |      Stash  |  O    |\n"
    "|  \\_/  |             |       |\n"
    "|  :::  |_____________| . . . |\n"
    "\\_____________________________/")

while True:
    # Display menu to user
    print()
    print("----------- Menu ----------")
    print("Add game (add)")
    print("Remove game (remove)")
    print("Show inventory (show)")
    print("Search by year (year)")
    print("Search for a title (title)")
    print("Quit (q)\n")
    user_selection = input("What would you like to do? ").lower()



    # Use conditional statements to call functions based on user input
    if user_selection == "add":
       addgame()
        # update() will add to the dictionary if the key does not exist
       
    elif user_selection == "remove":
        RemoveGame()

    
    elif user_selection == "show":
        count_inv()
        display_inv()



    elif user_selection == "year":
        search_year()

    elif user_selection == "title":
        search_title()

    elif user_selection == "q":
        print("Bye bye!")
        break # out of the loop

    else:
        print("Error: That was not an option.\n")

print("")
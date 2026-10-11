
"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Set the player's starting room.
current_room = "Great Hall"

# Continue the game until the player exits.
while current_room != "exit":
    # Display the player's current room.
    print(f"\nYou are in the {current_room}.")

    # Ask the player to enter a direction or exit.
    command = input(
        "Enter a direction (north, south, east, west) or 'exit': "
    ).strip().lower()

    # Check whether the player wants to exit.
    if command == "exit":
        current_room = "exit"
        print("Thanks for playing!")

    # Check whether the direction is valid for the current room.
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]

    # Handle directions that are unavailable from this room.
    elif command in ["north", "south", "east", "west"]:
        print("You can't go that way from here. Try another direction.")

    # Handle any other invalid command.
    else:
        print("Invalid command. Enter north, south, east, west, or exit.")

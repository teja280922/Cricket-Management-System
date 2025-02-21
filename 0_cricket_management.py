matches = {}

def display_menu():
    print("\nCricket Match Management")
    print("1. View all matches")
    print("2. Add a match")
    print("3. Update a match")
    print("4. Delete a match")
    print("5. Exit")

def view_matches():
    if not matches:
        print("No matches available.")
    else:
        print("\nList of Matches:")
        for date, match in matches.items():
            print(f"{date}: {match}")

def add_match():
    date = input("Enter the match date (YYYY-MM-DD): ")
    if date in matches:
        print(f"Warning: A match already exists on {date}. Details: {matches[date]}")
        return
    match = input("Enter match details (e.g., Team A vs Team B): ")
    matches[date] = match
    print("Match added successfully!")

def update_match():
    view_matches()
    if matches:
        date = input("Enter the date of the match to update (YYYY-MM-DD): ")
        if date in matches:
            new_details = input("Enter updated match details: ")
            matches[date] = new_details
            print("Match updated successfully!")
        else:
            print(f"No match found on {date}.")

def delete_match():
    view_matches()
    if matches:
        date = input("Enter the date of the match to delete (YYYY-MM-DD): ")
        if date in matches:
            removed_match = matches.pop(date)
            print(f"Match on {date} ('{removed_match}') deleted successfully!")
        else:
            print(f"No match found on {date}.")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        view_matches()
    elif choice == '2':
        add_match()
    elif choice == '3':
        update_match()
    elif choice == '4':
        delete_match()
    elif choice == '5':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please choose between 1-5.")

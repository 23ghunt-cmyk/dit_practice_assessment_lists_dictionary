# Function to ensure user input is a valid integer
def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a integer.")

# Determine NCEA results based on credits
def calculate_status(s):
    total = s["a"] + s["m"] + s["e"]
    passed = total >= 80
    
    endorsement = "None"
    if s["e"] >= 50:
        endorsement = "Excellence"
    elif (s["m"] + s["e"]) >= 50:
        endorsement = "Merit"
        
    return total, passed, endorsement

# Initial list of student dictionaries (Database)
students = [
    {"name": "Aria Thompson", "year": 11, "a": 40, "m": 25, "e": 20},
    {"name": "Ben Turoa", "year": 12, "a": 30, "m": 10, "e": 55},
    {"name": "Chloe Smith", "year": 13, "a": 50, "m": 15, "e": 5},
    {"name": "David Ngata", "year": 11, "a": 20, "m": 45, "e": 25},
    {"name": "Elena Rodriguez", "year": 12, "a": 10, "m": 10, "e": 10},
    {"name": "Finn O'Connor", "year": 13, "a": 35, "m": 35, "e": 15},
    {"name": "Grace Lee", "year": 11, "a": 40, "m": 40, "e": 5},
    {"name": "Hemi Walker", "year": 12, "a": 25, "m": 10, "e": 50},
    {"name": "Isabella Chen", "year": 13, "a": 60, "m": 15, "e": 10},
    {"name": "Jack Wilson", "year": 11, "a": 30, "m": 20, "e": 5},
    {"name": "Kaia Williams", "year": 12, "a": 15, "m": 25, "e": 45},
    {"name": "Liam Taylor", "year": 13, "a": 45, "m": 30, "e": 10},
    {"name": "Mia Anderson", "year": 11, "a": 20, "m": 55, "e": 5},
    {"name": "Noah Brown", "year": 12, "a": 50, "m": 5, "e": 2},
    {"name": "Olivia Moore", "year": 13, "a": 10, "m": 10, "e": 70},
    {"name": "Priya Patel", "year": 11, "a": 40, "m": 30, "e": 10},
    {"name": "Quinn Davis", "year": 12, "a": 35, "m": 15, "e": 35},
    {"name": "Riley Jones", "year": 13, "a": 20, "m": 20, "e": 20},
    {"name": "Sophie Martin", "year": 11, "a": 10, "m": 40, "e": 40},
    {"name": "Thomas White", "year": 12, "a": 85, "m": 0, "e": 0}
]

# Main Program Loop
while True:
    print("NCEA Student Management Menu")
    print("1. Add New Student")
    print("2. Add Credits to Existing Student")
    print("3. Show All Student Data")
    print("4. Show Students who have Passed (80+ credits)")
    print("5. Show Endorsements (50+ M/E credits)")
    print("6. Filter by Year Level")
    print("7. Exit")
    
    choice = input("\nSelect an option (1-8)\n> ").lower()

# OPTION 1: CREATE
    if choice == "1":
        name = input("Name\n> ")
        while True:
            year = get_int("Year Level\n> ")
            if year < 9 or year > 13:
                print("Please enter a valid year level")
            else:
                break
        a = get_int("Achieved credits\n> ")
        m = get_int("Merit credits\n> ")
        e = get_int("Excellence credits\n> ")

        students.append({"name": name, "year": year, "a": a, "m": m, "e": e})
        print(f"Added {name} successfully.")

# OPTION 2: UPDATE
    elif choice == "2":
        name = input("Enter student name to update\n> ")
        for s in students:
            if s["name"].lower() == name.lower():
                s["a"] += get_int("Add Achieved: ")
                s["m"] += get_int("Add Merit: ")
                s["e"] += get_int("Add Excellence: ")
                print("Credits updated.")
                break
        else:
            print("Student not found.")

# OPTION 3: PRINT ALL
    elif choice == "3":
        print("\n--- All Student Data ---")
        for s in students:
            total, _, _ = calculate_status(s)
            print(f"{s['name']} (Year {s['year']}): {total} total credits (A:{s['a']} M:{s['m']} E:{s['e']})")

# OPTION 4: READ FILTERED (PASS/FAIL)
    elif choice == "4":
        print("\n--- Students Passed (80+ Credits) ---")
        for s in students:
            total, passed, _ = calculate_status(s)
            if passed:
                print(f"{s['name']} - {total} credits")

# OPTION 5: READ FILTERED (ENDORSEMENTS)
    elif choice == "5":
        print("\n--- Endorsement List ---")
        for s in students:
            _, _, endor = calculate_status(s)
            if endor != "None":
                print(f"{s['name']}: {endor} Endorsement")

# OPTION 6: READ FILTERED (YEAR LEVEL)
    elif choice == "6":
        while True:
            yr = get_int("Enter Year Level to filter\n> ")
            if yr < 9 or yr > 13:
                print("Please enter a valid year level")
            else:
                break
        for s in students:
            if s["year"] == yr:
                print(f"{s['name']} (Year {yr})")

# OPTION 7: EXIT
    elif choice == "7":
        print("Program stopped")
        break
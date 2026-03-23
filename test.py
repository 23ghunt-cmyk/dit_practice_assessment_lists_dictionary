import json

def calculate_status(s):
    """Returns a tuple of (Total Credits, Achievement Status, Endorsement)."""
    total = s['a'] + s['m'] + s['e']
    passed = total >= 80
    
    endorsement = "None"
    if s['e'] >= 50:
        endorsement = "Excellence"
    elif (s['m'] + s['e']) >= 50:
        endorsement = "Merit"
        
    return total, passed, endorsement

students = []

while True:
    print("\n--- NCEA Student Management Menu ---")
    print("1. Add New Student")
    print("2. Add Credits to Existing Student")
    print("3. Show All Student Data")
    print("4. Show Students who have Passed (80+ credits)")
    print("5. Show Endorsements (50+ M/E credits)")
    print("6. Filter by Year Level")
    print("7. Export Student to Text File")
    print("8. Exit")
    
    choice = input("\nSelect an option (1-8): ")

    if choice == '1':
        name = input("Name: ")
        year = input("Year Level: ")
        a = int(input("Achieved credits: "))
        m = int(input("Merit credits: "))
        e = int(input("Excellence credits: "))
        students.append({"name": name, "year": year, "a": a, "m": m, "e": e})
        print(f"Added {name} successfully.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        for s in students:
            if s['name'].lower() == name.lower():
                s['a'] += int(input("Add Achieved: "))
                s['m'] += int(input("Add Merit: "))
                s['e'] += int(input("Add Excellence: "))
                print("Credits updated.")
                break
        else:
            print("Student not found.")

    elif choice == '3':
        print("\n--- All Student Data ---")
        for s in students:
            total, _, _ = calculate_status(s)
            print(f"{s['name']} (Year {s['year']}): {total} total credits (A:{s['a']} M:{s['m']} E:{s['e']})")

    elif choice == '4':
        print("\n--- Students Passed (80+ Credits) ---")
        for s in students:
            total, passed, _ = calculate_status(s)
            if passed:
                print(f"{s['name']} - {total} credits")

    elif choice == '5':
        print("\n--- Endorsement List ---")
        for s in students:
            _, _, endor = calculate_status(s)
            if endor != "None":
                print(f"{s['name']}: {endor} Endorsement")

    elif choice == '6':
        yr = input("Enter Year Level to filter: ")
        for s in students:
            if s['year'] == yr:
                print(f"{s['name']} (Year {yr})")

    elif choice == '7':
        name = input("Enter name to export: ")
        for s in students:
            if s['name'].lower() == name.lower():
                total, passed, endor = calculate_status(s)
                filename = f"{s['name']}_report.txt"
                with open(filename, "w") as f:
                    f.write(f"NCEA Report for {s['name']}\n")
                    f.write(f"Year Level: {s['year']}\n")
                    f.write(f"Credits: A:{s['a']}, M:{s['m']}, E:{s['e']}\n")
                    f.write(f"Total: {total}\n")
                    f.write(f"Endorsement: {endor}\n")
                print(f"Exported to {filename}")

    elif choice == '8':
        print("Goodbye!")
        break
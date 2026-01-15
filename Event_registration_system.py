registrations = []

def register_event():
    name = input("Enter participant name: ")
    event = input("Enter event name: ")
    registrations.append({"name": name, "event": event})
    print("Registration successful")

def view_registrations():
    if not registrations:
        print("No registrations found")
    else:
        for reg in registrations:
            print(reg["name"], "- Event:", reg["event"])

def main():
    while True:
        print("1. Register for Event")
        print("2. View Registrations")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_event()
        elif choice == "2":
            view_registrations()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()

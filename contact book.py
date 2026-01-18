contact = {}

while True:
    print("\nContact Book")
    print("1 Add Contact")
    print("2 View Contact")
    print("3 Delete Contact")
    print("4 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact[name] = phone
        print("Contact added")

    elif ch == "2":
        if len(contact) == 0:
            print("No contact")
        else:
            for name in contact:
                print(name, ":", contact[name])

    elif ch == "3":
        name = input("Enter name to delete: ")
        if name in contact:
            del contact[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif ch == "4":
        print("Exit")
        break

    else:
        print("Wrong choice")
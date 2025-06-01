def menu():
    print("Welcome to the Home Menu!")
    print("1. View Profile")
    print("2. Settings")
    print("3. Logout")
    
    choice = input("Please select an option (1-3): ")
    
    if choice == '1':
        view_profile()
    elif choice == '2':
        settings()
    elif choice == '3':
        logout()
    else:
        print("Invalid choice, please try again.")
        menu()

print("ABC")

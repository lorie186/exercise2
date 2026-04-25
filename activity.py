try:
    username = input("Enter Username: ")
    age = int(input("Enter Age: "))

    with open("users.txt", "a") as file:
        file.write(f"{username} - {age}\n")

    print("\nDisplaying all saved users:")
    with open("users.txt", "r") as file:
        print(file.read())

except ValueError:
    print("Error: Invalid input. Please enter a number for Age.")

finally:
    print("System complete.")
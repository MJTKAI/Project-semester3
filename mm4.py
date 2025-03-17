try:
    age = int(input("Please enter your age: "))
    if age <= 19:
        print("You qualify for student discounts.")
    elif 20 <= age <= 54:
        print("You qualify for no age discounts.")
    else:
        print("You can receive senior discounts.")
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")

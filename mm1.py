try:
    num = float(input("Please enter a number: "))
    print(num * 2)
except ValueError:
    print("Invalid input. Please enter a valid number.")

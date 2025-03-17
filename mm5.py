def factorial_while(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


try:
    num = int(input("Enter a number to calculate its factorial: "))
    print(factorial_while(num))
except ValueError:
    print("Invalid input. Please enter a valid integer.")

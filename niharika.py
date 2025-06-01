num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
result = num1 / num2
print(f"The result of the division is: {result}")
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a valid denominator.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result of the division is: {result}")
finally:
    print("Thank you for using the division calculator!")

try:
    num1 = int(input("Enter First number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)

except (ValueError, ZeroDivisionError):
    print("You have entered incorrect input.")

finally:
    print("Thanks!!!")

print("Voting system Allowed or not allowed")
def voter (age):
    if age < 18:
        raise ValueError("Invalid voter")
    return "You are allowed to vote"

try:
    print(voter(19))
except ValueError as e:
    print(e)
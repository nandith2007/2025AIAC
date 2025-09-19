
def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.
    Returns an error message for negative inputs.

    Example:
    Input: 5
    Output: 120
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(factorial(num))
    except ValueError:
        print("Please enter a valid integer.")
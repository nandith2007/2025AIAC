def validate_indian_mobile_number(number: str) -> bool:
    """
    Validates if the given string is a valid Indian mobile number.
    The number must:
    - Start with 6, 7, 8, or 9
    - Contain exactly 10 digits
    """
    return (
        isinstance(number, str) and
        len(number) == 10 and
        number.isdigit() and
        number[0] in {'6', '7', '8', '9'}
    )

if __name__ == "__main__":
    user_input = input("Enter an Indian mobile number: ")
    if validate_indian_mobile_number(user_input):
        print("Valid Indian mobile number.")
    else:
        print("Invalid Indian mobile number.")
# palindrome_check.py

def is_palindrome(num):
    pass
     # Write Function Only






# --------------------------------------Don't Touch------------------------------------------------------------------

def run_test_cases():
    # Test case 1: Palindrome number
    assert is_palindrome(121) == True

    # Test case 2: Non-Palindrome number
    assert is_palindrome(123) == False

    # Test case 3: Single-digit Palindrome number
    assert is_palindrome(9) == True

    # Test case 4: Single-digit Non-Palindrome number
    assert is_palindrome(7) == True

    # Add more test cases as needed

    print("All test cases passed!")

if __name__ == "__main__":
    # Run the test cases
    run_test_cases()

    # Example usage
    num_to_check = int(input("Enter a number to check for Palindrome: "))
    
    if is_palindrome(num_to_check):
        print(f"{num_to_check} is a Palindrome number.")
    else:
        print(f"{num_to_check} is not a Palindrome number.")

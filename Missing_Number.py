def find_missing_number(arr):
    pass
    # Write Function Only







# --------------------------------------Don't Touch------------------------------------------------------------------

def run_test_cases():
    # Test case 1: Missing number is 4
    arr1 = [1, 2, 3, 5]
    assert find_missing_number(arr1) == 4

    # Test case 2: Missing number is 7
    arr2 = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert find_missing_number(arr2) == 7

    # Add more test cases as needed

    print("All test cases passed!")

if __name__ == "__main__":
    # Run the test cases
    run_test_cases()

    # Example usage
    numbers1 = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    missing_number1 = find_missing_number(numbers1)
    print(f"The missing number is: {missing_number1}")

    numbers2 = [1, 2, 3, 5]
    missing_number2 = find_missing_number(numbers2)
    print(f"The missing number is: {missing_number2}")

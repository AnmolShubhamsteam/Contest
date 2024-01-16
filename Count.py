def count_zeros_ones(arr):
    pass
    # Write Function Only









# --------------------------------------Don't Touch------------------------------------------------------------------


def run_test_cases():
    # Test case 1: 3 zeros, 2 ones
    arr1 = [0, 1, 0, 0, 1]
    count_zeros1, count_ones1 = count_zeros_ones(arr1)
    assert count_zeros1 == 3 and count_ones1 == 2

    # Test case 2: 5 zeros, 0 ones
    arr2 = [0, 0, 0, 0, 0]
    count_zeros2, count_ones2 = count_zeros_ones(arr2)
    assert count_zeros2 == 5 and count_ones2 == 0

    # Add more test cases as needed

    print("All test cases passed!")

if __name__ == "__main__":
    # Run the test cases
    run_test_cases()

    # Example usage
    binary_array = [1, 0, 1, 0, 0, 1, 1, 0, 1]
    count_zeros, count_ones = count_zeros_ones(binary_array)

    print(f"Count of 0's: {count_zeros}")
    print(f"Count of 1's: {count_ones}")

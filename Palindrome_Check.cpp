// palindrome_check.cpp

#include <bits/stdc++.h>

using namespace std;

bool is_palindrome(int num) {
    // Write Function Only
}






// ----------------------------------------Don't Touch--------------------------------------------------------------------
void run_test_cases() {
    // Test case 1: Palindrome number
    assert(is_palindrome(121) == true);

    // Test case 2: Non-Palindrome number
    assert(is_palindrome(123) == false);

    // Test case 3: Single-digit Palindrome number
    assert(is_palindrome(9) == true);

    // Test case 4: Single-digit Non-Palindrome number
    assert(is_palindrome(7) == true);

    // Add more test cases as needed

    cout << "All test cases passed!" << endl;
}

int main() {
    // Run the test cases
    run_test_cases();

    // Example usage
    int numToCheck;
    cout << "Enter a number to check for Palindrome: ";
    cin >> numToCheck;

    if (is_palindrome(numToCheck)) {
        cout << numToCheck << " is a Palindrome number." << endl;
    } else {
        cout << numToCheck << " is not a Palindrome number." << endl;
    }

    return 0;
}

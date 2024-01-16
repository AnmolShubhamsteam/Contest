#include <iostream>
#include <cassert>

using namespace std;

void count_zeros_ones(int arr[], int size, int& count_zeros, int& count_ones) {
    // Write Function Only


    

}






// ----------------------------------------Don't Touch--------------------------------------------------------------------

void run_test_cases() {
    // Test case 1: 3 zeros, 2 ones
    int arr1[] = {0, 1, 0, 0, 1};
    int count_zeros1, count_ones1;
    count_zeros_ones(arr1, sizeof(arr1) / sizeof(arr1[0]), count_zeros1, count_ones1);
    assert(count_zeros1 == 3 && count_ones1 == 2);

    // Test case 2: 5 zeros, 0 ones
    int arr2[] = {0, 0, 0, 0, 0};
    int count_zeros2, count_ones2;
    count_zeros_ones(arr2, sizeof(arr2) / sizeof(arr2[0]), count_zeros2, count_ones2);
    assert(count_zeros2 == 5 && count_ones2 == 0);

    // Add more test cases as needed

    cout << "All test cases passed!" << endl;
}

int main() {
    // Run the test cases
    run_test_cases();
    return 0;
}

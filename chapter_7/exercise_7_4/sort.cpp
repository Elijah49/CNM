/* 
 * Solution to Exercise 7.4.
 *
 * Insertion sort algorithm.
 */
#include <iostream>
#include <cstdlib>
using namespace std;

// Insert a value into the correct position in array
void insert(float a[], int p, float val) {
    // Move items up array until the right place is reached
    while (p > 0 && val < a[p-1]) {
        a[p] = a[p-1];
        p--;
    }

    // Put 'val' in the right place
    a[p] = val;
}

// Perform an insertion sort on an array
void insertionSort(float a[], int length) {
    for (int i = 0; i < length; i++) {
        insert(a,i,a[i]);
    }
}

int main() {
    const int n = 20;
    const int range = 100;

    float a[n];

    // Seed random number generator.
    srand(time(0));

    // Generate and print random numbers
    cout << "Generated random numbers: " << endl;
    for (int i = 0; i < n; i++) {
        a[i] = float(rand()) / RAND_MAX * range;
        cout << a[i] << endl;
    }
    cout << endl;

    // Sort array
    insertionSort(a,n);

    // Print sorted array
    cout << "Sorted random numbers: " << endl;
    for (int i = 0; i < n; i++) {
        cout << a[i] << endl;
    }

    return 0;
}


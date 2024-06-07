#include <stdio.h>

void merge(int array[], int left, int middle, int right) {
    int left_size = middle - left + 1;
    int right_size = right - middle;

    int left_subarray[left_size], right_subarray[right_size];

    for (int i = 0; i < left_size; i++)
        left_subarray[i] = array[left + i];
    for (int j = 0; j < right_size; j++)
        right_subarray[j] = array[middle + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < left_size && j < right_size) {
        if (left_subarray[i] <= right_subarray[j]) {
            array[k] = left_subarray[i];
            i++;
        } else {
            array[k] = right_subarray[j];
            j++;
        }
        k++;
    }

    while (i < left_size) {
        array[k] = left_subarray[i];
        i++;
        k++;
    }

    while (j < right_size) {
        array[k] = right_subarray[j];
        j++;
        k++;
    }
}

void mergeSort(int array[], int left, int right) {
    if (left < right) {
        int middle = left + (right - left) / 2;

        mergeSort(array, left, middle);
        mergeSort(array, middle + 1, right);

        merge(array, left, middle, right);
    }
}

void printArray(int array[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
}

int main() {
    int array[] = {12, 11, 13, 5, 6, 7};
    int array_size = sizeof(array) / sizeof(array[0]);

    printf("Given array is \n");
    printArray(array, array_size);

    mergeSort(array, 0, array_size - 1);

    printf("\nSorted array is \n");
    printArray(array, array_size);
    return 0;
}

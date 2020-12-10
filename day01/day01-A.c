/* day01-A.c: https://adventofcode.com/2020/day/1 */

#include <stdio.h>

/* Constants */

#define NSIZE   200
#define TARGET  2020

/* Functions */

size_t read_numbers(int *numbers) {
    int    number;
    size_t index;

    while (scanf("%d", &number) != EOF) {
        numbers[index++] = number;
    }

    return index;
}

int find_pair_product(int *numbers, size_t n, int target) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            if (numbers[i] + numbers[j] == target) {
                return numbers[i] * numbers[j];
            }
        }
    }

    return 0;
}

/* Main Execution */

int main(int argc, char *argv[]) {
    int    numbers[NSIZE] = {0};
    size_t nsize          = read_numbers(numbers);
    int    product        = find_pair_product(numbers, nsize, TARGET);

    printf("%d\n", product);
    return 0;
}

/* vim: set expandtab sts=4 sw=4 ts=8 ft=c: */

# Author: Hogan Lin
# Date: Mar 6th 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Description: Analyzing sorting algorithms with different input lists

import random
from algs import sort3, bubble_sort

# Counter for comparisons and swaps
class Counter:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def compare(self, a, b):
        self.comparisons += 1
        return a > b

    def swap(self, l, i, j):
        self.swaps += 1
        l[i], l[j] = l[j], l[i]

def instrumented_bubble_sort(l, counter):
    """
    Instrumented version of bubble sort to count comparisons and swaps.
    """
    n = len(l)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if counter.compare(l[j], l[j + 1]):
                counter.swap(l, j, j + 1)
                swapped = True
        if not swapped:
            break

# Generating different input lists
def generate_sorted_list(n):
    return list(range(n))

def generate_reversed_list(n):
    return list(range(n, 0, -1))

def generate_random_list(n):
    return [random.randint(0, 1000) for _ in range(n)]

def generate_almost_sorted_list(n):
    l = list(range(n))
    if n > 1:
        l[n//2], l[n//2 - 1] = l[n//2 - 1], l[n//2]  # Swap two elements
    return l

def generate_few_unique_list(n):
    return [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]

def analyze():
    sizes = [10, 100, 500]
    sorts = {"Bubble Sort": instrumented_bubble_sort}
    lists = {
        "Sorted": generate_sorted_list,
        "Reversed": generate_reversed_list,
        "Random": generate_random_list,
        "Almost Sorted": generate_almost_sorted_list,
        "Few Unique": generate_few_unique_list
    }

    results = []
    for name, generator in lists.items():
        for size in sizes:
            l = generator(size)
            for sort_name, sort_func in sorts.items():
                counter = Counter()
                sort_func(l[:], counter)  # Sort copy to avoid modifying original
                result = f"{sort_name} on {name} list of size {size}: {counter.comparisons} comparisons, {counter.swaps} swaps"
                results.append(result)
                print(result)  # Print for debugging

    with open("summary.txt", "w", encoding="utf-8") as f:
        for result in results:
            f.write(result + "\n")
        f.flush()  # Ensure content is written


if __name__ == "__main__":
    analyze()

# Step 1: Implement Modified Linear Search
def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  # Append index to the list if target is found
    return indices if indices else -1  # Return -1 if target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 5)
print(f"Linear Search: Indices of 5 are {result}")



#Step 2: Implement Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")



#Step 3: Compare Performance
import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)



#Step 4: Implement Recursive Binary Search
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")



#Step 5: Create a Main Function
def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

print()
def find_insertion_point(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left  # The insertion point

# Test the function
sorted_list = [1, 3, 5, 7, 9]
target = 6
insertion_point = find_insertion_point(sorted_list, target)
print(f"Insertion point for {target} is index {insertion_point}")
print()



# Linear Search with comparison counting
def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1  # Increment for each comparison
        if arr[i] == target:
            return i, comparisons  # Return index and comparison count
    return -1, comparisons  # Return -1 and comparison count if target not found

# Iterative Binary Search with comparison counting
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1  # Increment for each comparison
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons  # Return index and comparison count
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons  # Return -1 and comparison count if target not found

# Recursive Binary Search with comparison counting
def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons  # Return -1 and comparison count if target not found
    
    comparisons += 1  # Increment for each comparison
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)

# Function to test and compare the algorithms
def compare_search_algorithms(arr, target):
    # Linear Search
    index, linear_comparisons = linear_search(arr, target)
    print(f"Linear Search: Index {index}, Comparisons {linear_comparisons}")

    # Binary Search (iterative)
    sorted_arr = sorted(arr)
    index, binary_comparisons = binary_search(sorted_arr, target)
    print(f"Binary Search (iterative): Index {index}, Comparisons {binary_comparisons}")

    # Binary Search (recursive)
    index, recursive_comparisons = binary_search_recursive(sorted_arr, target, 0, len(sorted_arr) - 1)
    print(f"Binary Search (recursive): Index {index}, Comparisons {recursive_comparisons}")

# Test the function with a list and a target value
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 6
compare_search_algorithms(test_list, target)

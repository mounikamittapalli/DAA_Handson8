import random
def quickselect(arr, left, right, i):
    if left == right:
        return arr[left]

    # Randomly select a pivot index
    pivot_index = random.randint(left, right)
    pivot_index = partition(arr, left, right, pivot_index)

    # The pivot is in its sorted position
    if i == pivot_index:
        return arr[i]
    elif i < pivot_index:
        # Look for the i-th order statistic in the left subarray
        return quickselect(arr, left, pivot_index - 1, i)
    else:
        # Look for the i-th order statistic in the right subarray
        return quickselect(arr, pivot_index + 1, right, i)


def partition(arr, left, right, pivot_index):
    """ Partitions the array around the pivot element and returns the final position of the pivot. """
    pivot_value = arr[pivot_index]
    # Move the pivot to the end
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # Move the pivot to its correct place
    arr[right], arr[store_index] = arr[store_index], arr[right]

    return store_index


# Example usage
arr = [12, 3, 5, 7, 19, 1, 18, 6, 13]
print(arr)
i = 5  # 1-based index for the ith smallest element
order_statistic = quickselect(arr, 0, len(arr) - 1, i - 1)  # Convert to 0-based index
print(f"The {i}-th order statistic is {order_statistic}")

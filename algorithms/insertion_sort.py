def insertion_sort(data):
    arr = data.copy()

    # Start from the second element as the first element is considered sorted
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0,,,i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr # Yield after each shift operation

        # Insert the key to the right position
        arr[j + 1] = key
        yield arr # Yield after inserting the key

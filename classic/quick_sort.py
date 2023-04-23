def quickSort(arr):
    if len(arr) < 2:
        return arr

    else:
        p_idx = math.random.randint(0, len(arr))
        pivot = arr[p_idx]

        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)
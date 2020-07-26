def quick_sort(sequence):
    iteration_length = len(sequence)
    if iteration_length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_smaller, items_greater = [], []

    for item in sequence:
        if item < pivot:
            items_smaller.append(item)
        else:
            items_greater.append(item)

    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)


print(quick_sort([1, 3, 5, 7, 2, 4, 6]))

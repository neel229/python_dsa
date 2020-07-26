def insertion_sort(list):
    iteration_length = range(1, len(list))
    # Passthrough
    for i in iteration_length:
        value_to_sort = list[i]

        while list[i-1] > value_to_sort and i > 0:
            list[i], list[i-1] = list[i-1], list[i]
            i = i-1

    return list

print(insertion_sort([1,3,5,7,2,4,6]))

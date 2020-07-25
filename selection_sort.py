def selection_sort(demo_list):

    for i in range(len(demo_list)):
        min_value = i

        for j in range(i, len(demo_list)):
            if demo_list[j] < demo_list[min_value]:
                min_value = j
        # Swap the values
        demo_list[i], demo_list[min_value] = demo_list[min_value], demo_list[i]


demo_list = [23, 12, 1, 3, 4, 5, 8]
selection_sort(demo_list)

print(demo_list)


def bubble(list):
    iteration_lenght = len(list) - 1
    sorted = False

    # Logic
    while not sorted:
        sorted = True
        for i in range(0, iteration_lenght):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]

list = [1, 2, 45, 89, 4, 5]
bubble(list)

print(list)

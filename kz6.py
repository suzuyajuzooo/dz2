def print_average(arr):
    if not arr:
        print(0)
    else:
        average = sum(arr) / len(arr)
        print(average)
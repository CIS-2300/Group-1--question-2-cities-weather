def comparetoavg(a, b, c, avg):
    """Prints whether each number is below, equal to, or above the average."""
    original_equal_nums= 0
    for val in [a, b, c]:
        if val < avg:
            print(f'{val} is less than the average {avg}.')
        elif val > avg:
            print(f'{val} is greater than the average {avg}.')
        else:
            print(f'{val} is equal to the average {avg}')
            original_equal_nums+= 1
    print(f'There are {original_equal_nums} numbers that are equal to the average.')

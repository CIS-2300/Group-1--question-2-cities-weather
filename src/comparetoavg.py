def compareToAvg(avg, nums):
    for num in nums:
        if num < avg:
            print(f"{num} is below the average")
        elif num == avg:
            print(f"{num} is equal to the average")
        else:
            print(f"{num} is above the average")


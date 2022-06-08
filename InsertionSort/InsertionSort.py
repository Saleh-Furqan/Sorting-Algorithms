def sort(nums):
    indexLength = range(1, len(nums))

    for i in indexLength:
        valToSort = nums[i]

        while nums[i - 1] > valToSort and i > 0:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i = i - 1

    return nums


print(sort([5, 1, 2, 4, 10, 12, 11, 18, 15, 17]))

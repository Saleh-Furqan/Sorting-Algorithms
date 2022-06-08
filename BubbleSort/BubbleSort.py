def sort(nums):
    indexLength = len(nums) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(indexLength):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


print(sort([1, 3, 10, 5, 4, 3, 7]))
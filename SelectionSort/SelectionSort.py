def sort(nums):
    indexLength = range(len(nums) - 1)

    for i in indexLength:
        minVal = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                minVal = j

        if minVal != i:
            nums[minVal], nums[i] = nums[i], nums[minVal]

    return nums


print(sort([10, 9, 5, 7, 4, 1, 20, 28]))

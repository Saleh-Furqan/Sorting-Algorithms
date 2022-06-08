def sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    lowerItems = []
    greaterItems = []

    for i in nums:
        if i > pivot:
            greaterItems.append(i)

        else:
            lowerItems.append(i)

    return sort(lowerItems) + [pivot] + sort(greaterItems)


print(sort([5, 10, 20, 3, 7, 2, 8, 9, 1]))
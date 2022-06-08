def sort(sequence, item):
    indexStart = 0
    indexEnd = len(sequence) - 1

    while indexStart <= indexEnd:
        midpoint = indexStart + (indexEnd - indexStart) // 2
        midpointVal = sequence[midpoint]

        if midpointVal == item:
            return midpoint
        elif item < midpointVal:
            indexEnd = midpoint - 1
        else:
            indexStart = midpoint + 1

    return None


sequence = [2, 3, 4, 5, 10, 11, 15, 18, 20, 30, 47, 52, 69]
item = 15

print(sort(sequence, item))

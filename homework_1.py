arr = [2, 7, 11, 15]
target = 9


# Big-O: O(n^2)
def two_sum(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]

    return None


print(two_sum(arr, target))


# Big-O: O(n)
def two_sum(arr, target):
    dres = {}

    for i, val in enumerate(arr):
        diff = target - val
        if diff in dres:
            return [dres[diff], i]

        dres[val] = i

    return None


print(two_sum(arr, target))

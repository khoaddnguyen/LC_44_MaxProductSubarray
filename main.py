def maxProduct(self, nums: List[int]) -> int:

    result = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:  # to single out zero, but this IF does not do anything
            curMin, curMax = 1, 1
            continue

        temp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        # below will bug, therefore, replace with a temp
        # curMin = min(n * curMax, n * curMin, n)
        curMin = min(temp, n * curMin, n)
        result = max(result, curMax)

    return result

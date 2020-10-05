from typing import List

def maxSubArray(nums: List[int]) -> int:

    # if only one integer in nums, sum will be just that integer
    if len(nums) == 1:
        return nums[0]

    currsum = maxsum = nums[0]

    # only care about return the max sum therefore only keep track of sums
    for num in nums[1:]:
        currsum = max(num, num + currsum)
        maxsum = max(maxsum, currsum)

    return maxsum


if __name__ == '__main__':

    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray([1239875]))
    print(maxSubArray([-1]))
    print(maxSubArray([0]))
    print(maxSubArray([2, 5, 3, -5, 0, -3, 2, 5]))

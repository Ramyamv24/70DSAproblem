class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        p = {}
        for i, num in enumerate(nums):
            if target - num in p:
                return [i, p[target - num]]
            p[num] = i


# Main part
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    obj = Solution()
    result = obj.twoSum(nums, target)

    print(result)
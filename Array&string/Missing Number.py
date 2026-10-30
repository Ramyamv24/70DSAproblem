class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


# Main part
if __name__ == "__main__":
    nums = [3, 0, 1]

    obj = Solution()
    result = obj.missingNumber(nums)

    print(result)
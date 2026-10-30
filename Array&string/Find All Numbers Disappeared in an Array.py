class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]


# Main part
if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    obj = Solution()
    result = obj.findDisappearedNumbers(nums)

    print(result)
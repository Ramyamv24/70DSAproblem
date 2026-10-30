class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)


# Main part
if __name__ == "__main__":
    nums = [1, 2, 3, 1]

    obj = Solution()
    result = obj.containsDuplicate(nums)

    print(result)
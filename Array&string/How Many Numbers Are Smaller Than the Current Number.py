class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        allnums = [0] * 101
        res = [0] * len(nums)

        for n in nums:
            allnums[n] += 1

        for i in range(1, 101):
            allnums[i] += allnums[i - 1]

        for i in range(len(nums)):
            v = nums[i]
            if v == 0:
                res[i] = 0
            else:
                res[i] = allnums[v - 1]

        return res


# Main part
if __name__ == "__main__":
    nums = [8, 1, 2, 2, 3]

    obj = Solution()
    result = obj.smallerNumbersThanCurrent(nums)

    print(result)
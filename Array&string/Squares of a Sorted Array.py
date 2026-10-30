from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1

        return res


# Main part
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]

    obj = Solution()
    result = obj.sortedSquares(nums)

    print(result)
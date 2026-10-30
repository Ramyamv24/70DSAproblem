from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        i = 1

        while i < n - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i
                right = i

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                ans = max(ans, right - left + 1)
                i = right
            else:
                i += 1

        return ans


# Main part
if __name__ == "__main__":
    arr = [2, 1, 4, 7, 3, 2, 5]

    obj = Solution()
    result = obj.longestMountain(arr)

    print(result)
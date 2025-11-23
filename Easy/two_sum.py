from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
if __name__ == "__main__":
        solver = Solution()
        nums1 = [2, 7, 11, 15]
        target1 = 9
        result1 = solver.twoSum(nums1, target1)
        print(f"Test 1 - Giriş: {nums1}, Hedef: {target1}")
        print(f"Test 1 - Sonuç: {result1}")


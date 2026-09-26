class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        bucket = [0, 0, 0]

        for num in nums:
            bucket[num] += 1

        
        i = 0

        for index, num in enumerate(bucket):
            while num:
                nums[i] = index
                num -= 1
                i += 1

        
        return nums
        
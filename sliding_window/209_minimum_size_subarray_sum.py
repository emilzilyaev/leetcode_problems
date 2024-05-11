class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimal_diff =  1000000000
        currentSum = nums[0]
        left, right = 0, 0

        while (left != len(nums)):
            print(left, right)
            if currentSum < target:
                if right < len(nums) - 1:
                    right += 1
                    currentSum += nums[right]
                else:
                    break

            elif currentSum >= target:
                if minimal_diff > right-left:
                    minimal_diff = right-left
                currentSum -= nums[left]
                left += 1
        if minimal_diff ==1000000000:
            return 0
        else: 
            return minimal_diff+1

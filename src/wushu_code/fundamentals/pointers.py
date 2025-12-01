

class TwoSumSortedArray: 
    def two_sum_assorted_array(self, nums: list, target: int):
        """
        Set pointers
        left is at 0
        right is at the far end 

        Rules: 
        If sum < target, move the left up to a bigger number 
        If sum > target, move the right down to a smaller number 
        Return when the left and right equal the target 
        """
        
        left, right = 0, len(nums) - 1

        while left < right:
            current = nums[left] + nums[right]

            if current == target:
                return (left, right)
            elif current < target:
                left += 1
            else:
                right -= 1

        return None  # or (-1, -1) if you prefer a sentinel
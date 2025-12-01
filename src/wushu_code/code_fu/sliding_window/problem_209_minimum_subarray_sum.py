# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# [1,2,3,4,5]

class Problem209:

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_array = []
        min_len = float("inf")
        left_index =0
        curr_sum = 0

        for right_index in range(len(nums)): 

            curr_sum+=nums[right_index]

            #While the sum is equal or greater than target, adjust left side 
            while curr_sum >= target: 

                #Indexes lenth (plus 1 because index starts from zero)
                if right_index - left_index + 1 < min_len:
                    min_len = right_index - left_index + 1
                    #min_array = nums[left_index:right_index]

                #Slide left window right 
                curr_sum -= nums[left_index]
                left_index+=1
        
        return 0 if min_len == float("inf") else min_len #, [] if min_len is float("inf") else min_array

















    # def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    #     min_len = float("inf")
    #     left = 0
    #     cur_sum = 0

    #     for right in range(len(nums)):
    #         cur_sum += nums[right]

    #         while cur_sum >= target:
    #             if right - left + 1 < min_len:
    #                 print(right)
    #                 print(left)
    #                 min_len = right - left + 1
    #             cur_sum -= nums[left]
    #             left += 1
        
    #     return min_len if min_len != float("inf") else 0
            
            




    
    

def main():
    
    b = Problem209()
    #target = 7
    #nums = [2,3,1,2,4,3]
    target = 11
    #nums = [1,2,3,4,5]
    nums = [1,1,1,1,1,1,1,1]
    min_array = b.minSubArrayLen(target, nums)

    print(f"Min array {min_array}")

if __name__ == "__main__": main()



class Problem189: 

    def rotate(self, nums: list[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]
        Example 2:

        """

        #Step: Find last k-3 elements 
        #Step: Insert into a list 
        #Step: Go through remaining 0 to k-4 elements 
        
        #left_list = range(nums[k-3:k])
        #right_list = range(nums[0:k-4])
        n = len(nums)
        left_list = nums[n-k:n]
        right_list = nums[0:n-k]
        rotated_list = left_list + right_list

        return rotated_list

    

def main():
    
    b = Problem189()
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotated_list = b.rotate(nums, k)
    print(f"Rotated array is {rotated_list}")

if __name__ == "__main__": main()





# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n

class Problem88: 


    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        merged_array = []
        nums1 = [x for x in nums1 if x > 0]
        nums2 = [x for x in nums2 if x > 0]
        merged_array = nums1+nums2
        merged_array.sort()
        

        assert len(merged_array) == m+n
        return merged_array

    def derp_merge(self, nums1, m, nums2, n):
        """
        use this for leetcode but not a fan of this solution

        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = 0
        for i in range(m, m+n): 
            nums1[i] = nums2[k]
            k+=1
        nums1.sort()
        return nums1


def main():
    
    b = Problem88()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merged_array = b.merge(nums1, m, nums2, n)
    another_merged_array = b.derp_merge(nums1, m, nums2, n)
    
    print(f"Merged Array is {merged_array}")
    print(f"Another merged array is {another_merged_array}")

if __name__ == "__main__": main()


class Problem26SortedArray: 


    def removeDuplicates(self, nums): 
        seen = set() 
        output_array = list()

        for num in nums: 
            if num in seen: 
                output_array.append(-1)
            else: 
                output_array.append(num)
                seen.add(num)
        
        sorted_ouput_array = sorted(output_array, key=lambda x: (x is -1, x))
        
        return sorted_ouput_array
                
def main():
    
    b = Problem26SortedArray()
    array = [1,2,2,3,4,4,5]
    sorted_array = b.removeDuplicates(array)
    print(f"Sorted array is{sorted_array}")

if __name__ == "__main__": main()

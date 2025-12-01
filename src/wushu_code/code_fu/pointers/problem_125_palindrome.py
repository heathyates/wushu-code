#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

import re 

#0. Convert all uppercase to lowercase letters 
class Problem189: 

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        #
        Input: s = "A man, a plan, a canal: Panama"
        """

        s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
        rtype = True 


        left, right = 0, len(s)-1
        
        while left <= right: 
            if s[left] == s[right]: 
                left+=1
                right-=1
            else:
                return False
        
        return True
            
#poop
#pooop
#raceacar
#rr
#aa
#cc
#ea


def main():
    
    b = Problem189()
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    is_palidrome = b.isPalindrome(s)
    print(f"s = {s}, palidrome status is {is_palidrome}")

if __name__ == "__main__": main()


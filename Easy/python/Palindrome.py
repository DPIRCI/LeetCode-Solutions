from typing import List
#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x:int) -> bool:
        reverse=0
        temp=abs(x)
        while(temp>0):
            # temp%10 taking the last digit
            reverse=(reverse*10)+(temp%10)#add the last digit to the front
            temp=temp//10
        return reverse==x






if __name__ == "__main__":
    s=Solution()#solution object created
    x=232
    print("input:",x)
    print("output:",s.isPalindrome(x))
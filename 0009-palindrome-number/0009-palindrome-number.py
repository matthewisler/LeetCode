class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = [x for x in str(x)]
        for i in range(int(len(x_list)/2)):
            if x_list[i] != x_list[len(x_list)-1-i]:
                return False
        return True
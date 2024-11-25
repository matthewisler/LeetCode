class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [x.lower() for x in s if x.isalpha() or x.isnumeric()]
        s = "".join(s_list)
        i = 0
        loop_length = len(s)/2
        while i < loop_length:
            print(f"does {s[i]} == {s[len(s_list)-(1+i)]}")
            if s[i] == s[len(s_list)-(1+i)]:
                print("yes, continuing to next set of letters")
            else:
                print("no, returning False")
                return False
            i+=1
        return True

        
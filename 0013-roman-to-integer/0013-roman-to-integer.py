class Solution:
    def romanToInt(self, s: str) -> int:
        str_list = [x for x in s]
        ret_val = 0
        letter_dict = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in range(len(str_list)):
            if i < len(str_list)-1 and letter_dict[s[i]] < letter_dict[s[i+1]]:
                ret_val -= letter_dict[s[i]]
            else:
                ret_val += letter_dict[s[i]]
        return ret_val
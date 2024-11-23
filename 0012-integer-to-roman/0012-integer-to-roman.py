class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num_list = [x for x in str(num)]
        starting_place = len(num_list)
        print(f"starting_place: {starting_place}")
        output = ""
        if starting_place == 4:
            output += ("M" * int(num_list[0]))
            num_list.remove(num_list[0])

        starting_place = len(num_list)   
        if starting_place == 3:
            if int(num_list[0]) == 9:
                output += "CM"
            elif int(num_list[0]) >= 5:
                output += "D"+ ("C"*(int(num_list[0])-5))
            elif int(num_list[0]) == 4:
                output += "CD"
            else:
                output += ("C"*int(num_list[0]))
            num_list.remove(num_list[0])

        starting_place = len(num_list) 
        if starting_place == 2:
            if int(num_list[0]) == 9:
                output += "XC"
            elif int(num_list[0]) >= 5:
                output += "L"+ ("X"*(int(num_list[0])-5))
            elif int(num_list[0]) == 4:
                output += "XL"
            else:
                output += ("X"*int(num_list[0]))
            num_list.remove(num_list[0])

        starting_place = len(num_list) 
        if starting_place == 1:
            if int(num_list[0]) == 9:
                output += "IX"
            elif int(num_list[0]) >= 5:
                output += "V"+ ("I"*(int(num_list[0])-5))
            elif int(num_list[0]) == 4:
                output += "IV"
            else:
                output += ("I"*int(num_list[0]))
            num_list.remove(num_list[0])



        return output
        
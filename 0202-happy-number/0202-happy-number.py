class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0
        prev_numbers = []
        print(f"starting n: {n}")
        while i < 100:
            n_list = [x for x in str(n)]
            #print(n_list)
            for i in range(len(n_list)):
                n_list[i] = int(n_list[i])**2
                #print(f"n_list[i]: {str(n_list[i])}")
            n = sum(n_list)
            #print(f"is {n} == 1")
            if n == 1:
                return True
            elif n in prev_numbers:
                return False
            else:
                prev_numbers.append(n)

            i += 1
        return False
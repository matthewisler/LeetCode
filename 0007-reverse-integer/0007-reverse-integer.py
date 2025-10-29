class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x:
            if '-' in str(x):
                neg = True
                x *= -1

            x_list = [str(num) for num in str(x)]
            print(x_list)
            output = int(''.join(x_list[::-1]))
            if neg:
                output *= -1

            if output > (2**31) - 1 or output < -2**31:
                return 0
            
            
            return output

        return 0
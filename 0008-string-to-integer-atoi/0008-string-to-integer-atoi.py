class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s.strip()):
            output = []
            s = s.strip()
            neg = '-' == s[0]
            pos = "+" == s[0]
            if neg or pos:
                s = s[1:]
            
            print(s)
            for num in s:
                if num.isnumeric():
                    output.append(num)
                else:
                    break
            if output:
                out_str = "".join(output)
                output = int(out_str) if not neg else -1*int(out_str)

                if output > (2**31) - 1:
                    return (2**31) - 1
                if output < -2**31:
                    return -2**31
                return output
            return 0
        return 0

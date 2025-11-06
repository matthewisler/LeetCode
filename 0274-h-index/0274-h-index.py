class Solution:
    def hIndex(self, citations: List[int]) -> int:
        output = 0
        

        for i in range(1, len(citations)+1):
            cites = [x for x in citations if i<=x]
            print(f"cites: {cites}")
            if len(cites) >= i:
                output = i
                print(f"output set to: {output}")
                
        return output
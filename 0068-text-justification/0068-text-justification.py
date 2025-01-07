class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        width = 0

        for word in words:
            if width + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - width):
                    line[i % (len(line)-1 or 1)] += ' '
                    
                res = res + [''.join(line)]
                line = []
                width = 0
            
            line += [word]
            width += len(word)
        
        return res + [' '.join(line).ljust(maxWidth)]
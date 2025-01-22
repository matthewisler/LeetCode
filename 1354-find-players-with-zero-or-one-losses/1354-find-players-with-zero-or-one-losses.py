class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_losses = set()
        for match in matches:
            winner = match[0]
            loser = match[1]
            if (winner not in more_losses) and (winner not in one_loss):
                zero_loss.add(winner)
            
            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            
            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            
            elif loser in more_losses:
                continue
            
            else:
                one_loss.add(loser)
        
        return [sorted(list(zero_loss)), sorted(list(one_loss))]
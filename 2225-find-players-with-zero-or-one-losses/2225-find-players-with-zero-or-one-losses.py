class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # define dictionaries
        winners = set()
        losers = set()
        winners_with_loss_count = dict()
        players_loss_count = dict()
        
        # answers
        winners_with_no_loss = []
        players_one_loss = []
        
        # iterate through the matches to identify 
        for match in matches:
            # add winners to set
            winners.add(match[0])
            winners_with_loss_count[match[0]] = 0
            # add losers to set
            losers.add(match[1])
            players_loss_count[match[0]] = 0
            players_loss_count[match[1]] = 0
            
        # iterate through matches to get winners' & losers' loss count
        for match in matches:
            # if current match loser is in winner's set
            if match[1] in winners:
                winners_with_loss_count[match[1]] += 1
            
            players_loss_count[match[1]] += 1
                
        # iterate through winners' loss
        for key in winners_with_loss_count:
            if winners_with_loss_count[key] == 0:
                winners_with_no_loss.append(key)
                
        # iterate through all players' loss
        for key in players_loss_count:
            if players_loss_count[key] == 1:
                players_one_loss.append(key)
                
        winners_with_no_loss.sort()
        players_one_loss.sort()
        
        return [winners_with_no_loss, players_one_loss]
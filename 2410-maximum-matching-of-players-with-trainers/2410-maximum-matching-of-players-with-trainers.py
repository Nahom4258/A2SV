class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        player_ptr = 0
        trainer_ptr = 0
        
        players.sort()
        trainers.sort()
        matched = 0
        
        while player_ptr < len(players) and trainer_ptr < len(trainers):
            if players[player_ptr] <= trainers[trainer_ptr]:
                matched += 1
                player_ptr += 1
                trainer_ptr += 1
            else:
                trainer_ptr += 1
                
        return matched
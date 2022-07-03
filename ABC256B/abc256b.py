class Baseball:
    def __init__(self, num_of_batters, num_of_bases_advanced):
        self.num_of_batters = num_of_batters
        self.num_of_bases_advanced = num_of_bases_advanced

    def get_scores(self):
        num_of_bases_with_batter = [0] * self.num_of_batters
        for i in range(self.num_of_batters):
            for j in range(i+1):
                num_of_bases_with_batter[j] = num_of_bases_with_batter[j] + self.num_of_bases_advanced[i]
        scores = len([k for k in num_of_bases_with_batter if k >= 4])
        return scores


N = int(input())
A = list(map(int, input().split()))
baseball_game = Baseball(N, A)
game_scores = baseball_game.get_scores()
print(game_scores)

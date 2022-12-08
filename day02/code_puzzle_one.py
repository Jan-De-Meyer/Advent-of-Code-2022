play_rewards = ["X","Y","Z"]
index_opponent = ["A","B","C"]
total_score = 0
round_score = 0

def add_score_up(round_score ,your_hand):
    return round_score + play_rewards.index(your_hand)+1
def win(your_hand): 
    round_score =6
    return add_score_up(round_score, your_hand)

with open("values.txt") as file:
      for line in file:
        your_hand = line[2]
        opponents_hand = line[0]
        #when you tie
        if index_opponent.index(opponents_hand) == play_rewards.index(your_hand):
            round_score += 3
            total_score += add_score_up(round_score,your_hand)
            round_score = 0
        #when you win
        elif opponents_hand == "A" and your_hand == "Y":
            round_score += 6
            total_score += win(your_hand)
            round_score = 0
        elif opponents_hand == "B" and your_hand == "Z":
            round_score += 6
            total_score += win(your_hand)
            round_score = 0
        elif opponents_hand == "C" and your_hand == "X":
            round_score += 6
            total_score += win(your_hand)
            round_score = 0
        #when you lose
        else:
            total_score += add_score_up(round_score,your_hand)
            round_score = 0
print(total_score)

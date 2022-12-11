
index_opponent = ["A","B","C"]
total_score = 0
round_score = 0


def add_score_up(round_score ,your_hand):
    return round_score + index_opponent.index(your_hand)+1


with open("values.txt") as file:
      for line in file:
        outcome = line[2]
        opponents_hand = line[0]
        if outcome == "Y":
          total_score += add_score_up(3,opponents_hand)  
          round_score =0
        elif outcome == "X":
            if opponents_hand == "A":
                total_score += add_score_up(0,"C")
            elif opponents_hand == "B":
                 total_score += add_score_up(0,"A")
            else:
                total_score += add_score_up(0,"B")
            round_score =0
        
        elif outcome =="Z":
            if opponents_hand == "A":
                total_score += add_score_up(6,"B")
            elif opponents_hand == "B":
                 total_score += add_score_up(6,"C")
            else:
                total_score += add_score_up(6,"A")
            round_score =0
print(total_score)
print(f"Dealer hand:   ", end="")
for i in range(1,19):
    print(f"[Root.get_b_d_{i}] ", end="")
print("\\n", end="")
for i in range(1,5):
    print(f"[blackjack_player_{i}_tag.GetName]'s hand:  ", end="")
    for j in range(1,19):
        print(f"[Root.get_b_p{i}_{j}] ", end="")
    print("\\n", end="")
print("Dealer Status: [Root.get_ds]\\n", end="")
for i in range(1,5):
    print(f"[blackjack_player_{i}_tag.GetName]'s Status: [Root.get_p{i}s]\\n", end="")

for i in range(1,5):
    print(f"[blackjack_player_{i}_tag.GetName]'s Bet: [Root.bet_value_p{i}.GetValue] ducats\\n", end="")

for i in range(1,5):
    print(f"[blackjack_player_{i}_tag.GetName]'s Value: [Root.blackjack_player_{i}_hand_value.GetValue]\\n", end="")
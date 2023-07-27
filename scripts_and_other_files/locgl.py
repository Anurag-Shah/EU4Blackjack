# print(f"Dealer hand: ", end="")
# for i in range(1,19):
#     print(f"[Root.blackjack_dealer_hand_{i}.GetValue]  ", end="")
# print("\\n", end="")
# for i in range(1,5):
#     print(f"Player {i} hand: ", end="")
#     for j in range(1,19):
#         print(f"[Root.blackjack_player_{i}_hand_{j}]  ", end="")
#     print("\\n"`, end="")

print(f"Dealer hand:   ", end="")
for i in range(1,19):
    print(f"[Root.get_b_d_{i}] ", end="")
print("\\n", end="")
for i in range(1,5):
    print(f"Player {i} hand:  ", end="")
    for j in range(1,19):
        print(f"[Root.get_b_p{i}_{j}] ", end="")
    print("\\n", end="")
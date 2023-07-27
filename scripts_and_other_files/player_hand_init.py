for j in range(1,5):
    for i in range(1,19):
        print("\tset_variable = {")
        print(f"\t\twhich = blackjack_player_{j}_hand_{i}")
        print("\t\tvalue = 0") 
        print("\t}")
for i in range(1, 18):
    print("\tset_variable = {")
    print(f"\t\twhich = blackjack_dealer_hand_{i}")
    print("\t\tvalue = 0") 
    print("\t}")
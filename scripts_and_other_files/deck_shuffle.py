for i in range(208):
    print("\t\t\t\trandom_list = {")
    for j in range(208):
        if i == j:
            continue
        print("\t\t\t\t\t1 = {")
        print(f"\t\t\t\t\t\t# Swap {i} and {j}")
        print("\t\t\t\t\t\tset_variable = {")
        print("\t\t\t\t\t\t\twhich = swapper")
        print(f"\t\t\t\t\t\t\twhich = blackjack_deck_{i}")
        print("\t\t\t\t\t\t}")
        print("\t\t\t\t\t\tset_variable = {")
        print(f"\t\t\t\t\t\t\twhich = blackjack_deck_{i}")
        print(f"\t\t\t\t\t\t\twhich = blackjack_deck_{j}")
        print("\t\t\t\t\t\t}")
        print("\t\t\t\t\t\tset_variable = {")
        print(f"\t\t\t\t\t\t\twhich = blackjack_deck_{j}")
        print("\t\t\t\t\t\t\twhich = swapper")
        print("\t\t\t\t\t\t}")
        print("\t\t\t\t\t}\n")
    print("\t\t\t\t}\n")
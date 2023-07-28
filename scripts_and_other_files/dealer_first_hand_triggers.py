stri = """blackjack_dealer_first_card_is_%s = {
	OR = {
		AND = {
			check_variable = {
				which = blackjack_dealer_hand_1
				value = %s
			}
			NOT = {
				check_variable = {
					which = blackjack_dealer_hand_1
					value = %s
				}
			}
		}
		AND = {
			check_variable = {
				which = blackjack_dealer_hand_1
				value = %s
			}
			NOT = {
				check_variable = {
					which = blackjack_dealer_hand_1
					value = %s
				}
			}
		}
		AND = {
			check_variable = {
				which = blackjack_dealer_hand_1
				value = %s
			}
			NOT = {
				check_variable = {
					which = blackjack_dealer_hand_1
					value = %s
				}
			}
		}
		AND = {
			check_variable = {
				which = blackjack_dealer_hand_1
				value = %s
			}
			NOT = {
				check_variable = {
					which = blackjack_dealer_hand_1
					value = %s
				}
			}
		}
	}
}"""

for i in range(1, 14):
    print(stri % (i, i, i+1, i+13, i+14, i+26, i+27, i+39, i+40))
    print()
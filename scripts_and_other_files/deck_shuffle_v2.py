str1 = '''%s = {
    set_province_flag = blackjack_shuffle_province
}\n'''

str2 = '''event_target:blackjack_player_1_tag = {
    set_variable = {
        which = blackjack_deck_iterator
        value = 1
    }

    while = {
        limit = {
            NOT = {
                check_variable = {
                    which = blackjack_deck_iterator
                    value = 53
                }
            }
        }
        set_variable = {
            which = blackjack_deck_iterator_2
            value = 0
        }
        while = {
            limit = {
                NOT = {
                    check_variable = {
                        which = blackjack_deck_iterator_2
                        value = 4
                    }
                }
            }
            random_province = {
                limit = {
                    AND = {
                        has_province_flag = blackjack_shuffle_province
                        NOT = {
                            has_province_flag = blackjack_shuffle_assigned
                        }
                    }
                }
                set_province_flag = blackjack_shuffle_assigned
                set_variable = {
                    which = blackjack_deck_iterator
                    which = event_target:blackjack_player_1_tag
                }
            }
            change_variable = {
                which = blackjack_deck_iterator_2
                value = 1
            }
        }
        change_variable = {
            which = blackjack_deck_iterator
            value = 1
        }
    }
}

every_province = {
    clr_province_flag = blackjack_shuffle_assigned
}
'''

str4 = '''
%s = {
    event_target:blackjack_player_1_tag = {
        set_variable = {
            which = blackjack_deck_iterator
            which = PREV
        }
        set_variable = {
            which = blackjack_deck_%s
            which = blackjack_deck_iterator
        }
    }
}'''

for i in range(1, 209):
    print(str1 % i)
print(str2)
for i in range(1, 209):
    print(str4 % (i, i-1))
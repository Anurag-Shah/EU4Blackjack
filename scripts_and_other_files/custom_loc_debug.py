for i in range(1,5):
    for j in range(1,19):
        print("""defined_text = {
    name = get_b_p%d_%d""" % (i, j))

        for k in range(1, 14):
            print("""\ttext = {
		localisation_key = debug_card_%d
		trigger = {
            event_target:blackjack_player_1_tag = {
                OR = {
                    AND = {
                        check_variable = {
                            which = blackjack_player_%d_hand_%d
                            value = %d
                        }
                        NOT = {
                            check_variable = {
                                which = blackjack_player_%d_hand_%d
                                value = %d
                            }
                        }
                    }
                    AND = {
                        check_variable = {
                            which = blackjack_player_%d_hand_%d
                            value = %d
                        }
                        NOT = {
                            check_variable = {
                                which = blackjack_player_%d_hand_%d
                                value = %d
                            }
                        }
                    }
                    AND = {
                        check_variable = {
                            which = blackjack_player_%d_hand_%d
                            value = %d
                        }
                        NOT = {
                            check_variable = {
                                which = blackjack_player_%d_hand_%d
                                value = %d
                            }
                        }
                    }
                    AND = {
                        check_variable = {
                            which = blackjack_player_%d_hand_%d
                            value = %d
                        }
                        NOT = {
                            check_variable = {
                                which = blackjack_player_%d_hand_%d
                                value = %d
                            }
                        }
                    }
                }
            }
		}
	}""" % (k, i, j, k, i, j, k+1, i, j, k+13, i, j, k+14, i, j, k+26, i, j, k+27, i, j, k+39, i, j, k+40))

        print("}")


for j in range(1,19):
    print("""defined_text = {
    name = get_b_d_%d""" % j)

    for k in range(1, 14):
        print("""\ttext = {
        localisation_key = debug_card_%d
        trigger = {
            event_target:blackjack_player_1_tag = {
                OR = {
                    AND = {
                        check_variable = {
                            which = blackjack_dealer_hand_%d
                            value = %d
                        }
                        NOT = {
                            check_variable = {
                                which = blackjack_dealer_hand_%d
                                value = %d
                            }
                        }
                    }
                    AND = {
                        check_variable = {
                            which = blackjack_dealer_hand_%d
                            value = %d
                        }
                        NOT = {
                            check_variable = {
                                which = blackjack_dealer_hand_%d
                                value = %d
                            }
                        }
                    }
                    AND = {
                        check_variable = {
                            which = blackjack_dealer_hand_%d
                            value = %d
                        }
                        NOT = {
                            check_variable = {
                                which = blackjack_dealer_hand_%d
                                value = %d
                            }
                        }
                    }
                    AND = {
                        check_variable = {
                            which = blackjack_dealer_hand_%d
                            value = %d
                        }
                        NOT = {
                            check_variable = {
                                which = blackjack_dealer_hand_%d
                                value = %d
                            }
                        }
                    }
                }
            }
        }
    }""" % (k, j, k, j, k+1, j, k+13, j, k+14, j, k+26, j, k+27, j, k+39, j, k+40))

    print("}")
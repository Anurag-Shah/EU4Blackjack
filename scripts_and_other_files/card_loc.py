import os

cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
colors = ["clubs", "diamonds", "hearts", "spades"]

# reverse cause will be going 52 to 1 to simplify checks
cards.reverse()

dir = 'cards_loc'

players = ["dealer", "player_1", "player_2", "player_3", "player_4"]
max_in_hand = 18

for player in players:
    custom_text = "defined_text = {\n" \
                   f"\tname = get_{player}_hand_icons\n" \
                   "\trandom = no\n" \
                   "\ttext = {\n" \
                   f"\t\tlocalisation_key = {player}_hand_icons\n" \
                   "\t\ttrigger = { always = yes }\n" \
                    "\t}\n"\
                    "}\n\n"

    for hand_index in range(1, max_in_hand+1):
        custom_text += "defined_text = {\n" \
                        f"\tname = get_{player}_card_at_{hand_index}\n" \
                        "\trandom = no\n" \
                        "\ttext = {\n" \
                        "\t\tlocalisation_key = no_card\n" \
                        "\t\ttrigger = {\n" \
                        f"\t\t\tNOT = {{ check_variable = {{ blackjack_{player}_hand_{hand_index} = 1 }} }}\n"\
                        "\t\t}\n" \
                        "\t}\n" \
                        "\ttext = {\n" \
                        f"\t\tlocalisation_key = {player}_card_at_{hand_index}_full\n" \
                        "\t\ttrigger = {\n" \
                        f"\t\t\tNOT = {{ check_variable = {{ blackjack_{player}_hand_{hand_index+1} = 1 }} }}\n" \
                       "\t\t}\n" \
                       "\t}\n" \
                        "\ttext = {\n" \
                        f"\t\tlocalisation_key = {player}_card_at_{hand_index}_part\n" \
                        "\t\ttrigger = { always = yes }\n" \
                        "\t}\n" \
                        "}\n\n"

        for part in ['full', 'part']:
            custom_text += "defined_text = {\n" \
                            f"\tname = get_{player}_card_at_{hand_index}_{part}\n"\
                            "\trandom = no\n"

            for color_index, color in enumerate(colors):
                for card_index, card in enumerate(cards):
                    card_value = (3 - color_index) * 13 + (13 - card_index)
                    custom_text += "\ttext = {\n" \
                                   f"\t\tlocalisation_key = icon_{card}_{color}_{part}\n" \
                                   "\t\ttrigger = {\n" \
                                   f"\t\t\tcheck_variable = {{ blackjack_{player}_hand_{hand_index} = {card_value} }}\n" \
                                   "\t\t}\n" \
                                   "\t}\n"
            custom_text += "}\n\n"

        f = open(os.path.join(dir, 'customizable_localization', f'customizable_{player}.txt'), 'w', encoding='cp1252')
        f.write(custom_text)
        f.close()

loc_text = "l_english:\n"\
            ' no_card:0 ""\n'

for color in colors:
    for card in cards:
        loc_text += f' icon_{card}_{color}_full:0 "£icon_{card}_{color}£"\n'
        loc_text += f' icon_{card}_{color}_part:0 "£icon_{card}_{color}_part£"\n'

loc_text += "\n\n\n# Players hands\n"
for player in players:
    loc_text += f' {player}_hand_icons:0 "'
    for hand_index in range(1, max_in_hand+1):
        loc_text += f'[This.get_{player}_card_at_{hand_index}]'
    loc_text += '"\n'
    for hand_index in range(1, max_in_hand+1):
        loc_text += f' {player}_card_at_{hand_index}_full:0 "[This.get_{player}_card_at_{hand_index}_full]"\n'
        loc_text += f' {player}_card_at_{hand_index}_part:0 "[This.get_{player}_card_at_{hand_index}_part]"\n'

f = open(os.path.join(dir, "localisation", "customizable_locs_l_english.yml"), 'w', encoding='utf-8-sig')
f.write(loc_text)
f.close()
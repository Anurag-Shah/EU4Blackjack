stro = '''country_event = {
    id = blackjack_gallery.%s
	title = blackjack_gallery.%s.t
	desc = blackjack_gallery.%s.d
	picture = TRADEGOODS_eventPicture

	is_triggered_only = yes

	option = {
		name = "blackjack_gallery.%sa"
		hidden_effect = {
			country_event = {
				id = blackjack_gallery.%s
			}
		}
	}
	option = {
		name = "blackjack_gallery.%sb"
		hidden_effect = {
			country_event = {
				id = blackjack_gallery.%s
			}
		}
	}
	option = {
\tname = "blackjack_gallery.%sc"
\t\thidden_effect = {
\t\t\tcountry_event = {
\t\t\t\tid = blackjack_gallery.13
\t\t\t}
\t\t}
\t}
}

'''

for i in range(1, 13):
    print(stro % (i, i, i, i, i+1, i, i-1, i))
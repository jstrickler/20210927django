from carddeck import CardDeck, Card

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        for joker_rank in "1", "2":
            card = Card(joker_rank, 'JOKER')
            self._cards.append(card)





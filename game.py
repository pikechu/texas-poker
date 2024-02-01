from random import randint
from .card import ADeckOfCards
from .player import InGamePlayer

class Game(object):
    def __init__(self, players) -> None:
        self.players = players  # [player1, player2 ...]
        self.cards = ADeckOfCards()
        self.public_cards = []  # {card1, card2 ... card5}

        self.dealer = None
        self.dealer_seat = None

    def reset(self):
        for player in self.players:
            player.handcards.clear()
        self.public_cards = []
        self.dealer = None
        self.dealer_seat = None
        self.cards.shuffle()
 
    def start(self):
        assert len(self.players) >= 2 and len(self.players) <= 15
        self.reset()

    def draw_players_card(self):
        for player in self.players:
            self.handcards[player] = [self.cards.draw_one_card() for _ in range(2)]

    def draw_public_card(self):
        for _ in range(5):
            self.public_cards.append(self.cards.draw_one_card())

    def choose_dealer(self):
        if self.dealer is None:
            self.dealer_seat = randint(0, len(self.players - 1))
            self.dealer = self.players[self.dealer_seat]
        else:
            self.find_next_dealer()

    # bug if sit or leave
    def find_next_dealer(self):
        if self.dealer_seat >= len(self.players) - 1:
            self.dealer_seat = 0
        self.dealer = self.players[self.dealer_seat]

    def bet_small_blind(self):
        pass

    def bet_big_blind(self):
        pass


    # pre-flop 

    # flop
    # turn
    # river


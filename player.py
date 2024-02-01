from .lobby import get_table

class PlayerStatus(object):
    STAND = 0
    SIT = 1
    PLAYING = 2

class Player(object):
    def __init__(self, uid: int) -> None:
        self.uid = uid
        self.status = PlayerStatus.STAND
        self.tid = None
        self.chips = 0

    def add_chips(self, chips):
        self.chips += chips

    def buy_in(self, table_chips):
        assert self.chips >= table_chips
        self.chips -= table_chips

    def sit(self, tid):
        self.tid = tid
        self.buy_in(get_table(tid).buy_in)

    def stand(self):
        pass




class InGamePlayer(Player):
    def __init__(self, uid: int) -> None:
        super().__init__(uid)
        self.status = PlayerStatus.PLAYING
        self.handcards = []
        self.table_chips = 0

    def reset(self):
        self.status = PlayerStatus.PLAYING
        self.handcards = []
        self.table_chips = 0

    def draw_one_card(self, card):
        self.handcards.append[card]

    def bet(self):
        pass

    def fold(self):
        pass

    def all_in(self):
        pass



    
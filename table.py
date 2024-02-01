from .player import Player


class TableStatus(object):
    WAIT = 0
    PLAYING = 1

class Table(object):
    def __init__(self, tid: int) -> None:
        self.tid = tid
        self.players = []
        self.status = TableStatus.WAIT
        self.buy_in = 1000


    def join(self, player: Player):
        self.players.append(player)
        print(f'player {player.uid} joined table {self.tid}')

    def exit(self, player: Player):
        del self.players[self.players.find(player.uid)]
        print(f'player {player.uid} exited table {self.tid}')

    

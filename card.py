# 黑红梅方
# 0x11 - 0x1d 黑桃 spade
# 0x21 - 0x2d 红心 heart
# 0x31 - 0x3d 梅花 club
# 0x41 - 0x4d 方片 diamond

import random

# 一张牌
class Card(object):
    def __init__(self, id: int) -> None:
        self.color = int(id / 0x10)  # 0x1-0x4
        self.point = id % (0x10 * self.color)  # 0x1-0xd 

    def __str__(self) -> str:
        return f"color:{self.color},point:{self.point}"
    
    def color_sc(self, color: int) -> str:
        return {
            1: "黑桃",
            2: "红心",
            3: "梅花",
            4: "方块"
        }[color]
    
    def __eq__(self, __value: object) -> bool:
        return self.point == __value.point and self.color == __value.color


# 一副牌
class ADeckOfCards(object):
    def __init__(self) -> None:
        self.cards = []
        self.reset()
        self.index = 0

    def __str__(self) -> str:
        return ";".join([x.__str__() for x in self.cards])
    
    def reset(self) -> None:
        self.cards.clear()
        for c in range(1, 5):
            for p in range(1, 14):
                self.cards.append(Card(0x10 * c + p))
    
    # fisher-yates
    def shuffle(self) -> None:
        self.index = 0
        for i in range(len(self.cards) - 1, -1, -1):
            pos = random.randint(0, i)
            tmp = self.cards[i]
            self.cards[i] = self.cards[pos]
            self.cards[pos] = tmp

    def draw_one_card(self) -> Card:
        self.index += 1
        return self.cards[self.index - 1]

# 组合
class CardCombination(object):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

    def __init__(self, five_cards) -> None:
        assert len(five_cards) == 5
        for card in five_cards:
            assert type(card) == Card
        self.cards = five_cards
    
    def is_flush(self) -> bool:
        for i in range(4):
            if self.cards[i].color != self.cards[i+1].color:
                return False
        return True
    
    def _is_biggest_straight(self) -> bool:
        return [x.point for x in sorted(self.cards, key=lambda x: x.point)] == [0x1, 0xa, 0xb, 0xc, 0xd]
    
    def is_straight(self) -> bool:
        if self._is_biggest_straight():
            return True
        cards = sorted(self.cards, key=lambda x: x.point)
        for i in range(4):
            if cards[i].point != cards[i+1].point - 1:
                return False
        return True
    
    def is_straight_flush(self) -> bool:
        return self.is_flush() and self.is_straight()
    
    def is_royal_flush(self) -> bool:
        return self._is_biggest_straight() and self.is_flush()
    
    def _point_count_list(self) -> dict:
        d = {}
        for card in self.cards:
            if card.point not in d.keys():
                d[card.point] = 1
            else:
                d[card.point] += 1
        return d.values()
    
    def is_one_pair(self) -> bool:
        return len([x for x in self._point_count_list() if x >= 2]) >= 1
    
    def is_two_pair(self) -> bool:
        return len([x for x in self._point_count_list() if x >= 2]) >= 2
    
    def is_three_of_a_kind(self) -> bool:
        return len([x for x in self._point_count_list() if x >= 3]) >= 1
    
    def is_full_house(self) -> bool:
        return self.is_three_of_a_kind() and self.is_two_pair()
    
    def is_four_of_a_kind(self) -> bool:
        return len([x for x in self._point_count_list() if x >= 4]) >= 1
    
    def combination_type(self) -> int:
        if self.is_royal_flush():
            return CardCombination.ROYAL_FLUSH
        if self.is_straight_flush():
            return CardCombination.STRAIGHT_FLUSH
        if self.is_four_of_a_kind():
            return CardCombination.FOUR_OF_A_KIND
        if self.is_full_house():
            return CardCombination.FULL_HOUSE
        if self.is_flush():
            return CardCombination.FLUSH
        if self.is_straight():
            return CardCombination.STRAIGHT
        if self.is_three_of_a_kind():
            return CardCombination.THREE_OF_A_KIND
        if self.is_two_pair():
            return CardCombination.TWO_PAIR
        if self.is_one_pair():
            return CardCombination.ONE_PAIR
        return CardCombination.HIGH_CARD

    def combination_type_str(self) -> str:
        return {
            CardCombination.HIGH_CARD: "HIGH_CARD",
            CardCombination.ONE_PAIR: "ONE_PAIR",
            CardCombination.TWO_PAIR: "TWO_PAIR",
            CardCombination.THREE_OF_A_KIND: "THREE_OF_A_KIND",
            CardCombination.STRAIGHT: "STRAIGHT",
            CardCombination.FLUSH: "FLUSH",
            CardCombination.FULL_HOUSE: "FULL_HOUSE",
            CardCombination.FOUR_OF_A_KIND: "FOUR_OF_A_KIND",
            CardCombination.STRAIGHT_FLUSH: "STRAIGHT_FLUSH",
            CardCombination.ROYAL_FLUSH: "ROYAL_FLUSH"
        }[self.combination_type()]


def compare_two_card(card1, card2):
    if card1.point != card2.point:
        return card1 if card1.point > card2.point else card2
    if card1.color < card2.color:
        return card1
    return card2

if __name__ == '__main__':
    # a = ADeckOfCards()
    # print(a)
    # a.shuffle()
    # print(a)

    cb = CardCombination([Card(x) for x in [0x21, 0x32, 0x43, 0x29, 0x2c]])
    print(cb.combination_type_str())
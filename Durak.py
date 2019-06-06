import random
from collections import namedtuple


Card = namedtuple("Card", ("rank", "suit"))


def print_arr(arr):
    q = 0
    for rest_card in arr:
        q += 1
        print("{0}{1}[{2}] ".format(rest_card.rank, rest_card.suit, q), end='')
    print()


def st_choice(me, comp_card):
    random.shuffle(comp_card)
    for comp in comp_card:
        if comp.rank == me.rank or comp.suit == me.suit:
            return comp
    return False


def check(comp, m_card):
    return any(me.rank == comp.rank or me.suit == comp.suit for me in m_card)


def my_choice(my_card):
    print_arr(my_card)
    print("Выберите номер карты : ", end='')
    while True:
        try:
            usr_input = int(input())
            usr_input -= 1
            if 0 <= usr_input < len(my_card):
                return my_card[usr_input]
            elif len(my_card) == 0:
                return False
            else:
                print("Такой карты нет. Попробуйте другую : ", end='')
        except ValueError:
            print("Неверный ввод, попробуйте ещё раз : ", end='')


def game(comp, comp_card, my_card):
    while True:
        if not check(comp, my_card):
            print("Вы проиграли.")
            break
        while True:
            me = my_choice(my_card)
            if me.rank == comp.rank or me.suit == comp.suit:
                break
            else:
                print("Эта карта не подходит. Попробуйте ещё раз : ")

        print("Вы : {0}{1}".format(me.rank, me.suit))
        comp_card.remove(comp)
        comp = st_choice(me, comp_card)
        if not comp:
            print("Вы выиграли")
            break
        my_card.remove(me)
        print("Противник : {0}{1}".format(comp.rank, comp.suit))


def main():
    my_card = [Card(rank=7, suit='♣'), Card(9, '♣'), Card('J', '♣'), Card('K', '♣'),
               Card(8, '♠'), Card(10, '♠'), Card('Q', '♠'), Card('A', '♠'),
               Card(7, '♥'), Card(9, '♥'), Card('J', '♥'), Card('K', '♥'),
               Card(8, '♦'), Card(10, '♦'), Card('Q', '♦'), Card('A', '♦')]
    comp_card = [Card(7, '♠'), Card(9, '♠'), Card('J', '♠'), Card('K', '♠'),
                 Card(8, '♣'), Card(10, '♣'), Card('Q', '♣'), Card('A', '♣'),
                 Card(7, '♦'), Card(9, '♦'), Card('J', '♦'), Card('K', '♦'),
                 Card(8, '♥'), Card(10, '♥'), Card('Q', '♥'), Card('A', '♥')]

    me = random.choice(my_card)
    comp = st_choice(me, comp_card)
    print("Я : {0}{1}".format(me.rank, me.suit))
    print("Противник : {0}{1}".format(comp.rank, comp.suit))
    my_card.remove(me)
    game(comp, comp_card, my_card)


if __name__ == "__main__":
    main()


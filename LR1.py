import random
from collections import namedtuple


def print_arr(arr):
    q = 0
    for i in arr:
        q += 1
        print("{0}{1}[{2}] ".format(i[0], i[1], q), end='')
    print()


def st_choice(me, comp_card):
    random.shuffle(comp_card)
    for comp in comp_card:
        if comp[0] == me[0] or comp[1] == me[1]:
            return comp
    return False


def check(comp, m_card):
    for me in m_card:
        if me[1] == comp[0] or me[1] == comp[1]:
            return True
    return False


def my_choice(my_card):
    print_arr(my_card)
    print("Выберите номер карты : ", end='')
    while True:
        try:
            a = int(input())
            a -= 1
            if 0 <= a < len(my_card):
                return my_card[a]
            elif len(my_card) == 0:
                return False
            else:
                print("Такой карты нет попробуйте другую : ", end='')
        except ValueError:
            print("Неверный ввод, попробуйте ещё раз : ", end='')


def game(comp, comp_card, my_card):
    while True:
        if not check(comp, my_card):
            print("Вы проиграли.")
            break
        while True:
            me = my_choice(my_card)
            if me[0] == comp[0] or me[1] == comp[1]:
                break
            else:
                print("Эта карта не подходит. Попробуйте ещё раз : ")

        print("Вы : {0}{1}".format(me[0], me[1]))
        comp_card.remove(comp)
        comp = st_choice(me, comp_card)
        if not comp:
            print("Вы выиграли")
            break
        my_card.remove(me)
        print("Противник : {0}{1}".format(comp[0], comp[1]))


def main():
    my_card = [[7, '♣'], [9, '♣'], ['J', '♣'], ['K', '♣'],
               [8, '♠'], [10, '♠'], ['Q', '♠'], ['A', '♠'],
               [7, '♥'], [9, '♥'], ['J', '♥'], ['K', '♥'],
               [8, '♦'], [10, '♦'], ['Q', '♦'], ['A', '♦']]
    comp_card = [[7, '♠'], [9, '♠'], ['J', '♠'], ['K', '♠'],
                 [8, '♣'], [10, '♣'], ['Q', '♣'], ['A', '♣'],
                 [7, '♦'], [9, '♦'], ['J', '♦'], ['K', '♦'],
                 [8, '♥'], [10, '♥'], ['Q', '♥'], ['A', '♥']]

    me = random.choice(my_card)
    comp = st_choice(me, comp_card)
    print("Я : {0}{1}".format(me[0], me[1]))
    print("Противник : {0}{1}".format(comp[0], comp[1]))
    my_card.remove(me)
    game(comp, comp_card, my_card)


if __name__ == "__main__":
    main()

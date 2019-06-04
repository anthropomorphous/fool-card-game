import random
import collections
from collections import namedtuple


def print_arr(arr):
    q = 0
    for i in arr:
        q += 1
        print("{0}{1}[{2}] ".format(i[0], i[1], q), end='')
    print()


def comp_choice(comp_card):
    random.choice(comp_card)
    print("Карта противника : {0}{1}".format(comp_card[0][0], comp_card[0][1]))
    temp = comp_card[0]
    return temp


def st_choice(me, comp_card):
    random.shuffle(comp_card)
    for comp in comp_card:
        if comp[0] == me.rank or comp[1] == me.suit:
            return comp
    return False


def check(comp, m_card):
    for me in m_card:
        if me.rank == comp[0] or me.suit == comp[1]:
            return True
    return False


def my_choice(m_card):
    print_arr(m_card)
    print("Выберите номер карты : ", end='')
    while True:
        try:
            a = int(input())
            a -= 1
            if 0 <= a < len(my_card):
                return m_card[a]
            elif len(m_card) == 0:
                return False
            else:
                print("Такой карты нет попробуйте другую : ", end='')
        except ValueError:
            print("Неверный ввод, попробуйте ещё раз : ", end='')


def main():
    card = namedtuple('card', 'rank suit')
    m_card = card._make([7, '♣'], [9, '♣'], ['J', '♣'])
    comp_card = [[7, '♠'], [9, '♠'], ['J', '♠'], ['K', '♠'],
                 [8, '♣'], [10, '♣'], ['Q', '♣'], ['A', '♣'],
                 [7, '♦'], [9, '♦'], ['J', '♦'], ['K', '♦'],
                 [8, '♥'], [10, '♥'], ['Q', '♥'], ['A', '♥']]
    comp = 0
    choice = input("Хотите ходить первым ?[y/n] : ")
    if choice == 'y':
        me = comp_choice(m_card)
        comp = st_choice(me, comp_card)
        print("Вы : {0}{1}".format(me.rank, me.suit))
        print("Противник : {0}{1}".format(comp[0], comp[1]))
        m_card.remove(me)

    elif choice == 'n':
        comp = comp_choice(comp_card)

    while True:
        if not check(comp, m_card):
            print("Вы проиграли.")
            break
        while True:
            me = my_choice(m_card)
            if me.rank == comp[0] or me.suit == comp[1]:
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

    print("Я: ", end='')
    print_arr(m_card)
    print("Противник : ", end='')
    print_arr(comp_card)


if __name__ == "__main__":
    main()

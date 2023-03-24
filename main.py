#
# Program na Techniki Algorytmiczne
# Kacper Goleń, 72771
# Analiza złożoności algorytmów kolorowania wierzchołków grafu
#

from utils.print_welcoming import print_welcoming
from utils.decision import decision
from routines.routines import routine1, routine2


def main():

    print_welcoming()
    while True:
        d = decision()

        if d[0] == '0':
            break
        elif d[0] == '1':
            routine1(d[1])
        else:
            routine2(d[1])

    print("\n_FIN_\n")


if __name__ == '__main__':
    main()



import time

from utils.parse_data import parse_data
from utils.data_generator import generate_data
from utils.graph_drawing import graph_drawing
from utils.bcolors import bcolors

from algorytmy.algorytm_dokladny import algorytm_dokladny
from algorytmy.algorytm_niedokladny import largest_first
from algorytmy.kolorowanie_checker import sprawdzanie_poprawnosci_kolorowania


def routine1(algorythm):
    print("Wpisz numer:")
    print("\tPodaj liczbę testów: ")

    testy = 0
    wrong_colored = 0
    while True:
        testy = input()
        try:
            testy = int(testy)
        except:
            print(bcolors.FAIL + "Liczba testów musi być liczbą!" + bcolors.ENDC)
            continue
        break

    wierzcholki = []
    krawedzie = []
    while True:
        print("\tPodaj listę liczb wierzchołków: (np: 2,3,4)")
        wierzcholki = input()
        print("\tPodaj listę {} liczb krawędzi: (np: 1,2,6)".format(
            len(wierzcholki)
        ))
        krawedzie = input()

        wierzcholki = wierzcholki.split(',')
        krawedzie = krawedzie.split(',')
        if len(wierzcholki) != len(krawedzie):
            print(bcolors.FAIL + "Błędna liczba danych!" + bcolors.ENDC)
            continue

        data_correct = True

        for i in range(len(wierzcholki)):
            try:
                wierzcholki[i] = int(wierzcholki[i])
                krawedzie[i] = int(krawedzie[i])
            except:
                print(bcolors.FAIL + "Dane muszą być liczbami!" + bcolors.ENDC)
                data_correct = False
                break

            l_wierzcholkow = wierzcholki[i]
            l_krawedzi = krawedzie[i]
            if l_krawedzi > ((l_wierzcholkow*(l_wierzcholkow-1))/2):
                print(bcolors.FAIL + "Liczba krawedzi moze byc maks: n*(n-1) / 2; !" + bcolors.ENDC)
                print(bcolors.FAIL + "Czyli dla {} wierzcholkow, maks krawedzi to {:,.0f}, a nie {} :(".format(
                    l_wierzcholkow, ((l_wierzcholkow*(l_wierzcholkow-1))/2), l_krawedzi
                ) + bcolors.ENDC)
                data_correct = False
                break

        if data_correct:
            break

    wyniki = {}
    for i in range(len(wierzcholki)):
        w = wierzcholki[i]
        k = krawedzie[i]
        wyniki[str(w) + '_' + str(k)] = {}
        wyniki[str(w) + '_' + str(k)]['l_testow'] = 0
        wyniki[str(w) + '_' + str(k)]['czasy'] = []
        wyniki[str(w) + '_' + str(k)]['srednia'] = 0

    # testowanie
    for i in range(int(testy)):
        print("Test: {} z: {}".format(i, testy))
        for j in range(len(wierzcholki)):
            w = wierzcholki[j]
            k = krawedzie[j]
            generated_data = generate_data(w, k)

            st = 0
            et = 0
            if algorythm == '1':
                st = time.time()
                calculated = algorytm_dokladny(
                    generated_data[0],
                    generated_data[1],
                    generated_data[2]
                )
                et = time.time()
                if not sprawdzanie_poprawnosci_kolorowania(generated_data[2], calculated):
                    wrong_colored += 1
                    print(generated_data[0], generated_data[2], calculated)
                    graph_drawing(generated_data[0], generated_data[2], calculated, "Algorytm przybliżony")
            else:
                st = time.time()
                calculated = largest_first(
                    generated_data[0],
                    generated_data[2]
                )
                et = time.time()
                if not sprawdzanie_poprawnosci_kolorowania(generated_data[2], calculated):
                    wrong_colored += 1
                    print(generated_data[0], generated_data[2], calculated)
                    graph_drawing(generated_data[0], generated_data[2], calculated, "Algorytm przybliżony")

            wyniki[str(w) + '_' + str(k)]['l_testow'] += 1
            wyniki[str(w) + '_' + str(k)]['czasy'].append(et-st)
            wyniki[str(w) + '_' + str(k)]['srednia'] += (et-st)

    f = open("results.txt", "w")

    title = "Wyniki testowania:"
    print(title)
    f.write(title + '\n')

    for i in wyniki.keys():
        edges_and_vortexes = "\tWierzcholki: {}, Krawedzie: {}".format(
            int(i.split('_')[0]),
            int(i.split('_')[1])
        )
        print(edges_and_vortexes)
        f.write(edges_and_vortexes + '\n')

        suma_czasow = 0
        if testy > 10:
            print(bcolors.WARNING + "\n\n\tW przypadku dużej liczby testów,\n\tdokładne wyniki "
                                    "zapisywane są wyłącznie w pliku\n\n" + bcolors.ENDC)
            for j in wyniki[i]['czasy']:
                f.write(str(j) + '\n')
                suma_czasow += j
        else:
            print("\t\tCzasy:")
            for j in wyniki[i]['czasy']:
                print("\t\t", j)
                f.write(str(j) + '\n')
                suma_czasow += j
        wyniki[i]['srednia'] = suma_czasow / wyniki[i]['l_testow']
        print("\t\tŚrednia czasów:")
        print("\t\t", wyniki[i]['srednia'])
        f.write("\t\tSrednia czasow:" + '\n')
        f.write(str(wyniki[i]['srednia']) + '\n')

    f.write("ALL SREDNIE:" + '\n')
    for i in wyniki.keys():
        f.write(str(wyniki[i]['srednia']) + '\n')
    f.close()

    if wrong_colored > 0:
        print(bcolors.FAIL + "Błędnie pokolorowane grafy: {}!".format(wrong_colored) + bcolors.ENDC)


def routine2(algorythm):
    parsed_data = parse_data()

    wrong_colored = 0

    for i in parsed_data:
        st = 0
        et = 0
        if algorythm == '1':
            calculated = algorytm_dokladny(
                i[0],
                i[1],
                i[2]
            )

            if not sprawdzanie_poprawnosci_kolorowania(i[2], calculated):
                wrong_colored += 1
                print(i[0], i[2], calculated)
            graph_drawing(i[0], i[2], calculated, "Algorytm dokładny")
        else:
            calculated = largest_first(
                i[0],
                i[2]
            )
            if not sprawdzanie_poprawnosci_kolorowania(i[2], calculated):
                wrong_colored += 1
            graph_drawing(i[0], i[2], calculated, "Algorytm przybliżony")
    if wrong_colored > 0:
        print(bcolors.FAIL + "Błędnie pokolorowane grafy: {}!".format(wrong_colored) + bcolors.ENDC)

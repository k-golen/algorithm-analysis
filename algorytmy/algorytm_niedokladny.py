

def largest_first(w, k):

    stopnie_wierzcholkow = {}
    somsiedzi = {}
    wierzcholki_kolory = {}
    kolory = {}
    zbiory_do_kolorowania = []

    for wierzcholek in w:
        stopnie_wierzcholkow[wierzcholek] = 0
        somsiedzi[wierzcholek] = set()
        wierzcholki_kolory[wierzcholek] = -1
        kolory[wierzcholek] = 0
        #zbiory_do_kolorowania.append(set())

    for wierzcholki in k:
        stopnie_wierzcholkow[wierzcholki[0]] += 1
        stopnie_wierzcholkow[wierzcholki[1]] += 1
        somsiedzi[wierzcholki[0]].add(wierzcholki[1])
        somsiedzi[wierzcholki[1]].add(wierzcholki[0])

    w = [k for k, v in sorted(stopnie_wierzcholkow.items(), key=lambda item: item[1], reverse=True)]

    for wierzcholek in w:
        kolory_tmp = dict(kolory)
        # sprawdzenie kolorow somsiadow
        for s in somsiedzi[wierzcholek]:
            # jesli jest rozny niz -1, oznacz 1 jako uzyty
            if wierzcholki_kolory[s] != -1:
                kolory_tmp[wierzcholki_kolory[s]] = 1
        # przejscie po kolorach
        for i in range(len(kolory_tmp)):
            # jesli jakis jest dostepny to go wybierz
            if kolory_tmp[i] == 0:
                wierzcholki_kolory[wierzcholek] = i
                if i >= len(zbiory_do_kolorowania):
                    zbiory_do_kolorowania.append(set())
                zbiory_do_kolorowania[i].add(wierzcholek)
                break

    return zbiory_do_kolorowania

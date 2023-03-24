from utils.my_to_dnf import convert_to_dnf


def algorytm_dokladny(w, sw, k):
    if len(k) == 0:
        return [set(w)]

    # 1.1 utworzenie WAK na podstawie dostarczonych krawedzi
    # k
    WAK = ""
    for krawedz in k:
        WAK += "(" + sw[krawedz[0]] + "|" + sw[krawedz[1]] + ")" + "&"
    WAK = WAK[:-1]
    suma = len(k)
    # 1.2 przeksztalcenie WAK do mfa, bazy minimalne
    # worst case: 2^k * 2^k
    # size: 2^k
    my_sorted_bazy_minimalne = convert_to_dnf(WAK)
    suma += my_sorted_bazy_minimalne[1]
    my_sorted_bazy_minimalne = my_sorted_bazy_minimalne[0]

    # worst case: 2^k - k
    if len(sw) < len(my_sorted_bazy_minimalne):
        # 10, 14
        len_sw = len(sw)
        for i in range(len(my_sorted_bazy_minimalne) - len_sw):
            sw[len_sw + i] = str(len_sw + i).zfill(8)
    suma += len(my_sorted_bazy_minimalne)
    # 1.3 utworzenie maks zbiorow wew stabilnych na podstawie baz minimalnych
    # worst case: 2^k
    wierzcholki_w_all_zb_wew_stab = {}
    for i in range(len(my_sorted_bazy_minimalne)):
        letter = sw[i]
        wierzcholki_w_all_zb_wew_stab[letter] = ""
    suma += len(my_sorted_bazy_minimalne)
    zbiory_wew_stabilnie_wak = ""
    # opisuja w ktorej bazie minimalnej nie ma wierzcholka

    # 1.3 c.d. oraz 3 - utworzenie WAK na podstawie maks zbiorow wew stab
    # worst case: w * 2^k
    for wierzcholek in w:
        zbior_wew_stabilny_WAK = ""
        for i in range(len(my_sorted_bazy_minimalne)):
            if sw[wierzcholek] not in my_sorted_bazy_minimalne[i]:
                zbior_wew_stabilny_WAK += sw[i] + "|"
                wierzcholki_w_all_zb_wew_stab[sw[i]] += sw[wierzcholek]
        zbiory_wew_stabilnie_wak += "(" + zbior_wew_stabilny_WAK[:-1] + ")&"

    suma += len(w) * len(my_sorted_bazy_minimalne)
    zbiory_wew_stabilnie_wak = zbiory_wew_stabilnie_wak[:-1]

    # 4 przkesztalcenie WAK do mfa
    my_mfa = convert_to_dnf(zbiory_wew_stabilnie_wak, True)

    suma += my_mfa[1]
    my_mfa = my_mfa[0]
    # 5 wbranie najkrotszy iloczyn
    najkrotszy_iloczyn = my_mfa[0]
    zbiory_zbiorow_wew_stab = najkrotszy_iloczyn.split("&")

    pokolorowane = set()
    zbiory_do_kolorowania = []

    # 6 tworzenie "rodzin" i tworzenie zbiorow tych rodzin w <zbiory_do_kolorowania>
    index = 0
    for z in range(len(zbiory_zbiorow_wew_stab)):
        zbiory_do_kolorowania.append(set())
        a = zbiory_zbiorow_wew_stab[z]
        b = wierzcholki_w_all_zb_wew_stab[a]
        for i in range(0, len(wierzcholki_w_all_zb_wew_stab[zbiory_zbiorow_wew_stab[z]]), 8):
            index += 1
            zbior_wew_stab = wierzcholki_w_all_zb_wew_stab[zbiory_zbiorow_wew_stab[z]][i:i+8]
            wierzcholek = list(sw.values()).index(zbior_wew_stab)
            if wierzcholek not in pokolorowane:
                zbiory_do_kolorowania[z].add(wierzcholek)
            pokolorowane.add(wierzcholek)
            if len(pokolorowane) == len(w):
                z = len(zbiory_zbiorow_wew_stab)
                break

    suma += index
    return zbiory_do_kolorowania

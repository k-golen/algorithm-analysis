def sprawdzanie_poprawnosci_kolorowania(krawedzie, pokolorowanie):
    # jesli wierzcholki w jednej krawedzi sa w tym samym zbiorze
    # oznacza to ze maja ten sam kolor i sa blednie pokolorowane
    for k in krawedzie:
        for zbior in pokolorowanie:
            if k[0] in zbior:
                if k[1] in zbior:
                    return False
    return True

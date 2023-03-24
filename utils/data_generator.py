from random import randrange


def generate_data(w, k):
    generated_data = []

    liczba_wierzcholkow = w
    liczba_krawedzi = k

    wierzcholki_lista = [i for i in range(liczba_wierzcholkow)]
    slownik_wierzcholkow = {}

    for w in wierzcholki_lista:
        slownik_wierzcholkow[w] = str(w).zfill(8)

    generated_edges = []

    for i in range(liczba_wierzcholkow):
        for j in range(i + 1, liczba_wierzcholkow):
            generated_edges.append((i, j))

    while len(generated_edges) > liczba_krawedzi:
        generated_edges.pop(randrange(len(generated_edges)))

    generated_edges.sort(key=lambda tup: (tup[0], tup[1]))
    generated_data.append(wierzcholki_lista)
    generated_data.append(slownik_wierzcholkow)
    generated_data.append(generated_edges)
    return generated_data

import os
from dotenv import load_dotenv


def parse_data():
    load_dotenv()
    files = os.listdir(os.environ["input_files_directory"])
    parsed_data = []

    for j in range(1):
        for i in files:
            f = open(os.environ["input_files_directory"] + '\\' + i, 'r')

            number_of_elements = f.readline().split(' ')

            wierzcholki = [i for i in range(int(number_of_elements[0]))]
            krawedzie = []

            slownik_wierzcholkow = {}
            for w in wierzcholki:
                slownik_wierzcholkow[w] = str(w).zfill(8)

            for line in f:
                u = line.split(' ')
                for k in range(0, len(u), 2):
                    t = (int(u[k]), int(u[k+1]))
                    krawedzie.append(t)

            parsed_data.append([wierzcholki, slownik_wierzcholkow, krawedzie])

    return parsed_data


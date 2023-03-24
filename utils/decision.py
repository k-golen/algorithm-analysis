import os
from utils.bcolors import bcolors
from dotenv import load_dotenv


def decision():

    load_dotenv()
    decyzje = '01'
    print("Wpisz numer:")
    print("\t0. Zakończenie pracy")
    print("\t1. Generowanie danych i testowanie")
    if os.listdir(os.environ["input_files_directory"]):
        print("\t2. Kolorowanie wierzchołków grafu z danych z plików")
        decyzje += '2'
    else:
        print("\t( brak plików z danymi wejściowymi )")

    results = []

    while True:
        decyzja = input()
        if decyzja not in decyzje:
            print(bcolors.FAIL + "Wprowadz poprawną wartość!" + bcolors.ENDC)
            continue
        break
    results.append(decyzja)

    if decyzja == '0':
        return results

    decyzje = '12'
    print("Który algorytm wykorzystać:")
    print("\t1. Dokładny")
    print("\t2. Heurystyczny")

    while True:
        decyzja = input()
        if decyzja not in decyzje:
            print(bcolors.FAIL + "Wprowadz poprawną wartość!" + bcolors.ENDC)
            continue
        break

    results.append(decyzja)

    return results

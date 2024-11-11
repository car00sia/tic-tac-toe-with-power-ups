import random
liczba_wierszy = int(input("Podaj ilosc wierszy: "))
liczba_kolumn = int(input("Podaj ilosc kolumn: "))
plansza = [[" " for j in range(liczba_kolumn)] for i in range(liczba_wierszy)]
liczba_poweruppow = liczba_kolumn*liczba_wierszy//3

def wydrukuj_plansze(plansza):
    for i in range(len(plansza)):
        print(" | ".join(plansza[i]))

def czy_wygrana(plansza, znak):
    for i in range(liczba_wierszy):
        licznik3 = 0
        for j in range(liczba_kolumn):
            if plansza[i][j] == znak:
                licznik3 += 1
        if licznik3 == liczba_kolumn:
            return True

    for j in range(liczba_kolumn):
        licznik2 = 0
        for i in range(liczba_wierszy):
            if plansza[i][j] == znak:
                licznik2 += 1
        if licznik2 == liczba_wierszy:
            return True

    licznik1 = 0
    for i in range(min(liczba_wierszy, liczba_kolumn)):
        if plansza[i][i] == znak:
            licznik1 += 1
    if licznik1 == min(liczba_wierszy, liczba_kolumn):
        return True

    licznik4 = 0
    for i in range(min(liczba_wierszy, liczba_kolumn)):
        if plansza[i][liczba_kolumn - i - 1] == znak:
            licznik4 += 1
    if licznik4 == min(liczba_wierszy, liczba_kolumn):
        return True

    return False

def poweruppy(plansza, plansza_powerup, wiersz, kolumna, znak):
    print(plansza_powerup[wiersz][kolumna], "powerup")
    if 'ponowienie' == plansza_powerup[wiersz][kolumna]:
        print('Na tym polu jest powerupp - Masz mozliwosc wykonania kolejnego ruchu.')

        while plansza[wiersz][kolumna] in ["x", "o"]:
            wiersz = int(input("Podaj, ktory wiersz:")) - 1
            kolumna = int(input("Podaj ktora kolumna:")) - 1

        plansza[wiersz][kolumna] = znak
        if czy_wygrana(plansza, znak):
                print(znak," wygral")
                exit()
        plansza_powerup[wiersz][kolumna] = ''

    if 'dodanie' == plansza_powerup[wiersz][kolumna]:
        plansza_powerup[wiersz][kolumna] = ''
        print('Na tym polu jest powerupp - Na twojej planszy zostal dodany kolejny znak')

        while True:
            wiersz2 = random.randint(0, liczba_wierszy - 1)
            kolumna2 = random.randint(0, liczba_kolumn - 1)
            if plansza[wiersz2][kolumna2] not in ["x", "o"]:
                plansza[wiersz2][kolumna2] = znak
                break

    if 'zamienianie' == plansza_powerup[wiersz][kolumna]:
        plansza_powerup[wiersz][kolumna] = ''
        print('Na tym polu jest powerupp - Masz mozliwosc zamienienia znaku przeciwnika na swoj.')
        while b == 0:
            wiersz3 = input("Podaj wiersz na ktorym przeciwnik postawil swoj znak")
            kolumna3 = input("Podaj kolumne na ktorej przeciwnik postawil swoj znak")
            if plansza[wiersz3][kolumna3] == znak:
                print("Podaj wspolrzedne na ktorych przeciwnik postawil swoj znak")
            else:
                b = 1
                plansza[wiersz3][kolumna3] = znak
        wydrukuj_plansze(plansza)

def zapelnij_plansze(plansza, liczba_poweruppow, liczba_wierszy, liczba_kolumn):
    lista_poweruppow= ['ponowienie', 'dodanie', 'zamienianie']
    plansza_powerup = [[" " for j in range(liczba_kolumn)] for i in range(liczba_wierszy)]
    for i in range(liczba_poweruppow):
        wiersz1 = random.randint(0, liczba_wierszy - 1)
        kolumna1 = random.randint(0, liczba_kolumn - 1)
        while plansza_powerup[wiersz1][kolumna1] != " ":
            wiersz1 = random.randint(0, liczba_wierszy - 1)
            kolumna1 = random.randint(0, liczba_kolumn - 1)
        plansza_powerup[wiersz1][kolumna1] = random.choice(lista_poweruppow)
    licznik = 0

    while licznik != liczba_wierszy * liczba_kolumn:
        wiersz = int(input("Podaj, ktory wiersz:")) - 1
        kolumna = int(input("Podaj ktora kolumna:")) - 1
        if plansza[wiersz][kolumna] not in ["x", "o"]:
            if licznik % 2 == 1:
                plansza[wiersz][kolumna] = "o"
                if czy_wygrana(plansza, "o"):
                    print("Kolko wygralo")
                    break
                wydrukuj_plansze(plansza)
                poweruppy(plansza, plansza_powerup, wiersz, kolumna, "o")
            else:
                plansza[wiersz][kolumna] = "x"
                if czy_wygrana(plansza, "x"):
                    print("X wygrywaja")
                    break
                wydrukuj_plansze(plansza)
                poweruppy(plansza, plansza_powerup, wiersz, kolumna, "x")
            licznik += 1





wydrukuj_plansze(plansza)
zapelnij_plansze(plansza, liczba_poweruppow, liczba_wierszy, liczba_kolumn)

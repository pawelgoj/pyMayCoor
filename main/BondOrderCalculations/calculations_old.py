
import numpy as np


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def percent(s, suma):
    x = 0.0
    x = (s/suma)*100
    return x

# Liczenie walencyjnosci


def Walencyjnosc_kowa(s, poczatek, koniec):
    if poczatek != -1 and koniec != -1:
        tablica = []
        tablica2 = []
        tablicamuliken = []
        tablicawalencyjnosccalkowita = []
        jonowoscawa = []
        i = 0
        VC = 0
        for kolumna in range(poczatek, (koniec + 1)):
            wal = 0
            i = i + 1
            for wiersz in range(0, j):
                wal = wal + Tabelarzadwiazania[wiersz][kolumna]
            tablica.append(kolumna + 1)
            tablica2.append(round(wal, 5))
        for wiersz in range(poczatek, (koniec + 1)):
            wrrr = ladunekmulikena[wiersz]
            tablicamuliken.append(round(wrrr, 5))
        for x in range(0, i):
            a = tablica2[x]
            b = tablicamuliken[x]
            VC = round((0.5)*(a+(((a**2)+(4*(b**2)))**0.5)), 3)
            tablicawalencyjnosccalkowita.append(VC)
            c = round(abs(b)/(abs(b)+a), 3)
            jonowoscawa.append(c)

        print('Walencyjnosc')
        print("Walencyjnosc nie calkowita -tzw. kowalencyjnosc calkowita(Cov), ładunek mulikena (Mul), Walencyjnosc calkowita wedlug: Evarestov'a i Veryazov'a (Val), jonowosc (ion)")
        print()
        print("           Cov    Mul   Val    Ion")
        for x in range(0, i):
            print(tablica[x], " ", s, ":    ", tablica2[x], "  ", tablicamuliken[x],
                  "  ", tablicawalencyjnosccalkowita[x], "  ", jonowoscawa[x], sep='')



# Funkcja koordynacja I JEDNOSTKI Q


def koordynacja(poczatek, koniec, poczatek2, koniec2, promienodciecia, s):
    if poczatek != -1 and koniec != -1 and poczatek2 != -1 and koniec2 != -1:
        tablica = []
        tablica2 = []
        Tabelarzadwiazaniaxy = np.zeros(shape=(j, 20))
        idtlenu = np.zeros(shape=(j, 20), dtype=int)
        wiersz2 = 0
        if poczatek != -1 and koniec != -1:
            for kolumna in range(poczatek, (koniec + 1)):
                i = 0
                x = 0
                Q = 0
                for wiersz in range(poczatek2, koniec2 + 1):
                    if Tabelarzadwiazania[wiersz][kolumna] > promienodciecia:
                        i += 1
                        Tabelarzadwiazaniaxy[wiersz2][i] = Tabelarzadwiazania[wiersz][kolumna]
                        idtlenu[wiersz2][i] = wiersz + 1
                        if poczatek == poczatekP and koniec == koniecP and poczatek2 == poczatekO and koniec2 == koniecO:
                            if tablicaOP[x] >= 2:
                                Q += 1
                    x += 1
                tablica.append(i)
                tablica2.append(Q)
                wiersz2 += 1

        print(s)
        print()
        ilosc0 = 0
        ilosc1 = 0
        ilosc2 = 0
        ilosc3 = 0
        ilosc4 = 0
        ilosc5 = 0
        ilosc6 = 0
        ilosc7 = 0
        ilosc8 = 0
        ilosc9 = 0
        Q0 = 0
        Q1 = 0
        Q2 = 0
        Q3 = 0
        Q4 = 0

        if poczatek != -1 and koniec != -1:
            for x in range(0, koniec - poczatek + 1):

                if poczatek == poczatekP and koniec == koniecP and poczatek2 == poczatekO and koniec2 == koniecO:
                    print("idP", "coord", "Qi")
                    print(poczatek + 1 + x,
                          tablica[x], tablica2[x], sep='    ')
                else:
                    print(poczatek + 1 + x, tablica[x], sep='    ')
                print("idO: Rzad wiazania", end="   ")
                for y in range(0, 9):
                    if Tabelarzadwiazaniaxy[x][y] > 0:
                        print(idtlenu[x][y], ":", " ",
                              Tabelarzadwiazaniaxy[x][y], sep='', end="  ")
                print()
                print()
                if tablica[x] == 0:
                    ilosc0 += 1
                if tablica[x] == 1:
                    ilosc1 += 1
                if tablica[x] == 2:
                    ilosc2 += 1
                if tablica[x] == 3:
                    ilosc3 += 1
                if tablica[x] == 4:
                    ilosc4 += 1
                if tablica[x] == 5:
                    ilosc5 += 1
                if tablica[x] == 6:
                    ilosc6 += 1
                if tablica[x] == 7:
                    ilosc7 += 1
                if tablica[x] == 8:
                    ilosc8 += 1
                if tablica[x] > 8:
                    ilosc9 += 1
                if poczatek == poczatekP and koniec == koniecP:
                    if tablica2[x] == 0:
                        Q0 += 1
                    if tablica2[x] == 1:
                        Q1 += 1
                    if tablica2[x] == 2:
                        Q2 += 1
                    if tablica2[x] == 3:
                        Q3 += 1
                    if tablica2[x] == 4:
                        Q4 += 1

        ilosc0 = round((ilosc0/(koniec + 1 - poczatek))*100, 5)
        ilosc1 = round((ilosc1/(koniec + 1 - poczatek))*100, 5)
        ilosc2 = round((ilosc2/(koniec + 1 - poczatek))*100, 5)
        ilosc3 = round((ilosc3/(koniec + 1 - poczatek))*100, 5)
        ilosc4 = round((ilosc4/(koniec + 1 - poczatek))*100, 5)
        ilosc5 = round((ilosc5/(koniec + 1 - poczatek))*100, 5)
        ilosc6 = round((ilosc6/(koniec + 1 - poczatek))*100, 5)
        ilosc7 = round((ilosc7/(koniec + 1 - poczatek))*100, 5)
        ilosc8 = round((ilosc8/(koniec + 1 - poczatek))*100, 5)
        ilosc9 = round((ilosc9/(koniec + 1 - poczatek))*100, 5)

        if poczatek == poczatekP and koniec == koniecP:
            suma = Q1 + Q2 + Q3 + Q4 + Q0

            Q0 = round(percent(Q0, suma), 5)
            Q1 = round(percent(Q1, suma), 5)
            Q2 = round(percent(Q2, suma), 5)
            Q3 = round(percent(Q3, suma), 5)
            Q4 = round(percent(Q4, suma), 5)

        print()
        print("koordynacja, procent")
        print()

        if ilosc0 > 0:
            print("0:", ilosc0)
        if ilosc1 > 0:
            print("1:", ilosc1)
        if ilosc2 > 0:
            print("2:", ilosc2)
        if ilosc3 > 0:
            print("3:", ilosc3)
        if ilosc4 > 0:
            print("4:", ilosc4)
        if ilosc5 > 0:
            print("5:", ilosc5)
        if ilosc6 > 0:
            print("6:", ilosc6)
        if ilosc7 > 0:
            print("7:", ilosc7)
        if ilosc8 > 0:
            print("8:", ilosc8)
        if ilosc9 > 0:
            print(">8:", ilosc9)

        if poczatek == poczatekP and koniec == koniecP and poczatek2 == poczatekO and koniec2 == koniecO:
            print()
            print("Jednostki Qi")
            print()
            print("Q0:", Q0)
            print("Q1:", Q1)
            print("Q2:", Q2)
            print("Q3:", Q3)
            print("Q4:", Q4)
            print()

# Rząd wiazania od długosci wiazania


def rzadwiazania_dlugoscwiazania(nazwa1, nazwa2, promien_od_rzad_wiazania, poczatek, koniec, poczatek2, koniec2):
    if poczatek != -1 and koniec != -1 and poczatek2 != -1 and koniec2 != -1:
        dlugosc = 0
        print()
        print()
        print("id", nazwa1, "id", nazwa2,
              "dlugosc wiazania [A], rzadwiazania, połączenia do tlenu: P-O, P=O, Fe-O, Al-O ")
        print()
        iloscPOP = 0
        iloscPO = 0

        iloscPOFe = 0
        iloscPOFe2 = 0
        iloscPOFeAl = 0
        iloscPOFeAl2 = 0
        iloscPOFe2Al = 0
        iloscPOAl = 0
        iloscPOAl2 = 0

        iloscFeOFe = 0
        iloscAlOAl = 0
        iloscAlO2Al = 0
        iloscFeO2Fe = 0
        iloscAlFe = 0
        iloscAl2Fe = 0
        iloscFe2Al = 0

        for x in range(0, j):
            if Symbolpierwiastka[x] == nazwa1:
                kolumna = -1
                for y in range(0, (27*j)):
                    kolumna = Nr[y]
                    if indeksko[y] == nazwa2:
                        if Tabelarzadwiazania[x][kolumna] > promien_od_rzad_wiazania:
                            dlugosc = (
                                (kor2X[y]-korX[x])**2+(kor2Y[y]-korY[x])**2+(kor2Z[y]-korZ[x])**2)**0.5
                            if dlugosc < 8 and nazwa2 == 'O':
                                print(x + 1, kolumna + 1, '   ', round(dlugosc, 4), Tabelarzadwiazania[x][kolumna], '   ', tablicaOP[kolumna -
                                      poczatekO], tablicaOP2[kolumna - poczatekO], tablicaFe[kolumna - poczatekO], tablicaAl[kolumna - poczatekO],)
                                if tablicaOP[kolumna - poczatekO] == 2:
                                    iloscPOP = iloscPOP + 1
                                if tablicaOP[kolumna - poczatekO] == 1:
                                    if tablicaFe[kolumna - poczatekO] == 0 and tablicaAl[kolumna - poczatekO] == 0:
                                        iloscPO += 1
                                    if tablicaFe[kolumna - poczatekO] == 1 and tablicaAl[kolumna - poczatekO] == 0:
                                        iloscPOFe += 1
                                    if tablicaFe[kolumna - poczatekO] == 2 and tablicaAl[kolumna - poczatekO] == 0:
                                        iloscPOFe2 += 1
                                    if tablicaFe[kolumna - poczatekO] == 0 and tablicaAl[kolumna - poczatekO] == 1:
                                        iloscPOAl += 1
                                    if tablicaFe[kolumna - poczatekO] == 0 and tablicaAl[kolumna - poczatekO] == 2:
                                        iloscPOAl2 += 1
                                    if tablicaFe[kolumna - poczatekO] == 1 and tablicaAl[kolumna - poczatekO] == 1:
                                        iloscPOFeAl += 1
                                    if tablicaFe[kolumna - poczatekO] == 2 and tablicaAl[kolumna - poczatekO] == 1:
                                        iloscPOFe2Al += 1
                                    if tablicaFe[kolumna - poczatekO] == 1 and tablicaAl[kolumna - poczatekO] == 2:
                                        iloscPOFeAl2 += 1
                                if tablicaOP[kolumna - poczatekO] == 0:

                                    if tablicaFe[kolumna - poczatekO] == 2 and tablicaAl[kolumna - poczatekO] == 0:
                                        iloscFeOFe += 1
                                    if tablicaFe[kolumna - poczatekO] == 0 and tablicaAl[kolumna - poczatekO] == 2:
                                        iloscAlOAl += 1
                                    if tablicaFe[kolumna - poczatekO] == 3 and tablicaAl[kolumna - poczatekO] == 0:
                                        iloscFeO2Fe += 1
                                    if tablicaFe[kolumna - poczatekO] == 0 and tablicaAl[kolumna - poczatekO] == 3:
                                        iloscAlO2Al += 1
                                    if tablicaFe[kolumna - poczatekO] == 1 and tablicaAl[kolumna - poczatekO] == 1:
                                        iloscAlFe += 1
                                    if tablicaFe[kolumna - poczatekO] == 2 and tablicaAl[kolumna - poczatekO] == 1:
                                        iloscFe2Al += 1
                                    if tablicaFe[kolumna - poczatekO] == 1 and tablicaAl[kolumna - poczatekO] == 2:
                                        iloscAl2Fe += 1

                            elif dlugosc < 8:
                                print(x + 1, kolumna + 1, '   ', round(dlugosc,
                                      4), Tabelarzadwiazania[x][kolumna])
        print()
        print()
        print("ilosc wiazan z tlenem: ", nazwa1, "-O ",  "dla połaczeń:")
        if iloscPOP > 0:
            print("P-O-P:", iloscPOP)

        if iloscPO > 0:
            print("P=O:", iloscPO)
        if iloscPOFe > 0:
            print("P-O-Fe:", iloscPOFe)
        if iloscPOFe2 > 0:
            print("P-O-2Fe:", iloscPOFe2)
        if iloscFeOFe > 0:
            print("Fe-O-Fe:", iloscFeOFe)
        if iloscFeO2Fe > 0:
            print("Fe-O-2Fe:", iloscFeO2Fe)
        if iloscPOAl > 0:
            print("P-O-Al:", iloscPOAl)
        if iloscPOAl2 > 0:
            print("P-O-2Al:", iloscPOAl2)
        if iloscAlOAl > 0:
            print("Al-O-Al:", iloscAlOAl)
        if iloscAlO2Al > 0:
            print("Al-O-2Al:", iloscAlO2Al)
        if iloscAlFe > 0:
            print("Fe-O-Al:", iloscAlFe)
        if iloscAl2Fe > 0:
            print("Fe-O-2Al:", iloscAl2Fe)
        if iloscFe2Al > 0:
            print("2Fe-O-Al:", iloscFe2Al)
        print()
        print()

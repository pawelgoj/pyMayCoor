
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

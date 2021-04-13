# -*- coding: utf-8 -*-

#importowanie numpy
import numpy as np
#
#
#
#FUNKCJE
#
#funkcja sprawdza czy symbol jest numerem   
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
#funkcja procent 
def procent(s, suma):
   x = 0.0
   x = (s/suma)*100
   return x

#Liczenie walencyjnosci 
def Walencyjnosc_kowa(s, poczatek, koniec): 
    if poczatek != -1 and koniec != -1:
        tablica=[]
        tablica2=[]
        tablicamuliken =[]
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
        for wiersz in range(poczatek, (koniec +1)):
            wrrr=ladunekmulikena[wiersz]
            tablicamuliken.append(round(wrrr, 5))
        for x in range(0, i): 
            a = tablica2[x]
            b = tablicamuliken[x]
            VC = round((0.5)*(a+(((a**2)+(4*(b**2)))**0.5)), 3)
            tablicawalencyjnosccalkowita.append(VC)
            c = round(abs(b)/(abs(b)+a),3)
            jonowoscawa.append(c)
            
        print('Walencyjnosc')
        print("Walencyjnosc nie calkowita -tzw. kowalencyjnosc calkowita(Cov), ładunek mulikena (Mul), Walencyjnosc calkowita wedlug: Evarestov'a i Veryazov'a (Val), jonowosc (ion)")
        print() 
        print("           Cov    Mul   Val    Ion")
        for x in range(0, i):
            print(tablica[x], " ", s, ":    ", tablica2[x], "  ", tablicamuliken[x], "  ", tablicawalencyjnosccalkowita[x], "  ", jonowoscawa[x], sep='')


#funkcja drukuj wartosc min-max 
def min_max(s, maximum1, minimum1, maximum2, minimum2):
    if maximum1 != -10 or minimum1 != -10 or maximum2 != -10 or minimum2 != -10:
        print()
        print("Maksymalny rzad wiazania ", s, ": ", Tabelarzadwiazania[maximum1][maximum2], sep='')
        print("Minimalny rzad wiazania ", s, ": ", Tabelarzadwiazania[minimum1][minimum2], sep='')
        print()
        
#Przedział histogram
def drukuj_przedzial(s, przedzial):
    if przedzial != 0:
        print("przedział histogram ", s, ": ", przedzial, sep='')

#funkcja histogram
def histogram(ilosckolumnhh, przedzialh, poczatek1, koniec1, poczatek2, koniec2, dolnagranica, gornagranica, minimumid1, minimumid2, nazwa):
    if przedzialh != 0:
        tablicailoscrzedowpo = []
        for x in range(0, ilosckolumnh):
            i = 0
            for wiersz in range(poczatek1, koniec1 + 1):
                for kolumna in range(poczatek2, koniec2 + 1):
                    if Tabelarzadwiazania[wiersz][kolumna] <= gornagranica and Tabelarzadwiazania[wiersz][kolumna] > dolnagranica:
                        i+=1
            tablicailoscrzedowpo.append(i)
            dolnagranica = gornagranica
            gornagranica += przedzialh
        
        gornagranica = Tabelarzadwiazania[minimumid1][minimumid2] + (przedzialh / 2)
    
        print(nazwa)
        print()
        print("przedzaiał/2 ilosc")
        for x in range(0, ilosckolumnh):
            print(gornagranica, tablicailoscrzedowpo[x])
            gornagranica += przedzialh
        
        print()
        print()

#Funkcja koordynacja I JEDNOSTKI Q 
def koordynacja(poczatek, koniec, poczatek2, koniec2, promienodciecia, s):
    if poczatek != -1 and koniec != -1 and poczatek2 != -1 and koniec2 != -1: 
        tablica = []
        tablica2 = []
        Tabelarzadwiazaniaxy = np.zeros(shape=(j, 20))
        idtlenu = np.zeros(shape=(j, 20), dtype=int)
        wiersz2 = 0
        if poczatek != -1 and koniec !=-1:
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
        
        if poczatek != -1 and koniec !=-1:
            for x in range(0, koniec - poczatek + 1):
                
                if poczatek == poczatekP and koniec == koniecP and poczatek2 == poczatekO and koniec2 == koniecO:
                    print("idP", "coord", "Qi")
                    print (poczatek + 1 + x, tablica[x], tablica2[x], sep='    ') 
                else:
                    print (poczatek + 1 + x, tablica[x], sep='    ')
                print("idO: Rzad wiazania", end="   ")
                for y in range(0, 9):
                    if Tabelarzadwiazaniaxy[x][y] > 0:
                        print(idtlenu[x][y], ":", " ", Tabelarzadwiazaniaxy[x][y], sep='', end ="  ")
                print()
                print()
                if tablica[x] == 0: 
                    ilosc0 +=1 
                if tablica[x] == 1:
                    ilosc1 +=1
                if tablica[x] == 2:
                    ilosc2 +=1
                if tablica[x] == 3:
                    ilosc3 +=1
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
                        Q0 +=1 
                    if tablica2[x] == 1:
                        Q1 +=1
                    if tablica2[x] == 2:
                        Q2 +=1
                    if tablica2[x] == 3:
                        Q3 +=1
                    if tablica2[x] == 4:
                        Q4 += 1    
    
        ilosc0 = round((ilosc0/(koniec + 1 - poczatek))*100,5)
        ilosc1 = round((ilosc1/(koniec + 1 - poczatek))*100,5)
        ilosc2 = round((ilosc2/(koniec + 1 - poczatek))*100,5)
        ilosc3 = round((ilosc3/(koniec + 1- poczatek))*100,5)
        ilosc4 = round((ilosc4/(koniec + 1- poczatek))*100,5)
        ilosc5 = round((ilosc5/(koniec + 1- poczatek))*100,5)
        ilosc6 = round((ilosc6/(koniec + 1- poczatek))*100,5)
        ilosc7 = round((ilosc7/(koniec + 1- poczatek))*100,5)
        ilosc8 = round((ilosc8/(koniec + 1- poczatek))*100,5)
        ilosc9 = round((ilosc9/(koniec + 1- poczatek))*100,5)
        
        if poczatek == poczatekP and koniec == koniecP:
            suma = Q1 + Q2 + Q3 + Q4 + Q0
            
            Q0 = round(procent(Q0, suma),5)
            Q1 = round(procent(Q1, suma),5)
            Q2 = round(procent(Q2, suma),5) 
            Q3 = round(procent(Q3, suma),5)
            Q4 = round(procent(Q4, suma),5) 
    
        print ()
        print ("koordynacja, procent")
        print ()
    
        if ilosc0 > 0:
            print ("0:", ilosc0)
        if ilosc1 > 0:
            print ("1:", ilosc1) 
        if ilosc2 > 0:
            print ("2:", ilosc2)
        if ilosc3 > 0:
            print ("3:", ilosc3)
        if ilosc4 > 0:
            print ("4:", ilosc4)
        if ilosc5 > 0:
            print ("5:", ilosc5)
        if ilosc6 > 0:
            print ("6:", ilosc6)
        if ilosc7 > 0:
            print ("7:", ilosc7)
        if ilosc8 > 0:
            print ("8:", ilosc8)
        if ilosc9 > 0:
            print (">8:", ilosc9)
            
        if poczatek == poczatekP and koniec == koniecP and poczatek2 == poczatekO and koniec2 == koniecO:
            print ()
            print ("Jednostki Qi")
            print ()    
            print("Q0:", Q0)
            print("Q1:", Q1)
            print("Q2:", Q2)
            print("Q3:", Q3)
            print("Q4:", Q4)
            print()
            
#Rząd wiazania od długosci wiazania 
def rzadwiazania_dlugoscwiazania(nazwa1, nazwa2, promien_od_rzad_wiazania, poczatek, koniec, poczatek2, koniec2):
    if poczatek != -1 and koniec != -1 and poczatek2 != -1 and koniec2 != -1:
        dlugosc = 0
        print()
        print()
        print("id",nazwa1,"id", nazwa2, "dlugosc wiazania [A], rzadwiazania, połączenia do tlenu: P-O, P=O, Fe-O, Al-O ")
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
                            dlugosc = ((kor2X[y]-korX[x])**2+(kor2Y[y]-korY[x])**2+(kor2Z[y]-korZ[x])**2)**0.5
                            if dlugosc < 8 and nazwa2 == 'O': 
                                print(x + 1, kolumna + 1, '   ', round(dlugosc, 4), Tabelarzadwiazania[x][kolumna], '   ', tablicaOP[kolumna- poczatekO], tablicaOP2[kolumna- poczatekO], tablicaFe[kolumna- poczatekO], tablicaAl[kolumna- poczatekO],)
                                if tablicaOP[kolumna- poczatekO] == 2: 
                                    iloscPOP = iloscPOP + 1 
                                if tablicaOP[kolumna- poczatekO] == 1:
                                    if tablicaFe[kolumna- poczatekO] == 0 and tablicaAl[kolumna- poczatekO] == 0: 
                                        iloscPO += 1 
                                    if tablicaFe[kolumna- poczatekO] == 1 and tablicaAl[kolumna- poczatekO] == 0:
                                        iloscPOFe += 1
                                    if tablicaFe[kolumna- poczatekO] == 2 and tablicaAl[kolumna- poczatekO] == 0:
                                        iloscPOFe2 += 1
                                    if tablicaFe[kolumna- poczatekO] == 0 and tablicaAl[kolumna- poczatekO] == 1:
                                        iloscPOAl += 1
                                    if tablicaFe[kolumna- poczatekO] == 0 and tablicaAl[kolumna- poczatekO] == 2:
                                        iloscPOAl2 += 1
                                    if tablicaFe[kolumna- poczatekO] == 1 and tablicaAl[kolumna- poczatekO] == 1:
                                        iloscPOFeAl += 1
                                    if tablicaFe[kolumna- poczatekO] == 2 and tablicaAl[kolumna- poczatekO] == 1:
                                        iloscPOFe2Al += 1
                                    if tablicaFe[kolumna- poczatekO] == 1 and tablicaAl[kolumna- poczatekO] == 2:
                                        iloscPOFeAl2 += 1 
                                if tablicaOP[kolumna- poczatekO] == 0:
                                        
                                    if tablicaFe[kolumna- poczatekO] == 2 and tablicaAl[kolumna- poczatekO] == 0:
                                        iloscFeOFe += 1
                                    if tablicaFe[kolumna- poczatekO] == 0 and tablicaAl[kolumna- poczatekO] == 2:
                                        iloscAlOAl += 1
                                    if tablicaFe[kolumna- poczatekO] == 3 and tablicaAl[kolumna- poczatekO] == 0:
                                        iloscFeO2Fe += 1 
                                    if tablicaFe[kolumna- poczatekO] == 0 and tablicaAl[kolumna- poczatekO] == 3:
                                        iloscAlO2Al += 1     
                                    if tablicaFe[kolumna- poczatekO] == 1 and tablicaAl[kolumna- poczatekO] == 1:
                                        iloscAlFe += 1
                                    if tablicaFe[kolumna- poczatekO] == 2 and tablicaAl[kolumna- poczatekO] == 1:
                                        iloscFe2Al += 1
                                    if tablicaFe[kolumna- poczatekO] == 1 and tablicaAl[kolumna- poczatekO] == 2:
                                        iloscAl2Fe += 1 
                                    
                            elif dlugosc < 8: 
                                print(x + 1, kolumna + 1, '   ', round(dlugosc, 4), Tabelarzadwiazania[x][kolumna])
        print()
        print()
        print("ilosc wiazan z tlenem: ", nazwa1, "-O ",  "dla połaczeń:" )
        if iloscPOP > 0: 
            print("P-O-P:", iloscPOP )

        if iloscPO > 0:
            print("P=O:", iloscPO )
        if iloscPOFe > 0:
            print("P-O-Fe:", iloscPOFe)
        if iloscPOFe2 > 0:
            print("P-O-2Fe:", iloscPOFe2 )
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
        
#       
#       
#
#Program    
#
                     
#Wpisyawnie w pierszu poleceń komend 
a = input()
mmm = a.split()
a = mmm[0]
ilosckolumnh = int(input())
promienodcieciapo = float(input())
promienodcieciapo2 = float(input()) 
promienodcieciaFe = float(input())
promienodcieciaAl = float(input())
promienodcieciaPP = float(input())
promienodcieciaPAl = float(input())
promienodcieciaPFe = float(input())
promienodcieciaFeFe = float(input())
promienodcieciaFeAl = float(input())
promienodcieciaAlAl = float(input())
nazwaX = input()
XXX = nazwaX.split()
nazwaX = XXX[0]
promienodcieciaX = float(input())
promienodcieciaG = float(input())

print("Wyniki CPMD")
print()
print()
print("Promien odciecia P-O1: ", promienodcieciapo)
print("Promien odciecia P-O2: ", promienodcieciapo2)
print("Promien odciecia Fe-O: ", promienodcieciaFe)
print("Promien odciecia Al-O: ", promienodcieciaAl)
print("Promien odciecia P-P: ", promienodcieciaPP)
print("Promien odciecia P-Al: ", promienodcieciaPAl)
print("Promien odciecia P-Fe: ", promienodcieciaPFe)
print("Promien odciecia Fe-Fe: ", promienodcieciaFeFe)
print("Promien odciecia Fe-Al: ", promienodcieciaFeAl)
print("Promien odciecia Al-Al: ", promienodcieciaAlAl)

print("Promien odciecia ", nazwaX, "-O: ", promienodcieciaX, sep='')
print("Promien odciecia dla pozostałych połaczeń: ", promienodcieciaG)
print()
print()

#otwiera plik z danymi 
f = open(a, "r")
c = " POPULATION ANALYSIS FROM PROJECTED WAVEFUNCTIONS"
d = " MAYER BOND ORDERS FROM PROJECTED WAVEFUNCTIONS"
b = "0"

tablicamulikenlowdinvalence = []
while "SYMMETRY:                                           SIMPLE CUBIC" not in b:
    b = f.readline()
informacja_o_komurce = f.readline()

splitted = informacja_o_komurce.split()
kolumna = 0 
for symbol in splitted:
    kolumna +=1 
    if kolumna == 3:
        krawendz = float(symbol)

while c not in b:
    b = f.readline()
 
b =f.readline()     
b =f.readline()   
b =f.readline() 
while "\n" != b:
    tablicamulikenlowdinvalence.append(b)
    b = f.readline()
    
    
#Wczytywanie tablicy z rzedami wiazania-linijkami 
tablicamayerbondorders = []

while d not in b:
    b=f.readline()
    
f.readline()
b = f.readline()
b = f.readline()

ilelinijek =0 #ile linijek w stringu tablicamayerbondorders
while "\n" != b:
    j = 0 
    while "\n" != b:
        tablicamayerbondorders.append(b)
        ilelinijek += 1
        b = f.readline()
        j +=1
        
    b = f.readline()
    b = f.readline()

    
while "ATOM             COORDINATES                   CHARGES" not in b:
    b = f.readline()   

tablicacordinates = []
b = f.readline()
b = f.readline()

while "ChkSum" not in b:
    tablicacordinates.append(b)
    b = f.readline()

Tabelarzadwiazania = np.zeros(shape=(2*j,j + 2*j))

kolumna = 0
kolumna2 = 0
kolumna3 =0
wiersz = 0
poczatek = 0
koniec = j

#print(ilelinijek)

zakres = ilelinijek/j #ilelinijek
zakres = int(zakres)

#Przetwarzanie tablicy z ładunkami i walencyjnosciami 
ladunekmulikena = []
for y in range(poczatek, koniec):
    e = tablicamulikenlowdinvalence[y]
    splitted = e.split()
    kolumna = 0 
    for symbol in splitted:
        kolumna +=1 
        if kolumna == 3: 
            ladunekmulikena.append(float(symbol))
            
                
#Przetworzenie wcztanych linijek na macierz rzedow wiazania 
for y in range(0, zakres):
    wiersz = 0
    kolumna = 0
    Symbolpierwiastka = []
    for x in range(poczatek, koniec):
        e = tablicamayerbondorders[x]
        splitted = e.split()
        kolumna = -1 #bo pierwsza kolumna nie moze być wczytana
        kolumna2 = kolumna3
        for symbol in splitted: 
            if kolumna == -1: 
                kolumna += 1 
            elif is_number(symbol) == True:
                Tabelarzadwiazania[wiersz][kolumna2] = symbol 
                kolumna2 += 1 
                kolumna += 1 
            else:
                Symbolpierwiastka.append(symbol)
        wiersz +=1  
    kolumna3 = kolumna2  
    poczatek = koniec
    koniec = koniec + j  
print()     
print("tablica posklejana - rząd wiązania Mayera")   
print()  

for y in range(0, j):
    for x in range(0, kolumna2):
        print(Tabelarzadwiazania[y][x], end =" ")
    print() 
print()

#tablica koordynaty        
korX =[] 
korY = [] 
korZ = []
for y in range(0, j):
    e = tablicacordinates[y]
    splitted = e.split()
    kolumna = 0 
    for symbol in splitted:
        kolumna +=1 
        if kolumna == 3: 
            korX.append(0.52917720859*float(symbol))
        if kolumna == 4: 
            korY.append(0.52917720859*float(symbol))
        if kolumna == 5: 
            korZ.append(0.52917720859*float(symbol))
            
krawendz = 0.52917720859*krawendz
            
#wypisywanie koordynatów atomów plik xyz. 
print()
print('koordynaty-xyz')
print()
print(j)
print('koordynaty [A]')
for x in range(0,j): 
    print( Symbolpierwiastka[x], korX[x], korY[x], korZ[x])
print()
print()

#Periodyczne warunki brzegowe

kor2X =[0 for x in range(0, 27*j)]
kor2Y = [0 for x in range(0, 27*j)]
kor2Z = [0 for x in range(0, 27*j)]
indeksko = ['x' for x in range(0, 27*j)]
Nr = [0 for x in range(0, 27*j)]
w = -1

#Tworzenie tablicy 2 
for x in range(0, j):
    
    indeksko[x] = Symbolpierwiastka[x]
    Nr[x] = x
    kor2X[x] = korX[x]
    kor2Y[x] = korY[x]
    kor2Z[x] = korZ[x]

    #sciany
    w = w + 1 
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x]
    kor2Z[j + w] = korZ[x]
                
                
    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x]
    kor2Z[j + w] = korZ[x]


    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] 
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x]
   
    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] 
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x]

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] 
    kor2Y[j + w] = korY[x] 
    kor2Z[j + w] = korZ[x] + krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] 
    kor2Y[j + w] = korY[x] 
    kor2Z[j + w] = korZ[x] - krawendz

    #krawędzie 
    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x] 

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x] 

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x] 
    kor2Z[j + w] = korZ[x] + krawendz
    
    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x] 
    kor2Z[j + w] = korZ[x] - krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] 
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x] + krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] 
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x] - krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x] 

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x] 

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x] 
    kor2Z[j + w] = korZ[x] - krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x] 
    kor2Z[j + w] = korZ[x] + krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] 
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x] - krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] 
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x] + krawendz

    #wieszchołki 

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x] + krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x] - krawendz
    
    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x] - krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x] - krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x] + krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x] + krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] - krawendz
    kor2Y[j + w] = korY[x] + krawendz
    kor2Z[j + w] = korZ[x] - krawendz

    w = w + 1
    Nr[j + w] = x
    indeksko[j + w] = Symbolpierwiastka[x]
    kor2X[j + w] = korX[x] + krawendz
    kor2Y[j + w] = korY[x] - krawendz
    kor2Z[j + w] = korZ[x] + krawendz
    
#print("poczatek") 
#for x in range(0, 27*j):
    #print(indeksko[x], kor2X[x], kor2Y[x], kor2Z[x])

poczatekP = -1
koniecP = -1

for x in range(0, j):
    if Symbolpierwiastka[x] == "P" and Symbolpierwiastka[x - 1] != "P":
        poczatekP = x  
    if Symbolpierwiastka[x] == "P" and x == j-1:
        koniecP = x
    elif Symbolpierwiastka[x] == "P" and Symbolpierwiastka[x + 1] != "P":
        koniecP = x
        
poczatekO = -1
koniecO = -1

for x in range(0, j):
    if Symbolpierwiastka[x] == "O" and Symbolpierwiastka[x - 1] != "O":
        poczatekO = x 
    if Symbolpierwiastka[x] == "O" and x == j-1:
        koniecO = x
    elif Symbolpierwiastka[x] == "O" and Symbolpierwiastka[x + 1] != "O":
        koniecO = x

poczatekFe = -1
koniecFe = -1

for x in range(0, j):
    if Symbolpierwiastka[x] == "Fe" and Symbolpierwiastka[x - 1] != "Fe":
        poczatekFe = x  
    if Symbolpierwiastka[x] == "Fe" and x == j-1:
        koniecFe = x
    elif Symbolpierwiastka[x] == "Fe" and Symbolpierwiastka[x + 1] != "Fe":
        koniecFe = x

poczatekAl = -1
koniecAl = -1

for x in range(0, j):
    if Symbolpierwiastka[x] == "Al" and Symbolpierwiastka[x - 1] != "Al":
        poczatekAl = x  
    if Symbolpierwiastka[x] == "Al" and x == j-1:
        koniecAl = x
    elif Symbolpierwiastka[x] == "Al" and Symbolpierwiastka[x + 1] != "Al":
        koniecAl = x
        
poczatekX = -1
koniecX = -1

for x in range(0, j):
    if Symbolpierwiastka[x] == nazwaX and Symbolpierwiastka[x - 1] != nazwaX:
        poczatekX = x  
    if Symbolpierwiastka[x] == nazwaX and x == j-1:
        koniecX = x
    elif Symbolpierwiastka[x] == nazwaX and Symbolpierwiastka[x + 1] != nazwaX:
        koniecX = x

#histogram iloć(rzad wiaznia)
    
    
minimumido = int(-10)
maximumido = int(-10) 
minimumidoFe = int(-10)
maximumidoFe = int(-10)
minimumidoAl = int(-10)
maximumidoAl = int(-10)
minimumidoX = int(-10)
maximumidoX = int(-10)
minimumidp = int(-10)  
maximumidp = int(-10) 
minimumidFe = int(-10)  
maximumidFe = int(-10)
minimumidAl = int(-10)  
maximumidAl = int(-10)
minimumidX = int(-10)  
maximumidX = int(-10)

tablicaOP = [] 
tablicaOP2 = []
tablicaFe = []
tablicaAl = []
tablicaX = []

wiersz2 = 0 
TabelarzadwiazaniaO = np.zeros(shape=(5*j, 10))

for wiersz in range(poczatekO, koniecO + 1):
    i = 0
    Fe = 0
    Al = 0
    X = 0
    liczbapromienodcieca2 = 0
    if poczatekP != -1 and koniecP !=-1:
        for kolumna in range(poczatekP, (koniecP + 1)):
            if wiersz == poczatekO and kolumna == poczatekP:
                minimumido = poczatekO
                maximumido = poczatekO
                minimumidp = poczatekP
                maximumidp = poczatekP
            if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumido][minimumidp]:
                minimumido = wiersz
                minimumidp = kolumna
            if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumido][maximumidp]:
                maximumido = wiersz 
                maximumidp = kolumna 
            if Tabelarzadwiazania[wiersz][kolumna] > promienodcieciapo: 
                i += 1
                TabelarzadwiazaniaO[wiersz2][i]=Tabelarzadwiazania[wiersz][kolumna]
                if Tabelarzadwiazania[wiersz][kolumna] > promienodcieciapo2:
                    liczbapromienodcieca2 +=1             
    tablicaOP.append(i)
    tablicaOP2.append(liczbapromienodcieca2)
    if poczatekFe != -1 and koniecFe !=-1:
        for kolumna in range(poczatekFe, koniecFe + 1):
            if wiersz == poczatekO and kolumna == poczatekFe:
                minimumidoFe = poczatekO
                maximumidoFe = poczatekO
                minimumidFe = poczatekFe
                maximumidFe = poczatekFe
            if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidoFe][minimumidFe]:
                minimumidoFe = wiersz
                minimumidFe = kolumna
            if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidoFe][maximumidFe]:
                maximumidoFe = wiersz 
                maximumidFe = kolumna
            if Tabelarzadwiazania[wiersz][kolumna] > promienodcieciaFe: 
                Fe += 1
                TabelarzadwiazaniaO[wiersz2][i + Fe]=Tabelarzadwiazania[wiersz][kolumna]
    tablicaFe.append(Fe)
    if poczatekAl != -1 and koniecAl !=-1:
        for kolumna in range(poczatekAl, (koniecAl + 1)):
            if wiersz == poczatekO and kolumna == poczatekAl:
                minimumidoAl = poczatekO
                maximumidoAl = poczatekO
                minimumidAl = poczatekAl
                maximumidAl = poczatekAl
            if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidoAl][minimumidAl]:
                minimumidoAl = wiersz
                minimumidAl = kolumna
            if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidoAl][maximumidAl]:
                maximumidoAl = wiersz 
                maximumidAl = kolumna
            if Tabelarzadwiazania[wiersz][kolumna] > promienodcieciaAl:
                Al += 1
                TabelarzadwiazaniaO[wiersz2][i + Fe + Al]=Tabelarzadwiazania[wiersz][kolumna]
    tablicaAl.append(Al)
    if poczatekX != -1 and koniecX !=-1:
        for kolumna in range(poczatekX, (koniecX + 1)):
            if wiersz == poczatekO and kolumna == poczatekX:
                minimumidoX = poczatekO
                maximumidoX = poczatekO
                minimumidX = poczatekX
                maximumidX = poczatekX
            if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidoX][minimumidX]:
                minimumidoX = wiersz
                minimumidX = kolumna
            if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidoX][maximumidX]:
                maximumidoX = wiersz 
                maximumidX = kolumna
            if Tabelarzadwiazania[wiersz][kolumna] > promienodcieciaX: 
                X += 1
                TabelarzadwiazaniaO[wiersz2][i + Fe + Al + X]=Tabelarzadwiazania[wiersz][kolumna]
    tablicaX.append(X)
    wiersz2 += 1
    
    
minimumidFeFe = int(-10)  
maximumidFeFe = int(-10)
minimumidFeFe2 = int(-10)  
maximumidFeFe2= int(-10)
minimumidAlAl = int(-10)  
maximumidAlAl = int(-10)
minimumidAlAl2 = int(-10)  
maximumidAlAl2 = int(-10)
minimumidPP = int(-10)  
maximumidPP = int(-10)
minimumidPP2 = int(-10)  
maximumidPP2 = int(-10)
minimumidFeP = int(-10)  
maximumidFeP = int(-10)
minimumidFeP2 = int(-10)  
maximumidFeP2 = int(-10)
minimumidAlP = int(-10)  
maximumidAlP = int(-10)
minimumidAlP2 = int(-10)  
maximumidAlP2 = int(-10)
minimumidFeAl = int(-10)  
maximumidFeAl = int(-10)
minimumidFeAl2 = int(-10)  
maximumidFeAl2 = int(-10)



if poczatekFe != -1 and koniecFe !=-1:
    for wiersz in range(poczatekFe, koniecFe + 1):
        Fe = 0
        if poczatekFe != -1 and koniecFe !=-1:
            for kolumna in range(poczatekFe, koniecFe + 1):
                if wiersz == poczatekFe and kolumna == poczatekFe:
                    minimumidFeFe = poczatekFe
                    maximumidFeFe = poczatekFe
                    minimumidFeFe2 = poczatekFe
                    maximumidFeFe2 = poczatekFe
                if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidFeFe][minimumidFeFe2]:
                    minimumidFeFe = wiersz
                    minimumidFeFe2 = kolumna
                if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidFeFe][maximumidFeFe2]:
                    maximumidFeFe = wiersz 
                    maximumidFeFe2 = kolumna
                if Tabelarzadwiazania[wiersz][kolumna] > promienodcieciaFeFe: 
                    Fe += 1
                

if poczatekAl != -1 and koniecAl !=-1:
    for wiersz in range(poczatekAl, koniecAl + 1):
        Al = 0
        if poczatekAl != -1 and koniecAl !=-1:
            for kolumna in range(poczatekAl, koniecAl + 1):
                if wiersz == poczatekAl and kolumna == poczatekAl:
                    minimumidAlAl = poczatekAl
                    maximumidAlAl = poczatekAl
                    minimumidAlAl2 = poczatekAl
                    maximumidAlAl2 = poczatekAl
                if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidAlAl][minimumidAlAl2]:
                    minimumidAlAl = wiersz
                    minimumidAlAl2 = kolumna
                if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidAlAl][maximumidAlAl2]:
                    maximumidAlAl = wiersz 
                    maximumidAlAl2 = kolumna
        
if poczatekP != -1 and koniecP !=-1:
    for wiersz in range(poczatekP, koniecP + 1):
        if poczatekP != -1 and koniecP !=-1:
            for kolumna in range(poczatekP, koniecP + 1):
                if wiersz == poczatekP and kolumna == poczatekP:
                    minimumidPP = poczatekP
                    maximumidPP = poczatekP
                    minimumidPP2 = poczatekP
                    maximumidPP2 = poczatekP
                if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidPP][minimumidPP2]:
                    minimumidPP = wiersz
                    minimumidPP2 = kolumna
                if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidPP][maximumidPP2]:
                    maximumidPP = wiersz 
                    maximumidPP2 = kolumna     
    
if poczatekP != -1 and koniecP !=-1:
    for wiersz in range(poczatekP, koniecP + 1):
        if poczatekFe != -1 and koniecFe !=-1:
            for kolumna in range(poczatekFe, koniecFe + 1):
                if wiersz == poczatekP and kolumna == poczatekFe:
                    minimumidFeP = poczatekP
                    maximumidFeP = poczatekP
                    minimumidFeP2 = poczatekFe
                    maximumidFeP2 = poczatekFe
                if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidFeP][minimumidFeP2]:
                    minimumidFeP = wiersz
                    minimumidFeP2 = kolumna
                if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidFeP][maximumidFeP2]:
                    maximumidFeP = wiersz 
                    maximumidFeP2 = kolumna 
                    
if poczatekP != -1 and koniecP !=-1:
    for wiersz in range(poczatekP, koniecP + 1):
        if poczatekAl != -1 and koniecAl !=-1:
            for kolumna in range(poczatekAl, koniecAl + 1):
                if wiersz == poczatekP and kolumna == poczatekAl:
                    minimumidAlP = poczatekP
                    maximumidAlP = poczatekP
                    minimumidAlP2 = poczatekAl
                    maximumidAlP2 = poczatekAl
                if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidAlP][minimumidAlP2]:
                    minimumidAlP = wiersz
                    minimumidAlP2 = kolumna
                if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidAlP][maximumidAlP2]:
                    maximumidAlP = wiersz 
                    maximumidAlP2 = kolumna 

if poczatekFe != -1 and koniecFe !=-1:
    for wiersz in range(poczatekFe, koniecFe + 1):
        if poczatekAl != -1 and koniecAl !=-1:
            for kolumna in range(poczatekAl, koniecAl + 1):
                if wiersz == poczatekFe and kolumna == poczatekAl:
                    minimumidFeAl = poczatekFe
                    maximumidFeAl = poczatekFe
                    minimumidFeAl2 = poczatekAl
                    maximumidFeAl2 = poczatekAl
                if Tabelarzadwiazania[wiersz][kolumna] <= Tabelarzadwiazania[minimumidAlP][minimumidAlP2]:
                    minimumidFeAl = wiersz
                    minimumidFeAl2 = kolumna
                if Tabelarzadwiazania[wiersz][kolumna] >= Tabelarzadwiazania[maximumidAlP][maximumidAlP2]:
                    maximumidFeAl = wiersz 
                    maximumidFeAl2 = kolumna 
    
przedzialh = (Tabelarzadwiazania[maximumido][maximumidp] - Tabelarzadwiazania[minimumido][minimumidp]) / ilosckolumnh
przedzialhFe = (Tabelarzadwiazania[maximumidoFe][maximumidFe] - Tabelarzadwiazania[minimumidoFe][minimumidFe]) / ilosckolumnh
przedzialhAl = (Tabelarzadwiazania[maximumidoAl][maximumidAl] - Tabelarzadwiazania[minimumidoAl][minimumidAl]) / ilosckolumnh
przedzialhFeFe = (Tabelarzadwiazania[maximumidFeFe][maximumidFeFe2] - Tabelarzadwiazania[minimumidFeFe][minimumidFeFe2]) / ilosckolumnh
przedzialhAlAl = (Tabelarzadwiazania[maximumidAlAl][maximumidAlAl2] - Tabelarzadwiazania[minimumidAlAl][minimumidAlAl2]) / ilosckolumnh

#Wypisywanie min i max dla rzedu wiazania dla danego połączenia 
min_max('P-O', maximumido, minimumido, maximumidp, minimumidp)
min_max('Fe-O', maximumidoFe, minimumidoFe, maximumidFe, minimumidFe)
min_max('Al-O', maximumidoAl, minimumidoAl, maximumidAl, minimumidAl)

nazwa = nazwaX + "-O"
min_max(nazwa, maximumidoX, minimumidoX, maximumidX, minimumidX)

min_max('Fe-Fe', maximumidFeFe, minimumidFeFe, maximumidFeFe2, minimumidFeFe2)
min_max('Al-Al', maximumidAlAl, minimumidAlAl, maximumidAlAl2, minimumidAlAl2)
min_max('P-P', maximumidPP, minimumidPP, maximumidPP2, minimumidPP2)
min_max('Fe-P', maximumidFeP, minimumidFeP, maximumidFeP2, minimumidFeP2)
min_max('Al-P', maximumidAlP, minimumidAlP, maximumidAlP2, minimumidAlP2)
min_max('Fe-Al', maximumidFeAl, minimumidFeAl, maximumidFeAl2, minimumidFeAl2)

print()
drukuj_przedzial("P-O", przedzialh)
drukuj_przedzial("Fe-O", przedzialhFe)
drukuj_przedzial("Al-O", przedzialhAl)
drukuj_przedzial("Fe-Fe", przedzialhFeFe)
drukuj_przedzial("Al-Al", przedzialhAlAl)
print()

#histogramP-O

gornagranica = Tabelarzadwiazania[minimumido][minimumidp] + przedzialh + 0.0001
dolnagranica = Tabelarzadwiazania[minimumido][minimumidp]

histogram(ilosckolumnh, przedzialh, poczatekO, koniecO, poczatekP, koniecP, dolnagranica, gornagranica, minimumido, minimumidp, "histogram P-O")

#histogramFe-O
       
gornagranica = Tabelarzadwiazania[minimumidoFe][minimumidFe] + przedzialhFe + 0.0001
dolnagranica = Tabelarzadwiazania[minimumidoFe][minimumidFe]

histogram(ilosckolumnh, przedzialhFe, poczatekO, koniecO, poczatekFe, koniecFe, dolnagranica, gornagranica, minimumidoFe, minimumidFe, "histogram Fe-O")

#histogramAl-O

gornagranica = Tabelarzadwiazania[minimumidoAl][minimumidAl] + przedzialhAl + 0.0001
dolnagranica = Tabelarzadwiazania[minimumidoAl][minimumidAl]

histogram(ilosckolumnh, przedzialhAl, poczatekO, koniecO, poczatekAl, koniecAl, dolnagranica, gornagranica, minimumidoAl, minimumidAl, "histogram Al-O") 
   

#histogramFe-Fe
gornagranica = Tabelarzadwiazania[minimumidFeFe][minimumidFeFe2] + przedzialhFeFe + 0.0001
dolnagranica = Tabelarzadwiazania[minimumidFeFe][minimumidFeFe2]

histogram(ilosckolumnh, przedzialhFeFe, poczatekFe, koniecFe, poczatekFe, koniecFe, dolnagranica, gornagranica, minimumidFeFe, minimumidFeFe2, "histogram Fe-Fe") 

#histogramAl-Al
gornagranica = Tabelarzadwiazania[minimumidAlAl][minimumidAlAl2] + przedzialhAlAl + 0.0001
dolnagranica = Tabelarzadwiazania[minimumidAlAl][minimumidAlAl2]

histogram(ilosckolumnh, przedzialhAlAl, poczatekAl, koniecAl, poczatekAl, koniecAl, dolnagranica, gornagranica, minimumidAlAl, minimumidAlAl2, "histogram Al-Al")
  
print()
print()
print("id, polaczenia do P, potencjalne wiązanie P=O (1), polaczenia do Fe, polaczenia do Al, rzad wiazania do P (dwie kolumny)")
print()

ilosc0 = 0
ilosc1 = 0
ilosc2 = 0 
ilosc3 = 0
iloscW = 0
iloscPodw = 0

for x in range(0, koniecO - poczatekO + 1): 
    print (poczatekO + 1 + x, " ", tablicaOP[x], tablicaOP2[x], tablicaFe[x], tablicaAl[x], " ", TabelarzadwiazaniaO[x][1], TabelarzadwiazaniaO[x][2], TabelarzadwiazaniaO[x][3], TabelarzadwiazaniaO[x][4], TabelarzadwiazaniaO[x][5], TabelarzadwiazaniaO[x][6], TabelarzadwiazaniaO[x][7], TabelarzadwiazaniaO[x][8], TabelarzadwiazaniaO[x][9])
    if tablicaOP[x] == 0: 
        ilosc0 +=1 
    if tablicaOP[x] == 1:
        ilosc1 +=1
    if tablicaOP[x] == 2:
        ilosc2 +=1
    if tablicaOP[x] > 2:
        iloscW +=1
    if tablicaOP2[x] >= 1:
        iloscPodw += 1

ilosc0 = round((ilosc0/(koniecO +1 - poczatekO))*100, 5)
ilosc1 = round((ilosc1/(koniecO +1 - poczatekO))*100, 5)
ilosc2 = round((ilosc2/(koniecO +1 - poczatekO))*100, 5)
ilosc3 = round((iloscW/(koniecO +1 - poczatekO))*100, 5) 

print ("Statystyka połączeń O do P")
print ()
print ("ilosć połączen, procent")
print ()
print ("0:", ilosc0)
print ("1:", ilosc1)  
print ("2:", ilosc2) 
print ("Więcej niż 2:", iloscW)
print ()
print ()
print ("ilosć ptencjanych wiazań podwójnych:")
print (iloscPodw)

#koordynacjaP 
print()
print()
koordynacja(poczatekP, koniecP, poczatekO, koniecO, promienodcieciapo, "P, koordynacja do tlenu")
#koordynacjaFe
print()
print()
koordynacja(poczatekFe, koniecFe, poczatekO, koniecO, promienodcieciaFe, "Fe, koordynacja do tlenu")

#koordynacjaAl
print()
print()
koordynacja(poczatekAl, koniecAl, poczatekO, koniecO, promienodcieciaAl, "Al, koordynacja do tlenu")

nazwa = nazwaX + ", koordynacja"

#koordynacjaX
print()
print()
koordynacja(poczatekX, koniecX, poczatekO, koniecO, promienodcieciaX, nazwa)

#koordynacjaFeFe----------------------------------------------------------------------------------------------------------------------------------------------
print()
print()
koordynacja(poczatekFe, koniecFe, poczatekFe, koniecFe, promienodcieciaFeFe, "Fe-Fe, koordynacja")

#koordynacjaAlAl
print()
print()
koordynacja(poczatekAl, koniecAl, poczatekAl, koniecAl, promienodcieciaAlAl, "Al-Al, koordynacja")

#koordynacjaPP
print()
print()
koordynacja(poczatekP, koniecP, poczatekP, koniecP, promienodcieciaPP, "P-P, koordynacja")

#koordynacjaPFe
print()
print()
koordynacja(poczatekP, koniecP, poczatekFe, koniecFe, promienodcieciaPFe, "P-Fe, koordynacja")

#koordynacjaPAl
print()
print()
koordynacja(poczatekP, koniecP, poczatekAl, koniecAl, promienodcieciaPAl, "P-Al, koordynacja")

#koordynacjaFeAl
print()
print()
koordynacja(poczatekFe, koniecFe, poczatekAl, koniecAl, promienodcieciaFeAl, "Fe-Al, koordynacja")

#Walencyjnosc 
print("Walencyjnosci atomow")
print()
Walencyjnosc_kowa("P", poczatekP, koniecP)
print()
Walencyjnosc_kowa("Fe", poczatekFe, koniecFe)
print()
Walencyjnosc_kowa("Al", poczatekAl, koniecAl)
print()
Walencyjnosc_kowa("O", poczatekO, koniecO)
print()
Walencyjnosc_kowa(nazwaX, poczatekX, koniecX)
print()
print()
#rzadwiazania w funkcji dlugosci wiazania
rzadwiazania_dlugoscwiazania("P", "O", promienodcieciapo, poczatekP, koniecP, poczatekO, koniecO)
print()
print()
rzadwiazania_dlugoscwiazania("Fe", "O", promienodcieciaFe, poczatekFe, koniecFe, poczatekO, koniecO)
print()
print()
rzadwiazania_dlugoscwiazania("Al", "O", promienodcieciaAl, poczatekAl, koniecAl, poczatekO, koniecO)
print()
print()
rzadwiazania_dlugoscwiazania(nazwaX, "O", promienodcieciaX, poczatekX, koniecX, poczatekO, koniecO)
print()
print()
rzadwiazania_dlugoscwiazania("Fe", "Fe", promienodcieciaFeFe, poczatekFe, koniecFe, poczatekFe, koniecFe) 
print()
print()
print()
print("koniec!")
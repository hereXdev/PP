# ------------------------------------------- LISTA 1.1 -------------------------------------------
# -------------------------------------------------------------------------------------------------





# ------------------------------------------- ZADANIE 1.1 -------------------------------------------

# print("Witaj w kalkulatorze BMI, podaj swoje dane: \n")

# wzrost = float(input("Podaj swoj wzrost: "))
# waga = float(input("Podaj swoja wage: "))

# BMI = waga/((wzrost/100)**2)

# sformatowana = f"{BMI:.2f}"
# print(sformatowana)  





# ------------------------------------------- ZADANIE 1.2 -------------------------------------------

# print("Kalkulator Dochodu Rodzinnego na Osobę")
# ojciec = float(input("Podaj dochód ojca: "))
# matka = float(input("Podaj dochód matki: "))
# liczba = float(input("Podaj ilość członków rodziny: "))

# caldochod = (ojciec + matka)
# dochodos = (ojciec + matka) / liczba

# Fcaldochod = f"{caldochod:.2f}"
# Fdochodos = f"{dochodos:.2f}"

# print("---------WYNIK--------")
# print("Dochod całkowity: ",Fcaldochod)
# print("Dochód na osobę: ",Fdochodos)






# ------------------------------------------- ZADANIE 1.3 -------------------------------------------

# print("Kalkulator wzrostu CM na CAL i STOPE")
# CM = float(input("Podaj CM: "))
# STOPA = float(30.48)
# CAL = float(2.54)

# przelstop = CM // STOPA
# przelstop1 = CM % STOPA

# przelcal = przelstop1 // CAL

# print("---------WYNIK--------")
# print("Twój wzrost:  ")
# print(f"W CM: {CM} | W STOPACH: {przelstop} | W CAL: {przelcal}")




# ------------------------------------------- ZADANIE 1.4 -------------------------------------------

# import math

# wysokosc = int(input("Podaj wyokość nad ziemią (w metrach): "))
# pierw_wysokosc = math.sqrt(wysokosc)

# d = (3.57 * pierw_wysokosc)
# wynik = (d / 1000 )
# print(f"Dystans to: {wynik:.2f}km")






# ------------------------------------------- ZADANIE 1.5 -------------------------------------------

# import math

# # promień koła
# r = 5

# # obliczanie pola
# pole = math.pi * r**2

# # obliczanie obwodu
# obwod = 2 * math.pi * r

# print("Promień:", r)
# print("Pole koła:", pole)
# print("Obwód koła:", obwod)






# ------------------------------------------- ZADANIE 1.6 -------------------------------------------

# dystans = float(input("Podaj dystans w km: "))
# cena_paliwa = float(input("Podaj cenę paliwa za litr: "))
# spalanie = float(input("Podaj spalanie (l/100km): "))

# zuzycie = (dystans * spalanie) / 100

# koszt = zuzycie * cena_paliwa

# print("Zużycie paliwa:", zuzycie, "l")
# print("Koszt podróży:", koszt, "zł")







# ------------------------------------------- ZADANIE 1.7 -------------------------------------------

# netto = float(input("Podaj kwotę netto: "))

# # VAT 23%
# vat = netto * 0.23
# brutto = netto + vat

# print(f"VAT: {vat:.2f} zł")
# print(f"Kwota brutto: {brutto:.2f} zł")








# ------------------------------------------- ZADANIE 1.8 -------------------------------------------

# wiek = int(input("Podaj swój wiek: "))
# zwolnienie = wiek <= 26

# print("Czy masz zwolnienie podatkowe:", zwolnienie)










# ------------------------------------------- ZADANIE 1.9 -------------------------------------------

# haslo = input("Podaj hasło: ")
# czy_poprawne = len(haslo) >= 8

# print("Czy hasło ma co najmniej 8 znaków:", czy_poprawne)







# ------------------------------------------- ZADANIE 1.10 -------------------------------------------

# rejestracja = input("Podaj numer rejestracyjny: ")

# # sprawdzenie pierwszych dwóch liter
# czy_krakow = rejestracja[:2] == "KR" or rejestracja[:2] == "KK"

# print("Czy rejestracja jest z Krakowa?:", czy_krakow)










# ------------------------------------------- ZADANIE 1.11 -------------------------------------------

# predkosc = float(input("Podaj prędkość km/h: "))

# # sprawdzenie zakresu
# czy_ok = predkosc >= 40 and predkosc <= 140

# print("Czy prędkość jest dozwolona:", czy_ok)










# ------------------------------------------- ZADANIE 1.12 -------------------------------------------

# tekst = "Mr. John May, born on 1998-02-16"
# imie = tekst[4:8]
# nazwisko = tekst[9:12]
# inicjaly = imie[0] + nazwisko[0]
# data = tekst[-10:]

# print("Imię:", imie)
# print("Nazwisko:", nazwisko)
# print("Inicjały:", inicjaly)
# print("Data urodzenia:", data)





# ------------------------------------------- ZADANIE 1.13 -------------------------------------------

# telefon = input("Podaj numer telefonu (9 cyfr): ")

# cz1 = telefon[0:3]
# cz2 = telefon[3:6]
# cz3 = telefon[6:9]

# print(cz1 + "-" + cz2 + "-" + cz3)









# ------------------------------------------- ZADANIE 1.14 -------------------------------------------

# swift = input("Podaj kod SWIFT (8 znaków): ")

# bank = swift[0:4]
# kraj = swift[4:6]

# print("Kod banku:", bank)
# print("Kod kraju:", kraj)








# ------------------------------------------- ZADANIE 1.15 -------------------------------------------

# x = 7
# y = 34

# print("Przed zamianą:")
# print("x =", x)
# print("y =", y)

# # temp - zmienna pomocnicza 
# temp = x
# x = y
# y = temp

# print("Po zamianie:")
# print("x =", x)
# print("y =", y)








# ------------------------------------------- ZADANIE 1.16 -------------------------------------------

# import random
# komputer = random.randint(1, 6)
# zgadnij = int(input("Zgadnij liczbę od 1 do 6: "))

# print("Czy trafiłeś:", zgadnij == komputer)










# ------------------------------------------- ZADANIE 1.17 -------------------------------------------

# import random

# r1 = random.randint(1, 6)
# r2 = random.randint(1, 6)
# r3 = random.randint(1, 6)

# suma = r1 + r2 + r3

# print("Rzut 1:", r1)
# print("Rzut 2:", r2)
# print("Rzut 3:", r3)
# print("Suma:", suma)









# ------------------------------------------- ZADANIE 1.18 -------------------------------------------

# liczba = int(input("Podaj liczbę całkowitą: "))

# print("Binarnie:", bin(liczba))
# print("Szesnastkowo:", hex(liczba))











# ------------------------------------------- ZADANIE 1.19 -------------------------------------------

# znak = input("Podaj znak: ")

# kod = ord(znak)

# print("Kod ASCII/Unicode:", kod)







# ------------------------------------------- ZADANIE 1.20 -------------------------------------------

# kody = [67, 111, 111, 108, 33]

# tekst = ""

# for kod in kody:
#     znak = chr(kod)
#     tekst += znak

# print("Odkodowany tekst:", tekst)








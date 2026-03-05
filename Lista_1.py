# ------------------------------------------- LISTA 1.1 -------------------------------------------
# -------------------------------------------------------------------------------------------------





# ------------------------------------------- ZADANIE 1.1.1 -------------------------------------------

# print("Witaj w kalkulatorze BMI, podaj swoje dane: \n")

# wzrost = float(input("Podaj swoj wzrost: "))
# waga = float(input("Podaj swoja wage: "))

# BMI = waga/((wzrost/100)**2)

# sformatowana = f"{BMI:.2f}"
# print(sformatowana)  





# ------------------------------------------- ZADANIE 1.1.2 -------------------------------------------

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






# ------------------------------------------- ZADANIE 1.1.3 -------------------------------------------

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




# ------------------------------------------- ZADANIE 1.1.4 -------------------------------------------

# import math

# wysokosc = int(input("Podaj wyokość nad ziemią (w metrach): "))
# pierw_wysokosc = math.sqrt(wysokosc)

# d = (3.57 * pierw_wysokosc)
# wynik = (d / 1000 )
# print(f"Dystans to: {wynik:.2f}km")






# ------------------------------------------- ZADANIE 1.1.5 -------------------------------------------

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






# ------------------------------------------- ZADANIE 1.1.6 -------------------------------------------

# dystans = float(input("Podaj dystans w km: "))
# cena_paliwa = float(input("Podaj cenę paliwa za litr: "))
# spalanie = float(input("Podaj spalanie (l/100km): "))

# zuzycie = (dystans * spalanie) / 100

# koszt = zuzycie * cena_paliwa

# print("Zużycie paliwa:", zuzycie, "l")
# print("Koszt podróży:", koszt, "zł")







# ------------------------------------------- ZADANIE 1.1.7 -------------------------------------------

# netto = float(input("Podaj kwotę netto: "))

# # VAT 23%
# vat = netto * 0.23
# brutto = netto + vat

# print(f"VAT: {vat:.2f} zł")
# print(f"Kwota brutto: {brutto:.2f} zł")








# ------------------------------------------- ZADANIE 1.1.8 -------------------------------------------

# wiek = int(input("Podaj swój wiek: "))
# zwolnienie = wiek <= 26

# print("Czy masz zwolnienie podatkowe:", zwolnienie)










# ------------------------------------------- ZADANIE 1.1.9 -------------------------------------------

# haslo = input("Podaj hasło: ")
# czy_poprawne = len(haslo) >= 8

# print("Czy hasło ma co najmniej 8 znaków:", czy_poprawne)







# ------------------------------------------- ZADANIE 1.1.10 -------------------------------------------

# rejestracja = input("Podaj numer rejestracyjny: ")

# # sprawdzenie pierwszych dwóch liter
# czy_krakow = rejestracja[:2] == "KR" or rejestracja[:2] == "KK"

# print("Czy rejestracja jest z Krakowa?:", czy_krakow)










# ------------------------------------------- ZADANIE 1.1.11 -------------------------------------------

# predkosc = float(input("Podaj prędkość km/h: "))

# # sprawdzenie zakresu
# czy_ok = predkosc >= 40 and predkosc <= 140

# print("Czy prędkość jest dozwolona:", czy_ok)










# ------------------------------------------- ZADANIE 1.1.12 -------------------------------------------

# tekst = "Mr. John May, born on 1998-02-16"
# imie = tekst[4:8]
# nazwisko = tekst[9:12]
# inicjaly = imie[0] + nazwisko[0]
# data = tekst[-10:]

# print("Imię:", imie)
# print("Nazwisko:", nazwisko)
# print("Inicjały:", inicjaly)
# print("Data urodzenia:", data)





# ------------------------------------------- ZADANIE 1.1.13 -------------------------------------------

# telefon = input("Podaj numer telefonu (9 cyfr): ")

# cz1 = telefon[0:3]
# cz2 = telefon[3:6]
# cz3 = telefon[6:9]

# print(cz1 + "-" + cz2 + "-" + cz3)









# ------------------------------------------- ZADANIE 1.1.14 -------------------------------------------

# swift = input("Podaj kod SWIFT (8 znaków): ")

# bank = swift[0:4]
# kraj = swift[4:6]

# print("Kod banku:", bank)
# print("Kod kraju:", kraj)








# ------------------------------------------- ZADANIE 1.1.15 -------------------------------------------

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








# ------------------------------------------- ZADANIE 1.1.16 -------------------------------------------

# import random
# komputer = random.randint(1, 6)
# zgadnij = int(input("Zgadnij liczbę od 1 do 6: "))

# print("Czy trafiłeś:", zgadnij == komputer)










# ------------------------------------------- ZADANIE 1.1.17 -------------------------------------------

# import random

# r1 = random.randint(1, 6)
# r2 = random.randint(1, 6)
# r3 = random.randint(1, 6)

# suma = r1 + r2 + r3

# print("Rzut 1:", r1)
# print("Rzut 2:", r2)
# print("Rzut 3:", r3)
# print("Suma:", suma)









# ------------------------------------------- ZADANIE 1.1.18 -------------------------------------------

# liczba = int(input("Podaj liczbę całkowitą: "))

# print("Binarnie:", bin(liczba))
# print("Szesnastkowo:", hex(liczba))











# ------------------------------------------- ZADANIE 1.1.19 -------------------------------------------

# znak = input("Podaj znak: ")

# kod = ord(znak)

# print("Kod ASCII/Unicode:", kod)







# ------------------------------------------- ZADANIE 1.1.20 -------------------------------------------

# kody = [67, 111, 111, 108, 33]

# tekst = ""

# for kod in kody:
#     znak = chr(kod)
#     tekst += znak

# print("Odkodowany tekst:", tekst)




















# ------------------------------------------- LISTA 1.2 -------------------------------------------
# -------------------------------------------------------------------------------------------------



















# ------------------------------------------- ZADANIE 1.2.1 -------------------------------------------

# predkosc = int(input("Podaj prędkość pojazdu (km/h): "))

# if predkosc > 140:
#     print("Przekroczenie prędkości!")
# else:
#     print("Jedziesz zgodnie z przepisami.")






# ------------------------------------------- ZADANIE 1.2.2 -------------------------------------------

# liczba = int(input("Podaj liczbę całkowitą: "))

# if liczba % 2 == 0:
#     print("Liczba parzysta")
# else:
#     print("Liczba nieparzysta")






# ------------------------------------------- ZADANIE 1.2.3 -------------------------------------------

# stan_konta = 500
# kwota = float(input("Podaj kwotę zakupów: "))

# if stan_konta >= kwota:
#     print("Płatność zaakceptowana")
# else:
#     print("Brak środków")






# ------------------------------------------- ZADANIE 1.2.4 -------------------------------------------

# poprawne = int(input("Podaj liczbę poprawnych odpowiedzi: "))
# wszystkie = int(input("Podaj liczbę wszystkich pytań: "))

# procent = (poprawne / wszystkie) * 100

# if procent >= 50:
#     print("Test zaliczony")
# else:
#     print("Test niezaliczony")






# ------------------------------------------- ZADANIE 1.2.5 -------------------------------------------

# pensja = 5000
# premia = input("Czy pracownik otrzymuje premię? (tak/nie): ")

# if premia == "tak":
#     pensja = pensja * 1.15

# print("Ostateczna pensja:", pensja, "zł")






# ------------------------------------------- ZADANIE 1.2.6 -------------------------------------------

# rozmiar = input("Podaj rozmiar (S, M, L, XL): ")

# if rozmiar == "S":
#     print("Small size")
# elif rozmiar == "M":
#     print("Medium size")
# elif rozmiar == "L":
#     print("Large size")
# elif rozmiar == "XL":
#     print("Extra large size")
# else:
#     print("Incorrect symbol")






# ------------------------------------------- ZADANIE 1.2.7 -------------------------------------------

# a = float(input("Podaj pierwszą liczbę: "))
# b = float(input("Podaj drugą liczbę: "))
# operacja = input("Podaj operację (+, -, *, /): ")

# if operacja == "+":
#     wynik = a + b
# elif operacja == "-":
#     wynik = a - b
# elif operacja == "*":
#     wynik = a * b
# elif operacja == "/":
#     wynik = a / b
# else:
#     wynik = "Nieznana operacja"

# print("Wynik:", wynik)






# ------------------------------------------- ZADANIE 1.2.8 -------------------------------------------

# tryb = input("Podaj tryb jazdy (A/M/E): ")
# dystans = float(input("Podaj dystans w km: "))

# if tryb == "A":
#     spalanie = 7
# elif tryb == "M":
#     spalanie = 9
# elif tryb == "E":
#     spalanie = 6
# else:
#     print("Nieznany tryb")
#     spalanie = 0

# zuzycie = (dystans * spalanie) / 100

# print("Zużycie paliwa:", zuzycie, "l")






# ------------------------------------------- ZADANIE 1.2.9 -------------------------------------------

# miesiac = int(input("Podaj numer miesiąca (1-12): "))

# if 1 <= miesiac <= 3:
#     print("I kwartał")
# elif 4 <= miesiac <= 6:
#     print("II kwartał")
# elif 7 <= miesiac <= 9:
#     print("III kwartał")
# elif 10 <= miesiac <= 12:
#     print("IV kwartał")
# else:
#     print("Błędny numer miesiąca")






# ------------------------------------------- ZADANIE 1.2.10 -------------------------------------------

# wiek = int(input("Podaj swój wiek: "))

# if wiek < 13:
#     print("Child")
# elif 13 <= wiek <= 19:
#     print("Teen")
# elif 20 <= wiek <= 64:
#     print("Adult")
# else:
#     print("Senior")






# ------------------------------------------- ZADANIE 1.2.11 -------------------------------------------

# poprawny_login = "admin"
# poprawne_haslo = "1234"

# login = input("Podaj login: ")
# haslo = input("Podaj hasło: ")

# if login == poprawny_login and haslo == poprawne_haslo:
#     print("Zalogowano poprawnie")
# else:
#     print("Błędne dane logowania")






# ------------------------------------------- ZADANIE 1.2.12 -------------------------------------------

# wiek = int(input("Podaj wiek: "))

# if wiek < 18 or wiek >= 65:
#     print("Przysługuje zniżka")
# else:
#     print("Brak zniżki")






# ------------------------------------------- ZADANIE 1.2.13 -------------------------------------------

# imie1 = input("Podaj imię pierwszej osoby: ")
# wiek1 = int(input("Podaj wiek pierwszej osoby: "))

# imie2 = input("Podaj imię drugiej osoby: ")
# wiek2 = int(input("Podaj wiek drugiej osoby: "))

# if wiek1 >= 18 and wiek2 >= 18:
#     print("Obie osoby są pełnoletnie")
# else:
#     print("Nie wszystkie osoby są pełnoletnie")






# ------------------------------------------- ZADANIE 1.2.14 -------------------------------------------

# x = float(input("Podaj pierwszą liczbę: "))
# y = float(input("Podaj drugą liczbę: "))

# if not (x < 0 and y < 0):
#     print("Przynajmniej jedna liczba nie jest ujemna")
# else:
#     print("Obie liczby są ujemne")






# ------------------------------------------- ZADANIE 1.2.15 -------------------------------------------

# ean = input("Podaj kod EAN-13: ")

# if len(ean) == 13 and ean.isdigit():

#     if ean[:3] == "590":
#         print("Poprawny kod EAN-13 - produkt z Polski")
#     else:
#         print("Poprawny kod EAN-13 - produkt z innego kraju")

# else:
#     print("Niepoprawny kod EAN-13")



















# ------------------------------------------- LISTA 1.3 -------------------------------------------
# -------------------------------------------------------------------------------------------------















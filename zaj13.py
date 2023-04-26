 def dodawanie(liczba1, liczba2):
     suma=liczba1+liczba2
     return suma
 def mnozenie(liczba1,liczba2):
     iloczyn=liczba1*liczba2
        return iloczyn

# print('podaj liczbe')
# pierwsza=int(input())
# print('podaj liczbe')
# druga=int(input())
# suma=dodawanie(pierwsza,druga)
# iloczyn=mnozenie(pierwsza,druga)
# print(suma)
# print(iloczyn)

# def dzialanie(liczba1):
#     suma=liczba1+liczba1
#     kwadrat=suma**2
#     wynik=kwadrat-1
#     return wynik

# print('podaj liczbe')
# pierwsza=float(input())
# wynik=dzialanie(pierwsza)
# print("wynik dzialaniea",wynik)


# def dlugosc(lista):
#     dlugosclisty=0
#     for i in lista:
#         dlugosclisty+=1
#     return dlugosclisty

    

# lista=[1,2,5,9,45,23,14,79,2135]
# dlugosclisty=dlugosc(lista)
# print(dlugosclisty)

# def najwiekszy(lista):
#     najwiekszy=0
#     for i in lista:
#         if i>najwiekszy:
#             najwiekszy=i
#     return najwiekszy

# def najmniejszy(lista):
#     najmniejszy=lista[0]
#     for i in lista:
#         if i<najmniejszy:
#             najmniejszy=i
#     return najmniejszy

# def nta(lista,n):
#     return lista[n]

# # def koniunkcja(p,q):
# #     if p==0 and q ==0:
# #         return 0
# #     elif p==1 and q ==0:
# #         return 0
# #     elif p==0 and q==1:
# #         return 1
# #     elif p==1 and q== 1:
# #         return 1

# def koniunkcja1(p,q):
#     return p*q

# lista=[9,6,5,98,654,217,8,1]
# maxlisty=najwiekszy(lista)
# print(maxlisty)

# minlisty=najmniejszy(lista)
# print(minlisty)

# print('podaj n')
# n=int(input())
# nta=lista[n]
# print(nta)

# print("podaj p i q")
# p=int(input())
# q=int(input())
# print(koniunkcja1(p,q))


def gwiazdka(liczba):
    for i in range(liczba):
        print('*')
        
liczba=int(input())
print(gwiazdka)



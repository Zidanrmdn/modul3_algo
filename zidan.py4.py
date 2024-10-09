# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:40:49 2024

@author: ASUS
"""
print("=====Selamat datang di Segitiga Detektor=====")
while True:
    a = float(input("masukkan isi sisi A: "))
    b = float(input("masukkan isi sisi B: "))
    c = float(input("masukkan isi sisi C: "))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("segitiga sama sisi")
        elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            print("segitiga siku-siku")
        else:
            print("segitiga sembarang")
    else:
        print("bukan segitiga")
    print("Terima Kasih!")
    ulang = input("Apakah ingin mencoba lagi? (Y/T): ").lower()
    if ulang != 'y':
        break
print("=====Terima Kasih=====")


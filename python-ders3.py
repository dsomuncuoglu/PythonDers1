# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 00:26:54 2021

@author: DenizS
"""

#%% Fonksiyon İşlemleri - Basit fonksiyon oluşturma


def basitfonksiyon():
    print("Merhaba Python, ilk fonksiyon")

basitfonksiyon()
#%% Değer alan fonksiyon

def degerfonksiyon(kadi,sifre):
    print("Kullanıcının Adi=",kadi,"Kullanıcı sifresi=",sifre)

degerfonksiyon("deniz", "1234")
degerfonksiyon("ahmet", "ahmet1")

#%% Değer alan fonksiyon-2 --- Birden fazla deger gönderilmesi halinde istenen değerin alıması

def degerfonksiyon2(*kadi):
    print("Kullanıcının Adi=",kadi[1])
    print("Kullanıcının Adi=",kadi[3])

degerfonksiyon2("123","ahmet","1998","mehmet")

#%% Deger alan fonksiyon-3 --- Fonksiyona varsayılan değer atama işlemi


def degerfonksiyon3(kadi="Deniz",sifre="1234"):
    print("Kullanıcının Adi=",kadi,"Kullanıcı sifresi=",sifre)

degerfonksiyon3() # Boş yollanınca varsayılan değer gelir ve hata vermez.

#%% Deger döndüren fonksiyon

def degerdondurenfonk(sayi):
    return sayi**2
giris=int(input("Girilen sayının 2 üssünü buluncaktır. Bir sayi giriniz="))
print(degerdondurenfonk(giris))

#%% Fonksiyonlar kullanarak girilen sayının negatif veya pozitif olduğunu bulan program

def nnp(sayi):
    if(sayi<0):
        print("Sayi negatiftir.")
    elif(sayi>0):
        print("Sayi pozitiftir.")
    else:
        print("Sayi sıfıra eşittir.")

girisdegeri=int(input("Sayi giriniz="))
nnp(girisdegeri)

#%% Fonksiyonlar kullanarak girilen sayının faktoriyelini bulma

def faktoriyel(sayi):
    if sayi==1:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)

girisdegeri=int(input("Faktoriyelini istediğiniz sayıyı giriniz="))
print(faktoriyel(girisdegeri))

#%%

def faktoriyel(sayi):
    if sayi==1 or sayi==0:
        return 1
    elif sayi>0:
        return sayi*faktoriyel(sayi-1)
    else:
        print("negatif olamaz")

girisdegeri=int(input("Faktoriyelini istediğiniz sayıyı giriniz="))
print(faktoriyel(girisdegeri))
"""if faktoriyel(girisdegeri)==False:
    print("Negatif sayıların faktoriyeli bulunamaz")
else:
    print(faktoriyel(girisdegeri))"""

#%% Fonksiyon kullanarak liste oluşturma ve kullanıcıdan değerleri isteme

def liste(adet):
    sayilar=[]
    for x in range(adet):
        print(x+1,".sayiyi giriniz=")
        sayi=int(input())
        sayilar.append(sayi)
    return sayilar

kacadet=int(input("Liste kaç elemanlı olsun="))
print(liste(kacadet))

#%% Modüller

import modul2 as mdl

mdl.ilkfonk("Ahmet")

x=mdl.kisi.values()
print(x)

mdl.kisi[0]="Mehmet"
print(x)

#%% Hazır modül kullanımı

import platform as plt

print(plt.system())

#%% Bir modülün tüm işlevlerini kullanmak için dir kullanılır.

import platform as plt

print(dir(plt))

print(plt.win32_ver())


import numpy as np 

print(dir(np))


#%% Modüllerde from kullanımı -- sınırlı fonksiyon kullanımı

from modul2 import kisi

print(kisi["ulke"])

#%% Datetime modülü ile haftanın çalışma gününde olup olmadığını gösteren program

from datetime import datetime

def gunkontrol(girilentarih):
    gun=girilentarih.weekday()
    if gun<5:
        return True
    else:
        return False

if gunkontrol(datetime.now()):
    print("Hafta içi çalışma günü")
else:
    print("Hafta sonu tatil günü.")

#%% Sınıflar ve Nesneler

class ilksınıf:
    x=19
    
print(ilksınıf()) # bellekteki yerini gösterir.

nesne=ilksınıf()
print(nesne.x) # Nesne oluşturulduktan sonra x değeri çağırılır.

#%% Sınıf ve Nesneler içerisinde __init__ kullanımı

class sinif:
    def __init__(self,ad,yas):
        self.ad=ad
        self.yas=yas

nesne=sinif("Ahmet",19)

print(nesne.ad)
print(nesne.yas)

nesne.yas=65        # nesneyi güncellemek için
print(nesne.yas)

del nesne.yas       # nesneyi içerisinde tanımlanan değişkeni silmek için

del nesne           # nesneyi tamamen silmek

#%% Sınıf ve Nesnelerde - Nesne Yöntemleri

class sinif:
    def __init__(self,ad,yas):
        self.ad=ad
        self.yas=yas
    def merhaba(self):
        print("Merhaba, benim adım ",self.ad)
nesne=sinif("Mehmet", 21)
nesne.merhaba()

#%% Sınıf ve Nesnelerde - Self (self değişkeni değiştirilebilirdir.)

class sinif:
    def __init__(selfdegistir,ad,yas):
        selfdegistir.ad=ad
        selfdegistir.yas=yas
    def merhaba(selfdegistir2):
        print("Merhaba, benim adım ",selfdegistir2.ad)
nesne=sinif("Mehmet", 21)
nesne.merhaba()

#%% Class tanımlaması yapılırken içerik boş geçilemez. Boş geçmek istenirse pass tanımı kullanılır.

class bossinif:
    pass            # sistemin hata vermesi önlendi.



#%%
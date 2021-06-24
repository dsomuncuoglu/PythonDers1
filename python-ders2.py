# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:23:38 2021

@author: DenizS
"""

#%% List-Tanımlama-Arama

meyveler=["elma","armut","portakal"] # liste oluşturma 
print(meyveler)
print(type(meyveler))

meyveler2=list(("elma","armut","portakal")) # liste oluşturma 2
print(meyveler2)
print(type(meyveler2))


sayilar=[1,2,3,4]
durumlar=[True,False]
karma=["elma",1,True]

print(karma)
print(type(karma)) # karma değişkenin tipini gösterir.

print(len(meyveler)) # liste eleman sayısını belirtir.
print(len(sayilar))
print(len(karma))

print(karma[:1]) # String özelliği burada geçerlidir.

#%% List devam...
if "elma" in karma:
    print("liste içerisinde elma elemanı bulunmuştur.")
else:
    print("eleman bulunamadı.")
    
meyveler=["elma","armut","portakal","muz","erik"]
print(meyveler)

meyveler[2]="PORTAKAL"
print(meyveler)

meyveler.insert(2, "ananas") # indeks elemanın önüne eklenir.
print(meyveler)
meyveler.append("çilek") # listenin sonuna ekler
print(meyveler)

#%% Listeleri birleştirme

meyveler1=["elma","erik"]
meyveler2=["portakal","ananas"]

meyveler1.extend(meyveler2) # meyveler1 listesine meyveler2 elemanlarını ekleme
print(meyveler1)

meyveler1.remove("elma") # listeden "elma" adındaki değişkeni sil
print(meyveler1)

del meyveler1[2] # listeden 2.ci elemanı sil
print(meyveler1)

meyveler1.pop(1) # listeden 1.ci elemanı çıkarma
print(meyveler1)

meyveler2.clear() # listenin içerisini tamamen temizleme(silme)
print(meyveler2)

#%% Döngü ile Liste kontrolü

gunler=["pazartesi","sali","carsamba","persembe","cuma","cumartesi","pazar"]

for y in gunler:
    print(y)

for x in gunler:
    print(x[:3]) # liste elemanlarının ilk üç harfini yazdırma

for gun in range(len(gunler)):
    print("Listenin",gun,gunler[gun])
    
yeniliste=[]

for z in gunler:  # içerisinde "a" harfi olan liste elemanlarını yeniliste ye ekle
    if "a" in z:
        yeniliste.append(z)
print(yeniliste)

yeniliste2=[]
for z in gunler:  # içerisinde "a" harfi olmayanları liste elemanlarını yeniliste2 ye ekle
    if "a" not in z:
        yeniliste2.append(z)
print(yeniliste2)

#%% While ile liste kontrolü

i=0
while i<len(gunler):
    print("Listenin",i,gunler[i])
    i+=1

#%% Listeyi küçükten büyüğe sıralama

meyveler.sort()
print(meyveler)

sayilar2=[1,54,42,66,11,99]

sayilar2.sort()
print(sayilar2)

#%% Listeyi büyükten küçüğe sıralama

meyveler.sort(reverse=True)
print(meyveler)

sayilar2=[1,54,42,66,11,99]

sayilar2.sort(reverse=True)
print(sayilar2)

#%% Listeyi başka listeye kopyalamak

bosliste=[]

bosliste=gunler.copy() # 1. kopyalama yöntemi
print(bosliste)

bosliste2=[]

bosliste2=list(gunler) # 2. kopyalama yöntemi
print(bosliste2)

#%% Listeleri birleştirme

list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2 # liste birleştirme birinci yöntem
print(list3)

for x in list2:
    list1.append(x) # liste birleştirme ikinci yöntem
print(list1)

list1.extend(list2) # liste birleştirme üçüncü yöntem
print(list1)

#%% Tuple

flowers=('Lale','Gül','Papatya','Orkide')

flowers2=tuple(('Lale','Gül'))

print(flowers)
print(flowers2)

print(type(flowers))
print(type(flowers2))

stringtuple=("elma","armut")
sayituple=(1,2,3,4)
booltuple=(True,False,True)
karmatuple=("elma",1,True)

print(stringtuple)
print(sayituple)
print(booltuple)
print(karmatuple)

print(len(sayituple))

print(sayituple[:2])

if 1 in sayituple:
    print("sayi tuplenın içerisinde 1 elemanı bulunmaktadır.")
else:
    print("sayı tuplenın içerisinde aranan eleman bulunmamaktadır.")

#%% Tuple 'ı bir listeye dönüştürme işlemi (tuple olduğunda içerisinden eleman silinemez veya 
# eklenemez. O yüzden tuple'ı listeye dönüştürmemiz gerekir.)

x=("elma","armut")
y=list(x)
y.append("kivi") # liste yapıldıktan sonra silme işlemi gerçekleştirildi.
y.remove("elma") # liste yapıldıktan sonra ekleme işlemi gerçekleştirildi.
x=tuple(y)

print(x)

#%% Tuple for kullanımı 

ulkeler=("Türkiye","Almanya","Bulgaristan","Maceristan")

for x in ulkeler:
    print(x)

for y in range(len(ulkeler)):
    print(ulkeler[y])
#%% Tuple while kullanımı

i=0
while i<len(ulkeler):
    print(ulkeler[i])
    i+=1

#%% Tuple birleştirme işlemi

tuple1=("araba","kamyon")
tuple2=(1,2,3)
tuple3=tuple1+tuple2

print(tuple3)

#%% Tuple çoğaltma işlemi

meyvelertuple=("elma","armut")
yenituple=meyvelertuple*2
print(yenituple)

#%% Tuple daki aranan değerin kaç kaz görüldüğü

ornektuple=(1,2,4,6,8,6,3,6,5,6)

sayac=ornektuple.count(6)

print(sayac)

#%% Tuple daki aranan degerin hangi indekste oldugunu gösterir.

ornektuple2=(2,3,4,5,6,6,6,7,8)

indeks=ornektuple2.index(7)

print(indeks)

#%% Set-kümeler (Yinelenen üyeler tek üyemiş gibi davranırlar.)

# Set oluşturma

kitapturleri={"roman","hikaye","destan","oyku","roman"}
print(kitapturleri)

arabamarkasi=set(("bmw","mercedes","opel","renault","bmw"))
print(arabamarkasi)

if "bmw" in arabamarkasi:
    print("bulundu.")
else:
    print("bulunamadı.")

print(len(kitapturleri))
print(len(arabamarkasi))

set1={"a","b","c"}
set2={1,2,3,4}
set3={True,False}
karmaset={"a",1,True}

# Set birleştirme
set4=set1.union(set2)
print(set4)

#%% Set for kullanımı

for x in kitapturleri:
    print(x)
#%% Set deger ekleme

ucak={"airbus a380","airbus a300"}
print(ucak)
ucak.add("boeing 737")
print(ucak)


setucak={"airbus a380","airbus a300"}
print(setucak)
setguncelle={"boeing 787","boeing 747"}
setucak.update(setguncelle)
print(setucak)

#%% Set öğe çıkarma


setucak.pop()# Set içerisinden bir öğeyi kaldırma-çıkarma ilk öğe çıkar
print(setucak)

setucak.remove("airbus a380")# yöntem.1
print(setucak)

setucak.discard("airbus a300")# yöntem.2
print(setucak)

setucak.clear()# set içersini tamamen temizleme
print(setucak)

del setucak # set'i tamamen silme

#%% Set ile for kullanımı

for x in kitapturleri:
    print(x)

#%% Set yineleme gösterme

x={"telefon","pc","tablet"}
y={"tablet","mobil","bilgisayar"}
x.intersection_update(y)
print(x)

#%% Yinelenlerle yeni bir set oluşturma

x={"telefon","pc","tablet"}
y={"tablet","mobil","bilgisayar"}
z=x.intersection(y)
print(z)

#%% Yinelenen ögeleri çıkarma

x={"telefon","pc","tablet"}
y={"tablet","mobil","bilgisayar"}
x.symmetric_difference_update(y)
print(x)

#%% Yinelenleri çıkarıp yeni bir set oluşturma

x={"telefon","pc","tablet"}
y={"tablet","mobil","bilgisayar"}
z=x.symmetric_difference(y)
print(z)

#%% Dictionary oluşturma

arac={
      "Marka":"Tesla",
      "Model":"Model X",
      "Electric":True,
      "Yıl":2019,
      "Renk":["kırmızı","siyah","beyaz","mavi"]
      }
print(arac)
print(len(arac))
print(type(arac))

yıl=arac["Yıl"]
print(yıl)

marka=arac.get("Marka")
print(marka)

deger=arac.values()
print(deger)

arac["Yıl"]="2018"
print(arac)

arac.update({"Model":"Model 3"})
print(arac)

arac["Vites"]="Otomatik"
print(arac)

#%% Dictionary öge silme

arac.pop("Vites")
print(arac)

arac.popitem() # rastgele bir şekilde bir öge siler.
print(arac)

del arac["Marka"]
print(arac)

arac.clear() # içerisindeki tüm öğeleri siler. Dictionary kalır.
print(arac)

del arac # dictionary 'i tamamen silme işlemi

#%% Dictionary for kullanımı 

for x in arac: # sadece anahtar adı döngüsü olur.
    print(x)

for y in arac: # sadece değişkenleri döndürür.
    print(arac[y])

for z in arac.keys(): # sadece anahtar adı döngüsü olur.
    print(z)

for c in arac.values(): # sadece değişkenleri döndürür.
    print(c)
    
for v in arac.items(): # sözlüğün tüm elemanlarını gösterir.
    print(v)
    
#%%  Dictionary kopyalama

yenidict=arac.copy()
print(yenidict)

yenidict2=dict(arac)
print(yenidict2)

#%% Dictionary içerisinde dictionary oluşturma

sinif={
      "ögrenci":{
          "adi":"deniz",
          "yıl":"1998"
          },
      "ögrenci2":{
          "adi":"furkan",
          "yıl":"1997"
          },
      "ögrenci3":{
          "adi":"mahmut",
          "yıl":"1999"
          }
      }

print(sinif)


#%% Dictionary içerisinde dictionary oluşturma-2

ögrenci={
          "adi":"deniz",
          "yıl":"1998"
          },
ögrenci2={
          "adi":"furkan",
          "yıl":"1997"
          },
ögrenci3={
          "adi":"mahmut",
          "yıl":"1999"
          }
sinif={
       "ögrenci1":ögrenci,
       "ögrenci2":ögrenci2,
       "ögrenci3":ögrenci3
       }
print(sinif)






#%%
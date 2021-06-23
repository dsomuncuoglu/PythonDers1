# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:04:20 2021

@author: DenizS
"""

#%%
print("Merhaba Dünya")# Bu tek satırlı yorumlayıcıdır.
print("Hello World")
'''
Bu da çoklu yorum satırıdır.
'''

#%% Bir sayının negatif-pozitif ve sıfıra eşit olup olmadığını bulan python kodu

sayi=-1

if(sayi<0):
    print("Sayi negatif")
elif(sayi>0):
    print("Sayi pozitif")
else:
    print("Sayi sıfıra esittir.")



#%% Klavyeden girilen sayı 0 değil iken; klavyeden girilen sayıları çarpma (while loop)

deger=1
carp=1
while deger!=0:
    carp*=deger
    print(carp)
    deger=int(input("Sayi gir="))




#%% 4'den başlayarak 55'e kadar olan sayıları 10'ar 10'ar arttır. (for loop)

for sayi in range(4,55,10):
    print(sayi)     

#%% Metin içerisindeki 'x' harfini görünce dur.

metin="merhaba x dünya"

for x in metin:
    if(x=="x"):
        break
    print(x)



#%% Metin içerisindeki 'x' harfini görünce ekrana yazdırma.

metin="merhaba x dünya"

for x in metin:
    if(x=="x"):
        continue
    print(x)
    
#%% Boolean

print(10<9)

print(10>9)

print(10==9)

x=200
print(isinstance(x,int))

#%% Değişkenin türünü öğrenim ve belirtimi

tamsayi=100
ondaliklisayi=1.5
metin="Merhaba"

print(type(metin))
print(type(tamsayi))
print(type(ondaliklisayi))

#%% Tür dönüşümü

metin2="35"
metin3="1.5"

degisken=(int(metin2))

degisken2=(float(metin3))

print(degisken)
print(degisken2)

print(type(degisken))
print(type(degisken2))

#%% Çoklu değişken işlemleri

x,y,z="Elma", "Armut", "Portakal"

print(x)
print(y)
print(z)

#%% Birden çok değişkene bir tane değer atama

x=y=z="Elma"

print(x)
print(y)
print(z)

#%% Paketten çıkarma işlemleri (tuple)

meyveler="Elma", "Armut", "Portakal"

x,y,z=meyveler

print(x)
print(y)
print(z)

#%% Rastgele sayı üretme

import random

rastgele=random.randrange(0,10)

print(rastgele)
#%% Değişken birleştirme

x,y,z="Elma", "Armut", "Portakal"

print(x+y+z)

print(x,y,z)

#%% Kullanıcının veri girişi yapması

kullaniciadi=input("Kullanıcı adını girin=")
print("Kullanıcı adınız=",kullaniciadi)

#%% Kullanıcının sayi girişi

sayi1=int(input("Birinci sayiyi girin="))
sayi2=int(input("ikinci sayiyi girin="))

print("Girilen birinci sayi=",sayi1,"Girilen ikinci sayi=",sayi2,"Toplam=",sayi1+sayi2)

#%% Python'daki oparatörleri

x=3
y=3

print(x%y)  # mod alma işlemi
print(x**y) # üs alma işlemi
print(x//y) # katmanlı bölme

#%% Karşılaştırma operatörleri

x=3
y=6

print(x<y)
print(x>y)
print(x>=y)
print(x<=y)
print(x==y)

#%% Karşılaştırma operatörleri 2
x=19
y=3
if(x>=y):
    print("x büyük veya eşittir.")
if(x!=y):
    print("x y'ye eşit değildir.")
if(x==y):
    print("x y'ye eşittir.")

#%% Atama operatörleri

x=19

x+=4
print("x degeri",x)

x*=4
print("x'in yeni degeri",x)

x%=5
print("x'in yeni degeri",x)

x//=3
print("x'in yeni degeri",x)
#%%
y=3

while y<7:
    print("y nin degeri",y)
    y+=3
    
else:
    print("işlem bitmiştir.")

#%%
y=0

while y<7:
    y+=1
    if(y==5):
        continue
    else:
        print(y)

#%% Mantıksal operatörler (and,or,not)

x=35

if(x>30 and x<37):
    print("Sayi 30 ile 32 arasındadır.")

#%% Mantıksal operatörler 2

x=int(input("Bir sayı giriniz="))

y=bool(x>10 and x<15)

while(y==True and x<30):
    x+=1
    print(x)
else:
    print("Girilen sayı 10 ile 15 arasinda olmalıdır.")
    
#%% Klavyeden girilen üç sayıdan en büyüğünü bulma

x=int(input("Birinci sayıyı giriniz="))
y=int(input("İkinci sayıyı giriniz="))
z=int(input("Üçüncü sayıyı giriniz="))

if(x==y and x==z):
    print("Degerler birbirine eşittir.")
elif(x>=y and x>=z):
    print(x," degeri en büyük sayıdır.")
elif(y>=x and y>=z):
    print(y," degeri en büyük sayıdır.")
elif(z>=x and z>=y):
    print(z," degeri en büyük sayıdır.")


#%% Klavyeden girilen üç sayıdan büyükten küçüğe sıralama

x=int(input("Birinci sayıyı giriniz="))
y=int(input("İkinci sayıyı giriniz="))
z=int(input("Üçüncü sayıyı giriniz="))

if(x==y and x==z):
    print(x,"=",y,"=",z)
else:
    if(x>y and x>z):
        if(y>z):
            print(x,y,z)
        else:
            print(x,z,y)
         
    elif(y>x and y>z):
        if(x>z):
            print(y,x,z)
        else:
            print(y,z,x)
    
    elif(z>x and z>y):
        if(x>y):
            print(z,x,y)
        else:
            print(z,y,x)

#%%

x=["elma","muz","armut"]
y=["elma","muz","armut"]

z=x

print(x is y)

print(x is z)


if(z is x):
    print("diziler aynıdır.")

if("elma" in x):
    print("dizi içerisinde mevcuttur.")
else:
    print("dizi içerisinde mevcut değildir.")
#%% String
a="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

print(a)

print(a[0])# ilk harfi verir.

print(a[0:5])# 0 ile 5 karakter arasını yazdırır.

print(a[:5])# baştan 5.ci karakter arasını yazdır.

print(a[2:])# 2. karakterden sonuna kadar yazdır.

print(a[-5:])# karaketerleri sondan itibaren yazar.(negatif)

print(a.upper()) # metini büyük harf ile yazar.

print(a.lower()) # metini küçük harf ile yazar.

print(a.strip()) # metindeki boşlukları kaldırma

for x in a[0:11]: # 0 ile 11 karakterleri arasındaki metini teker teker ekrana basar
    print(x)
#%% String 2
print(len(a)) # dizenin uzunluğunu verir.

print("text" in a) # a stringinde "text" kelimesi var mı? 

print("text" not in a) # a stringinde "deniz" kelimesi yok.

if "text" in a:
    print("aranan metin bulundu.")
else:
    print("aranan metin bulunamadı")

#%% String 3

yas=23
adi="Deniz"
maas=5000

metin="Merhaba, benim Adım {}. Yaşım {}. Maasım {} TL'dir."

print(metin.format(adi,yas,maas))

#%%
x=int(input("Birinci sayıyı giriniz="))
y=int(input("İkinci sayıyı giriniz="))
z=int(input("Üçüncü sayıyı giriniz="))
degermetin="en büyük deger {}, ortanca deger {}, küçük deger {}"
if(x==y and x==z):
    print(x,"=",y,"=",z)
else:
    if(x>y and x>z):
        if(y>z):
            print(degermetin.format(x,y,z))
            
        else:
            print(degermetin.format(x,z,y))
         
    elif(y>x and y>z):
        if(x>z):
            print(degermetin.format(y,x,z))
        else:
            print(degermetin.format(y,z,x))
    
    elif(z>x and z>y):
        if(x>y):
            print(degermetin.format(z,x,y))
        else:
            print(degermetin.format(z,y,x))



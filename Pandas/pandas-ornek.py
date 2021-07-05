# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 12:14:50 2021

@author: DenizS
"""

#%% Pandas kütüphanesini import etmek

import pandas as pd
import numpy as np

#%%

liste=[1,2,3,4,5]

pandas_list=pd.Series(liste)

print(pandas_list)

#%%

index_list=['a','b','c','d','e']

pandas_index=pd.Series(liste,index_list)

print(pandas_index)

#%%

sozluk={'ahmet':'forvet',
        'mehmet':'defans',
        'eren':'kaleci',}

pandas_sozluk=pd.Series(sozluk)

print(pandas_sozluk)

#%% Attributes

print(pandas_list.T)

print(pandas_list.dtypes)

print(pandas_list.is_unique)

print(pandas_list.size)

#%% Methods

print(pandas_list.head())

print(pandas_list.head(2))

print(pandas_list.describe())

print(pandas_sozluk.describe())



#%%

seri=pd.Series(data=liste,index=(index_list))

print(seri)

#%%

calisanlar=["ahmet","ece","emre"]
maaslar=[1000,2000,1000]

seri2=pd.Series(data=maaslar,index=(calisanlar))

print(seri2)

#%% CSV okuma

okuma=pd.read_csv("sarkicilar.csv")

print(okuma)


#%% CSV to pd.Series()

read=pd.read_csv("gunler.csv",usecols=(["Günler"]),squeeze=(True))

print(read)

#%% Python Built-in Functions

liste2=[1,2,3,4,66,2,55,41]

print(len(liste2))

sozluk_conv=dict(seri)

print(sozluk_conv)

#%% Serilerde sıralama

print(sorted(liste2,reverse=1)) # Büyükten küçüğe sıralama

print(sorted(liste2)) # Küçükten büyüğe sıralama

print(read.sort_values()) # Serilerde sıralama , küçükten büyüğe

print(read.sort_values(ascending=False)) # Serilerde sıralama, büyükten küçüğe


#%% İnplace Parametres

read.sort_values(inplace=True) # Küçükten büyüğe sıralama işlemini kalıcı hale getirme

print(read)

#%% İndekse göre sıralama işlemi

print(read.sort_index())

read.sort_index(inplace=True) # read değişken içeriği sıralamaya göre değiştirildi.

print(read)

#%% Gunler serisinde değerin olup olmadığının kontrolü

print("Pazartesi" in read.values)

#%%

gunler=pd.read_csv("gunler.csv",index_col='Günler',squeeze=(True))

print(gunler["Pazartesi"])

#%% Üstteki işlemin aynısını yapar

print(gunler.get("Pazartesi"))

#%%

print(gunler.get("Monday",default="aranan gün bulunamadı"))

#%% get(key)

print(gunler.get(key=["Pazar","Pazartesi","Salı"],default="aranan gün bulunamadı"))

#%% Max-Min Özellikleri

randList=np.random.randint(10,100,15)

randSeri=pd.Series(randList)

print(randSeri)

print(randSeri.max())

print(randSeri.min())

print(randSeri.idxmax())

#%% Apply Metodu

def ikiEkle(sayi):
    return sayi+2

print(randSeri.apply(ikiEkle)) # Bir fonksiyon ile Serinin değerlerini değiştirme


#%% Map Metodu

calisanlar2=["ahmet","ece","emre","buşra","cuneyt","deniz","gizem","efe"]

calisanlarSeri=pd.Series(calisanlar2)

print(calisanlarSeri)

kuraSonuc={"ahmet":5,
           "ece":2,
           "emre":0,
           "buşra":1,
           "cuneyt":6,
           "deniz":3,
           "gizem":4,
           "efe":7}

kuraSerisi=pd.Series(kuraSonuc)

print(kuraSerisi)

mapping=kuraSerisi.map(calisanlarSeri)

print("Kura Çekiliş Sonucu\n",mapping)


#%% DataFrame

df=pd.read_csv('calisan_data.csv')

print(df)

print(df.isnull()) # Dataframe içerisinde null değerler boolean ile döner.

print(df.isnull().sum()) # Fonksiyon bağlama , toplamda sütunlardaki null değerleri gösterir.

matris=df.values

print(matris) # Dataframe np_array'e çevirme

print(matris[0,0])

print(df.Isimler)

print(df.dtypes)

print(df.describe())

print(df.columns)

print(df.shape)

print(df.info())

#%% Replace columns name

df.rename(columns={"DogumTarihi":"Doğum Tarihi"},inplace=True)

print(df["Doğum Tarihi"])

print(df[["Doğum Tarihi","Maas"]])

#%% Toplam maas bulma

toplammaas=0
for m in df.Maas:
    toplammaas+=m

print(toplammaas)

print(df.Maas.sum())


#%%

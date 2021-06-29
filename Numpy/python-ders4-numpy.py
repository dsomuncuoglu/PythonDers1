# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:46:46 2021

@author: DenizS
"""

#%% Numpy oluşturma

import numpy as np

ND=np.array([1,2,3,4,5])
print(ND)
print(type(ND))

PL=[1,2,3,4,5]
print(PL)

#%% ND array 2 boyutlu matris

ND=np.array([[1,2,3,4,5],[1,2,3,4,5]])

print(ND)

print(ND.shape) # ND array'in boyutlarını gösterir.

print(ND.ndim)  # ND array'in boyutunu gösterir.

print(ND.dtype) # ND array'in içerisindeki veri tipini belirtir.

print(ND.size)  # ND array'in içerisindeki eleman sayısını belitir.

#%% ND array 3 boyutlu matris

ND3=np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])

print(ND3)

print(ND3.shape)

print(ND3.ndim)

print(ND3.size)
#%% Sıfır boyutlu ND array (nokta)

ND0=np.array(4)

print(ND0)

print(type(ND0))

print(ND0.ndim)

#%%

ND2=np.zeros((11,10))

print(ND2)

print(ND2.ndim)
#%%
ND3=np.ones((4,3))

print(ND3)

print(ND3.dtype)
#%% np.full

ND3=np.full((3,3),7)

print(ND3)

#%% np.eye BİRİM MATRİS OLUŞTURUR

ND3=np.eye(5)

print(ND3)

#%% np.diag BELİRLENEN DEĞERLERİN DİAGONAL BİÇİMDE MATRİSE YERLEŞMESİNİ SAĞLAR

ND3=np.diag([3,7,9,0,3,4,5])

print(ND3)

#%% np.arange belirlenen değere kadar tek boyutlu dizi oluşturur.

ND=np.arange(20) 

print(ND)

ND2=np.arange(5,12) #[baslangıc,son]

print(ND2)

ND3=np.arange(6,18,5) #[baslangıc,son,artış miktarı]

print(ND3)
#%% np.arange(20).reshape(4,5) belirlenen değeri 2 boyutlu bir matris halinde dönüştür

ND=np.arange(20).reshape(4,5) # reshape yapılırken eleman sayısından fazla yada az olamaz.

print(ND)
#%% Satır ve sütunlardaki değerlere ulaşma
# Birinci Yöntem
print(ND[2][1]) # 5 sayısına ulaşmak için = satır ve sütun bilgisi girilir.
# İkinci Yöntem
print(ND[2,1])  # İndeksler 0'dan başlar.    

print(ND[1]) # İkinci satırı komple getirir. (Baştan başlayarak satırı gösterir.)

print(ND[-1]) # İkinci satırı komple getirir. (Sondan başlayarak satırı gösterir.)

print(ND[:,1]) # İkinci sütun elemanlarını komple getirir.(Baştan başlayarak sütunu gösterir.)

print(ND[:,-1]) # İkinci sütun elemanlarını komple getirir.(Sondan başlayarak sütunu gösterir.)

print(ND[1:3]) # İki satır arasını alma

print(ND[1:4,1:4]) # Seçilen satır ve sütun arasını alma

print(ND[-2,-2]) # Satır ve sütuna sondan bakılırak sonuca ulaşılır.
#%% Satır ve sütunlardaki değerleri değiştirme işlemleri

ND[0,0]=99 # Satır ve sütunu girilen değerin değerini değiştirme işlemi
print(ND)

ND[:,2]=45 # Üçüncü sütundaki tüm değerleri değiştirme
print(ND)

#%% Satır, sütun veya değer silme işlemleri

ND=np.delete(ND, 2,axis=1) # Üçüncü sütunun değerlerini silme(axis=1 sütun)
print(ND)

ND=np.delete(ND, 0,axis=0) # Birinci satır değerlerini silme(axis=0 satır)
print(ND)

ND=np.delete(ND, -1,axis=0) # Sondan birinci satır değerlerini silme(axis=0 satır)
print(ND)

ND=np.delete(ND, -2,axis=1) # Sondan ikinci sütunun değerlerini silme(axis=1 sütun)
print(ND)

#%% Satır, sütun veya değer ekleme işlemleri

ND=np.append(ND, [[7,7,7]],axis=0) # Belirlenen değerleri append(son) satıra eklenme(axis=0 satır) 
print(ND)

ND=np.insert(ND,0,[[6,6,6]],axis=0) # Belirlenen değerleri insert(baş) satıra ekleme(axis=0 satır)
print(ND)

ND=np.append(ND, [[1],[1],[1],[1],[1],[1.1]],axis=1) 
# Belirlenen değerleri append(son) sütuna eklenme(axis=1 sütun) 
# Belirlenen değerler hem satır hem sütun oldukları için [[1],[1],[1],[1],[1],[1]] bu şekide kullanılır.
print(ND)

ND=np.insert(ND,1,[5,15,25,35,45,5],axis=1) # Belirlenen değerleri insert(baş) satıra ekleme(axis=1 sütun)
print(ND)

ND=np.insert(ND,0,[5],axis=1) # Belirlenen değerleri insert(baş) satıra ekleme(axis=1 sütun)
print(ND)
#%% Mastris parçalama

PARCA_ND=ND[1:4,2:4]
print(PARCA_ND)

PARCA_ND[0,0]=99 # Parcadaki eleman değişirse tam olan ND'de değişir.
print("--------------")
print(ND)


PARCA_ND2=ND[1:4,2:4].copy() # Parçayı kopyalarsak eleman değişirse ND'de değişme olmaz.
print(PARCA_ND2)

PARCA_ND2[0,0]=11

print("--------------")
print(ND)
#%% Rastgele ND oluşturma

ND_random=np.random.randint(0,10, (4,5))

print(ND_random)


print(ND_random>=5) # Array içersindeki değerlerin 5'e eşit veya büyük olduğunun kontrolü(bool)

print(ND_random[ND_random>=5]) # Array içersindeki değerlerin 5'e eşit veya büyük yazdırma

#%% Element - Wise

print(ND_random)
print("--------------------")
print(ND_random+2)


ND_random2=np.random.randint(0,10, (4,5))

print("Random_1")
print(ND_random)
print("Random_2")
print(ND_random2)

print("Toplam ND")
print(ND_random+ND_random2)


#%% Dosyalama işlemleri

data_1=np.loadtxt("studentAssessment.csv", delimiter=",",skiprows=1,dtype='S8' )

np.set_printoptions(suppress=True)

print(data_1)



#%%
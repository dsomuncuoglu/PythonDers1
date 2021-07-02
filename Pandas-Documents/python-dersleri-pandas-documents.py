# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:24:18 2021

@author: DenizS
"""
#%%
import numpy as np
import pandas as pd

#%% Nesne oluşturma islemi

s=pd.Series([1,3,5,np.nan,6,8])

print(s)
#%% DataFrame oluşturma işlemi- ilk sütununda tarihlerin belirlenme işlemi

dates= pd.date_range("20210101",periods=6)
print(dates)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
print(df)


#%% DataFrame oluşturma işlemi - Objeleri sözlük içerisinde oluşturup dizi haline dönüştürme

df2= pd.DataFrame({
    "A":1,
    "B":pd.Timestamp("20210102"), # Tarih belirleme işlemi
    "C":pd.Series(1,index=list(range(4)),dtype="float32"), # Float tipinde pandas dizisi
    "D":np.array([3]*4,dtype="int32"), # İnteger tipinde numpy dizisi 
    "E":pd.Categorical(["test","train","test1","train1"]), # Pandas kategori dizisi
    "F":"foo", # String veri tipi
    })
print(df2)
#%% DateFrame2 'nin veri tiplerini sonuçlarını gösteren işlem

print(df2.dtypes)

#%% Veri görüntüleme 

print(df2.head()) # Tüm verileri görme

print(df2.tail(1)) # Sondan gösterim için kullanılır. Sayı arttıkça başa yaklaşır.

#%% İndeks ve satır görüntüleme

print(df.index)

print(df.columns)

#%% DataFrame.to_numpy()

print(df.to_numpy())

print(df2.to_numpy())

#%% İstatistik özelliklerini gösterme işlemi

print(df.describe())

print(df2.describe())

#%% Verilerin transpozesi

print(df.T)

print(df2.T)

#%% Verilerin eksene göre sıralanması

print(df.sort_index(axis=1, ascending=False))


print(df2.sort_index(axis=1, ascending=False))

#%% Değerlerin sıralanması

print(df.sort_values(by="B"))

print(df2.sort_values(by="B"))

#%% Belirlenen bir sütunu yazdırma

print(df["A"])

#%% İstenen satırları gösterme

print(df[0:3])

print(df["20210103":"20210106"]) # Belirlenen tarihler arasını görüntüleme

#%% İstenilen etiketin görüntülenmesi

print(df.loc[dates[0]])

#%% İstenilen çoklu eksen etiketini görüntülenmesi

print(df.loc[:,["A","B"]])

#%% İstenilen çok eksenli etiketin baslangıc ve sonu degerinin belirtilmesi

print(df.loc["20210102":"20210104",["A","B"]])

#%% İstenilen tarih değerine göre A ve B etiketlerinin döndürdüğü değerler

print(df.loc["20210102",["A","B"]])

#%% Bir etiket içersindeki değerin çağrılması

print(df.loc[dates[0],"A"])

print(df.loc[dates[0],"B"])

print(df.loc[dates[0],"C"])

print(df.loc[dates[0],"D"])

#%% Bir etiket içersindeki değerin daha hızlı erişilmesi

print(df.at[dates[0],"A"])

print(df.at[dates[0],"B"])

print(df.at[dates[0],"C"])

print(df.at[dates[0],"D"])

#%% Pozisyona göre seçim işlemleri (Dilimleme) (Satır ve sütun çağrımları)

print(df.iloc[3]) # satır yazdırma

print(df.iloc[3:5,0:2]) # satır ve sütuna göre yazdırma

print(df.iloc[[1,2,4],[0,2]])

print(df.iloc[1:3,:]) # belirli satırlara göre tüm etiketleri yazdırma

print(df.iloc[:,1:3]) # belirli sütunlara göre tüm değerleri yazdırma

print(df.iloc[1,1])

print(df.iat[1,1])

#%% Boolean ifadeye göre indeksleri görüntüleme

print(df[df["A"]>0]) # A etiketinde pozitif değerlerine göre tüm etiketleri yazdırma

print(df[df>0]) # Tüm etiket değerlerinde pozitifleri yazdırma (negatifler NAN)

#%% isin() metodu kullanarak filtreleme

df3=df.copy()

df3["E"]=["one","one","two","three","four","three"]

print(df3)

print(df3[df3["E"].isin(["two","four"])]) 

# Oluşturulan E etiketindeki aranan kriterlere göre tüm etiketlerin gösterilmesi

#%% Yeni sütun ayarlarken verileri indekslere göre otomatik olarak yerleştirme

s1=pd.Series([1,2,3,4,5,6], index=pd.date_range("20210102",periods=6))

print(s1)

df["F"]=s1

print(df)

#%% Değerleri etiketlere göre 

df.at[dates[0],"A"]=0

print(df)

df.iat[0,1]=0

print(df)

df.loc[:,"D"]=np.array([5]*len(df))

print(df)

#%% 

df3=df.copy()

df3[df3>0]=-df3

print(df3)

#%%

df1=df.reindex(index=dates[0:4], columns=list(df.columns)+["E"])

df1.loc[dates[0]:dates[1],"E"]=1

print(df1)

#%% Verileri eksik olmayan satırların gösterilmesi

print(df1.dropna(how="any"))

#%% Eksik verilerin belirlenen değerler ile doldurulması

print(df1.fillna(value=5))

#%% Hangi değerlerin NAN(boş) olduğunu boolean ile gösterimi 

print(pd.isna(df1))

#%% Operasyon İşlemleri
# Genel olan işlemler, eksik verileri hariç tutar.
# Tanımlayıcı bir istatistik geliştirme işlemi

print(df.mean())

#%% Diğer eksende aynı işlemin yapılması

print(df.mean(1))

#%% 

s=pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)

print(s)

print(df.sub(s,axis="index"))


#%% Apply

print(df.apply(np.cumsum))

print(df.apply(lambda x:x.max()-x.min()))

#%% Histroglama

s=pd.Series(np.random.randint(0,7,size=10))

print(s)

print(s.value_counts())

#%% String Metodları

s=pd.Series(["A","B","C","Aaba","Baca",np.nan,"CABA","dog","cat"])

print(s.str.lower()) # tüm stringleri(değişkenleri) küçük harf yapar

print(s.str.upper()) # tüm stringleri(değişkenleri) büyük harf yapar

#%% String Birleştirme

df=pd.DataFrame(np.random.randn(10,4))

print(df)


#%%

pieces=[df[:3],df[3:7],df[7:]]

print(pd.concat(pieces))


#%% Join - SQL tarzı veri birleştirme

left=pd.DataFrame({"key":["foo","foo"],"lval":[1,2]})

right=pd.DataFrame({"key":["foo","foo"],"rval":[4,5]})

print(left)

print(right)

merge=pd.merge(left, right,on="key")

print(merge)


#%% 2

left=pd.DataFrame({"key":["foo","bar"],"lval":[1,2]})

right=pd.DataFrame({"key":["foo","bar"],"rval":[4,5]})

print(left)

print(right)

merge2=pd.merge(left, right,on="key")

print(merge2)

#%% Gruplama İşlemleri
# Splitting - Verileri bazı kriterlere göre gruplama
# Applying - Her gruba göre b#ağımsız fonksiyon belirleme
# Combining - Sonuçları bir veri yapısına birleştirme


df=pd.DataFrame({
    "A":["foo","bar","foo","bar","foo","bar","foo","foo"],
    "B":["one","one","two","three","two","two","one","three"],
    "C":np.random.randn(8),
    "D":np.random.randn(8)
    })

print(df)
#%% Gruplar arası veri toplanımı 

print(df.groupby("A").sum())

#%% Gruplar arası çoklu veri toplanımı

print(df.groupby(["A","B"]).sum())

#%% Reshaping - Yeniden biçimlendirme(şekillendirme)

tuples=list(zip(
    *[
      ["bar","bar","baz","baz","foo","foo","qux","qux"],
      ["one","two","one","two","one","two","one","two"],
      ]
    ))

index=pd.MultiIndex.from_tuples(tuples, names=["first","second"])

df=pd.DataFrame(np.random.randn(8,2),index=index,columns=(["A","B"]))

df2=df[:4]

print(df2)

#%% Dataframe sütunlarını bir seviyeye göre sıkıştırma

stacked=df2.stack()

print(stacked)


#%% Unstack işlemi (Sıkıştırma işlemini geri alma)

unstacked=stacked.unstack()

print(unstacked)

unstacked1=stacked.unstack(1) #first-second unstack

print(unstacked1)

unstacked2=stacked.unstack(0) # bar,baz,foo,... unstack

print(unstacked2)


#%% Pivot Table - Eksen Tablosu

df=pd.DataFrame({
    "A":["one","one","two","three"]*3,
    "B":["A","B","C"]*4,
    "C":["foo","foo","foo","bar","bar","bar"]*2,
    "D":np.random.randn(12),
    "E":np.random.randn(12),
    })

print(df)

#%%

pivot=pd.pivot_table(df,values=("D"),index=(["A","B"]),columns=("C"))

print(pivot)


#%% Zaman Dizileri (Time Series)

rng=pd.date_range("1/1/2021",periods=100,freq="S")

ts=pd.Series(np.random.randint(0,500,len(rng)),index=(rng))

resample=ts.resample("5Min").sum()

print(resample)

#%% Saat dilimi gösterimi

rng=pd.date_range("2/7/2021 00:00",periods=5,freq="D")

ts=pd.Series(np.random.randn(len(rng)),rng)

print(ts)


ts_utc=ts.tz_localize("UTC")

print(ts_utc)

#%% Başka saat dilimine çevirme

ts_convert=ts_utc.tz_convert("Turkey")

print(ts_convert)

#%% Zaman aralığı arasında dönüşüm

rng=pd.date_range("2/7/2021",periods=5,freq="M")

ts=pd.Series(np.random.randn(len(rng)),index=(rng))

print(ts)

ps=ts.to_period()

print(ps)

ps_timestamp=ps.to_timestamp()

print(ps_timestamp)

#%% 

prng=pd.period_range("1990Q1","2000Q4",freq="Q-NOV")

ts=pd.Series(np.random.randn(len(prng)),prng)

ts.index=(prng.asfreq("M","e")+1).asfreq("H","s")+10

print(ts.head())

#%% Pandas ta kategori işlemleri

df=pd.DataFrame({
    "id":[1,2,3,4,5,6],
    "raw_grade":["a","b","b","a","a","e"]
    })

df["grade"]=df["raw_grade"].astype("category")

print(df["grade"])


#%%

df["grade"].cat.categories=["very good","good","very bad"]

df["grade"]=df["grade"].cat.set_categories(["very bad","bad","medium","good","very good"])

print(df["grade"])


#%%

print(df.sort_values(by="grade"))

print(df.groupby("grade").size())

#%% Çizim işlemleri (Plotting)

import matplotlib.pyplot as plt

plt.close("all")

#%%

ts=pd.Series(np.random.randn(1000),index=(pd.date_range("2/7/2021",periods=1000)))

ts=ts.cumsum()

print(ts.plot())

#%%

df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=(["A","B","C","D"]))

df=df.cumsum()

plt.Figure()

df.plot()

plt.legend(loc='best')


#%% Veri giriş/çıkış işlemleri

# CSV

df.to_csv("foo.csv")

print(pd.read_csv("foo.csv"))

#%% HDF5

df.to_hdf("foo.h5","df")

print(pd.read_hdf("foo.h5", "df"))

#%% Excel

df.to_excel("foo.xlsx",sheet_name="Sheet1")

print(pd.read_excel("foo.xlsx","Sheet1",index_col=(None),na_values=(["NAN"])))







#%% type test
print(type("foo"))

#%%

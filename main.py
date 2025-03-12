# Python OOP Ödevi - main.py

# 1. Bir sınıf (class) oluşturma ve nesne üretme
class Ogrenci:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def bilgileri_goster(self):
        return f"Öğrenci: {self.ad}, Yaş: {self.yas}"

ogr1 = Ogrenci("Ahmet", 21)
print(ogr1.bilgileri_goster())

# 2. Kapsülleme (Encapsulation) Örneği
class BankaHesabi:
    def __init__(self, bakiye):
        self.__bakiye = bakiye  

    def bakiye_goster(self):
        return f"Bakiye: {self.__bakiye} TL"

    def para_cek(self, miktar):
        if miktar <= self.__bakiye:
            self.__bakiye -= miktar
            return f"{miktar} TL çekildi. Yeni bakiye: {self.__bakiye} TL"
        else:
            return "Yetersiz bakiye!"

hesap = BankaHesabi(1000)
print(hesap.bakiye_goster())
print(hesap.para_cek(200))

# 3. Kalıtım (Inheritance) Örneği
class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        return "Ses çıkarıyor..."

class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav!"

kedi1 = Kedi("Minnak")
print(kedi1.ses_cikar())

# 4. Polymorphism (Çok Biçimlilik) Örneği
class Kus:
    def ses_cikar(self):
        return "Cik cik!"

class Kopek:
    def ses_cikar(self):
        return "Hav hav!"

def hayvan_sesi(hayvan):
    print(hayvan.ses_cikar())

kus1 = Kus()
kopek1 = Kopek()

hayvan_sesi(kus1)
hayvan_sesi(kopek1)
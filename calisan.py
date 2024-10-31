class Calisan:
    def __init__(self,ad,pozisyon,maas):
        self.ad=ad
        self.pozisyon=pozisyon
        self.maas=maas
    def zamYap(self,miktar):
        self.maas+=miktar
        print(f"Maaş güncellendi:{self.maas} TL")
    def __str__(self):
        return f"{self.ad}, Pozisyon:{self.pozisyon}, Maaş:{self.maas} TL"

calisanlar={}

def calisanEkle():
    ad=input("Çalışanın adını giriniz:")
    pozisyon=input("Çalışanın pozisyonunu giriniz:")
    maas=float(input("Çalışanın maaşını giriniz:"))
    calisanlar[ad]=Calisan(ad,pozisyon,maas)
    print(f"Çalışan {ad} eklendi")
def calisanlariGoruntule():
    for calisan in calisanlar.values():
        print(calisan)
def anaFonksiyon():
    while True:
        print("1.Çalışan Ekle")
        print("2.Çalışanları Görüntüle")
        print("3.Zam yap")
        print("4.Çıkış")
        secim=int(input("Bir seçim yapınız:"))
        if secim==1:
            calisanEkle()
        elif secim==2:
            calisanlariGoruntule()
        elif secim==3:
            ad=input("Çalışanın adını giriniz:")
            if ad in calisanlar:
                miktar=float(input("Zam miktarını girin:"))
                calisanlar[ad].zamYap(miktar)
            else:
                print("Çalışan bulunamadı")
        elif secim==4:
            break
        else:
            print("Geçersiz seçim")

if __name__ =="__main__":
    
    anaFonksiyon()

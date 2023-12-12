def main():
    n = int(input("Otoparkın Bir Kenar Uzunluğu: "))
    otopark = otopark_olustur(n)
    print(f"Otopark:\n{otopark_ciz(otopark)}")
    while True:
        try:
            cevap = int(input("Eklenecek Araç Sayısı Girin:"))
            arac_ekle(otopark, cevap)
            print(f"Otopark:\n{otopark_ciz(otopark)}")
        except ValueError:
            print("Geçerli bir değer girilmedi! İşlem iptal ediliyor..")
            break
        except:
            print("Hata! İşlem iptal ediliyor...")
            break
def otopark_olustur(n):
    otopark = [] # 2D Matris
    for i in range(n):
        satir = [] # Her bir satır buraya eklenecek
        for j in range(n):
            satir.append(0) 
        otopark.append(satir) # Satırların alt alta eklenerek 2D olması
    return otopark

def otopark_ciz(otopark):
    image = ""
    for line in otopark:
        image += str(line) + "\n"
    return image

def yer_bul(otopark):
    uzaklık = -1 # -1 Yapılma sebebi, matrisin ilk elemanının i + j toplamının 0 olması
    cords = None # None olarak yaratıldı, eğer bu değer değiştirilmezse boş yer kalmadığı anlamına geliyor
    for i in range(len(otopark)):
        for j in range(len(otopark)):
            if(otopark[i][j] == 1): # Eğer o kordinat doluysa
                continue
            if ((i + j) > uzaklık): # Eğer o ana kadar bulunandan daha uzak bir kordinat bulunduysa
                uzaklık = i + j # Max uzaklık, tekrar kıyaslama için saklanır
                cords = (i, j) # Max uzaklığa ait kordinatlar saklanır
    return cords

def arac_ekle(otopark, n):
    if n == 0: # Eklenecek araç kalmamış
        return 
    cords = yer_bul(otopark)
    if cords == None: # Yer kalmamış
        print("Yer kalmadı!")
        return
    x, y = cords
    otopark[x][y] = 1 # O noktanın doldurulması
    arac_ekle(otopark, n - 1) # Recursion ile diğer araçların eklenmesi

main() # Main fonksiyonun çağrılması
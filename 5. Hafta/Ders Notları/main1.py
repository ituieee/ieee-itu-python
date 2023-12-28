import okul_islemleri # Kütüphaneyi ekliyoruz

print(okul_islemleri.siniflar) # değişkene erişmek
okul_islemleri.okul_yazdir("İstanbul Teknik Üniversitesi") # Fonksiyona erişmek
ogrenci1 = okul_islemleri.Ogrenci("Umur", 3) # Sınıfa erişmek
ogrenci1.info() # Bu objenin bir methodunu çağırmak
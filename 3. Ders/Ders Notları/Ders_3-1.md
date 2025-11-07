# Ders 3-1: Fonksiyonlar ve Modüller
## Fonksiyonlar

Fonksiyonlar, belirli bir görevi yerine getiren kod bloklarıdır. Fonksiyonlar, kodunuzu daha düzenli ve tekrar kullanılabilir hale getirir. Python'da fonksiyonlar `def` anahtar kelimesi ile tanımlanır. Fonksiyonlar parametreler alabilir ve değer döndürebilir.

```python
def selamla(isim):
    print("Merhaba, " + isim + "!")
selamla("Ali")  # Çıktı: Merhaba, Ali!
```

Fonksiyonlar, varsayılan parametreler de alabilir:

```python
def selamla(isim="Dünya"):
    print("Merhaba, " + isim + "!")
selamla()        # Çıktı: Merhaba, Dünya!
selamla("Ayşe")  # Çıktı: Merhaba, Ayşe!
```
Fonksiyonlar ayrıca birden fazla değer döndürebilir:

```python
def hesapla(a, b):
    toplam = a + b
    fark = a - b
    return toplam, fark
```
Burada kullanılan `return` ifadesi, fonksiyonun çağrıldığı yere değer döndürmesini sağlar. Hesapla fonksiyonu iki değeri birden döndürüyor ve bu değerler bir demet (tuple) olarak geri geliyor.

```python
sonuc = hesapla(10, 5)
print(sonuc)  # Çıktı: (15, 5)
```
Bunun için bir örnek daha:

```python
def carp(x, y):
    return x * y

sonuc = carp(4, 5)

print(sonuc)  # Çıktı: 20
print(carp(sonuc, 2))  # Çıktı: 40
```

## Modüller
Modüller, Python kodunu organize etmek için kullanılan dosyalardır. Bir modül, fonksiyonlar, sınıflar ve değişkenler içerebilir. Modüller, kodunuzu daha yönetilebilir hale getirir ve tekrar kullanılabilirliği artırır. Modüller, `import` ifadesi ile programa dahil edilir.

### Built-in Modüller
Python, birçok yerleşik (built-in) modül ile birlikte gelir. Örneğin, `math` modülü matematiksel işlemler için kullanılır:

```python
import math
print(math.sqrt(16))  # Çıktı: 4.0
print(math.pi)        # Çıktı: 3.141592653589793
```
Başka builtin modüller de vardır, örneğin `random`, `datetime`, `os` gibi. Bunların kullanımına da örnek verecek olursak:

```python
import random
print(random.randint(1, 10))  # 1 ile 10 arasında rastgele bir sayı üretir
import datetime
print(datetime.datetime.now())  # Şu anki tarih ve saati gösterir
import os
print(os.getcwd())  # Geçerli çalışma dizinini gösterir
```

Bu modülleri kullanacaksanız daha detaylı öğrenmek için Python dokümantasyonına bakabilirsiniz. 

### Pip ve Üçüncü Parti Modüller
Python'da üçüncü parti modülleri yüklemek için `pip` adlı paket yöneticisi kullanılır. Örneğin, `requests` modülünü yüklemek için terminalde şu komutu kullanabilirsiniz:

```
pip install requests
```

Yükledikten sonra, modülü programınıza dahil edebilirsiniz:

```python
import requests
response = requests.get('https://api.github.com')
print(response.status_code)  # Çıktı: 200 (başarılı istek)
```

Paketleri yükledikten sonra, modüllerin nasıl kullanılacağına dair dokümantasyonlarına bakmanız faydalı olacaktır. Python paket dizinleri sayesinde birçok modül bulabilirsiniz: https://pypi.org/

Paketleri yükledikten sonra kullanmaya başlamadan önce, modülün dökümantasyonunu incelemek her zaman iyi bir pratiktir. Hangi fonksiyonların ve sınıfların mevcut olduğunu, nasıl kullanılacağını öğrenmek için dökümantasyon önemlidir. Dökümantasyon genellikle modülün resmi web sitesinde veya PyPI sayfasında bulunabilir.

### Python Paket Yöneticileri ve Sanal Ortamlar

Python'da paket yönetimi için `pip` dışında başka araçlar da bulunmaktadır. Örneğin, `conda` özellikle veri bilimi ve makine öğrenimi projelerinde popülerdir. Güncel olarak `conda`, `venv` ve `uv` gibi araçlar da kullanılmaktadır. Bu araçlar, paketlerin ve bağımlılıkların yönetimini kolaylaştırır.

Farklı projeler genelde farklı bağımlılıklar gerektirir. Bu nedenle her proje için izole bir ortam oluşturmak iyi bir uygulamadır. Sanal ortamları oluşturmak için `venv`, `conda` veya `uv` gibi araçlar kullanılabilir. 

Bunlar arasında kişisel olarak önerdiğim `uv` aracı, modern ve kullanımı kolay bir paket yöneticisidir. `uv` ile sanal ortam oluşturmak ve paketleri yönetmek oldukça basittir. Bunun dışında conda da oldukça güçlüdür ve özellikle veri bilimi projelerinde yaygın olarak kullanılır.

Doğru paket yöneticisini ve sanal ortam aracını seçmek, projenizin ihtiyaçlarına ve kişisel tercihinize bağlıdır. Her iki araç da bağımlılık yönetimini kolaylaştırır ve projelerinizin daha düzenli olmasını sağlar. Bunların araştırmasını ve hangisinin sizin için en uygun olduğunu belirleme kısmını size bırakıyorum. Bu ders özelinde paket yöneticisi kullanacak kadar karmaşık projelere girmeyeceğiz. Kendi kullanımınız için araştırmanızı yapabilirsiniz.






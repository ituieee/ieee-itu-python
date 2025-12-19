# Ders 4-2: Operator Overriding (Operatör Aşırı Yükleme)

## Operator Overriding Nedir?

Operator overriding, Python'da tanımlanan sınıflarda `+`, `-`, `*`, `==`, `<` gibi operatörlerin davranışını özelleştirmemizi sağlayan bir özelliktir. 

Örneğin, iki custom nesnesi toplamamız gerektiğinde `+` operatörünün ne yapacağını kendimiz belirleyebiliriz.

## Temel Operatör Overriding Metodları

Python'da operatörleri overload etmek için **dunder metodlar** (double underscore methods) kullanırız.

| Operatör | Method | Açıklama |
|----------|--------|----------|
| `+` | `__add__()` | Toplama işlemi |
| `-` | `__sub__()` | Çıkarma işlemi |
| `*` | `__mul__()` | Çarpma işlemi |
| `/` | `__truediv__()` | Bölme işlemi |
| `//` | `__floordiv__()` | Taban bölme işlemi |
| `%` | `__mod__()` | Modulo işlemi |
| `==` | `__eq__()` | Eşit mi kontrol |
| `!=` | `__ne__()` | Eşit değil mi kontrol |
| `<` | `__lt__()` | Küçük mü kontrol |
| `>` | `__gt__()` | Büyük mü kontrol |
| `<=` | `__le__()` | Küçük veya eşit mi kontrol |
| `>=` | `__ge__()` | Büyük veya eşit mi kontrol |
| `[]` | `__getitem__()` | İndeks erişimi |
| `len()` | `__len__()` | Uzunluk |
| `str()` | `__str__()` | String temsili |
| `print()` | `__repr__()` | Detaylı temsili |

## Örnek 1: Basit Toplama Operatörü

Haydi bir Sayı (Number) sınıfı oluşturalım ve iki nesneyi toplayabilir yapalım:

```python
class Sayı:
    def __init__(self, değer):
        self.değer = değer
    
    def __add__(self, diğer):
        """+ operatörünü overload ediyoruz"""
        if isinstance(diğer, Sayı):
            return Sayı(self.değer + diğer.değer)
        return Sayı(self.değer + diğer)
    
    def __str__(self):
        return f"Sayı({self.değer})"

# Kullanım
s1 = Sayı(5)
s2 = Sayı(3)
s3 = s1 + s2

print(s3)  # Çıktı: Sayı(8)
```

## Örnek 2: Karşılaştırma Operatörleri

Öğrencilerin notlarını kıyaslayabileceğimiz bir sınıf yazalım:

```python
class Öğrenci:
    def __init__(self, ad, not_):
        self.ad = ad
        self.not_ = not_
    
    def __eq__(self, diğer):
        """İki öğrencinin notu eşit mi?"""
        return self.not_ == diğer.not_
    
    def __lt__(self, diğer):
        """Bu öğrencinin notu daha mı düşük?"""
        return self.not_ < diğer.not_
    
    def __gt__(self, diğer):
        """Bu öğrencinin notu daha mı yüksek?"""
        return self.not_ > diğer.not_
    
    def __str__(self):
        return f"{self.ad} ({self.not_})"

# Kullanım
ali = Öğrenci("Ali", 85)
ayşe = Öğrenci("Ayşe", 90)
bora = Öğrenci("Bora", 85)

print(ali == bora)    # True (her ikisinin notu 85)
print(ali < ayşe)     # True (Ali'nin notu daha düşük)
print(ayşe > ali)     # True (Ayşe'nin notu daha yüksek)
```

## Örnek 3: Vector Sınıfı

Daha kompleks bir örnek olarak vektörler ile çalışmayı görelim:

```python
class Vektör:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, diğer):
        """İki vektörü topla"""
        return Vektör(self.x + diğer.x, self.y + diğer.y)
    
    def __sub__(self, diğer):
        """İki vektörü çıkar"""
        return Vektör(self.x - diğer.x, self.y - diğer.y)
    
    def __mul__(self, skalar):
        """Vektörü skalarp çarp"""
        return Vektör(self.x * skalar, self.y * skalar)
    
    def __eq__(self, diğer):
        """İki vektör eşit mi?"""
        return self.x == diğer.x and self.y == diğer.y
    
    def __str__(self):
        return f"Vektör({self.x}, {self.y})"

# Kullanım
v1 = Vektör(1, 2)
v2 = Vektör(3, 4)

print(v1 + v2)    # Vektör(4, 6)
print(v2 - v1)    # Vektör(2, 2)
print(v1 * 3)     # Vektör(3, 6)
print(v1 == v2)   # False
```

## Örnek 4: __len__ ve __getitem__

Indeks erişimi ve uzunluk metodlarını kullanalım:

```python
class Çanta:
    def __init__(self):
        self.eşyalar = []
    
    def __len__(self):
        """Çantada kaç eşya var?"""
        return len(self.eşyalar)
    
    def __getitem__(self, indeks):
        """Çantadaki n. eşyaya erişim"""
        return self.eşyalar[indeks]
    
    def ekle(self, eşya):
        self.eşyalar.append(eşya)
    
    def __str__(self):
        return f"Çanta({self.eşyalar})"

# Kullanım
çanta = Çanta()
çanta.ekle("kalem")
çanta.ekle("kitap")
çanta.ekle("silgi")

print(len(çanta))      # 3
print(çanta[0])        # kalem
print(çanta[1])        # kitap
print(çanta[-1])       # silgi
```

## Neden Operator Overriding Kullanırız?

1. **Daha Okunabilir Kod**: `v1 + v2` yazmak `v1.add(v2)` yazmaktan daha anlaşılırdır.

2. **Sezgisel Kullanım**: Özel sınıflar standart operatörler gibi davranır.

3. **Pythonic Kod**: Python'un tasarım felsefesine uygun kodlar yazarız.

4. **Kütüphane Uyumluluğu**: NumPy, Pandas gibi kütüphaneler operator overriding kullanır.

## Dikkat Edilmesi Gerekenler

- Operatörler genellikle **simetrik** değildir. `a + b` ile `b + a` farklı metodlar çağırabilir.
- `__radd__()`, `__rsub__()` gibi ters operatörleri de tanımlayabilirsiniz.
- Karşılaştırma operatörleri (==, <, >, vb.) dikkatli olarak tasarlanmalıdır.

## Özet

- Operator overriding, sınıfların operatörlerle davranışını tanımlamamıza izin verir.
- Dunder metodlar (`__add__`, `__eq__` vb.) kullanarak operatörleri overload ederiz.
- Kod okunabilirliğini artırır ve Python felsefesine uygun yazılım yazarız.

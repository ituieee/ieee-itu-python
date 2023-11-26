x = float(input("1. Sayıyı Girin: ")) # aldığımız string değeri dönüştürmemiz gerekiyor
y = float(input("2. Sayıyı Girin: "))

print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"Bu sayılar birbirine tam bölünüyor mu: {(x % y) == 0}") # x % y hesabıyla x'in y ye kalanını bulduk, == 0 kısmıyla da bu değerin 0 a eşit olup olmadığı (yani kalansız olup olmadığı)


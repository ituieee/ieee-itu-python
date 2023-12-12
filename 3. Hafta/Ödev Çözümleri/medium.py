def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("0'a bölme işlemi yapılamaz!")
        return None
    else:
        return x / y

def get_user_input(): # Kullanıcıdan işlem yapılacak sayıları alan fonksiyon
    try:
        num1 = float(input("İlk Sayı: "))
        num2 = float(input("İkinci Sayı: "))
        return num1, num2
    except ValueError:
        print("Lütfen düzgün değerleri girin!")
        return None, None

def calculator(): # Ana Hesap makinesi fonksiyonu
    print("Hesap Makinesine Hoş Geldiniz:")

    while True:
        print("\nİşlem Seçin:")
        print("1. Toplama (+)")
        print("2. Çıkarma (-)")
        print("3. Çarpma (*)")
        print("4. Bölme (/)")
        print("5. Çıkış")

        choice = input("İşlem Seçiniz: ")

        if choice == '5':
            print("Çıkış Yapılıyor")
            break

        if choice not in {'1', '2', '3', '4'}:
            print("Hatalı İşlem Seçimi yaptınız.")
            continue

        num1, num2 = get_user_input()

        if num1 is None or num2 is None:
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            if result is not None:
                print(f"{num1} / {num2} = {result}")

calculator()
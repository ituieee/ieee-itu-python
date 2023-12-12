def string_combiner(*args):
    try:
        txt = ""
        for string in args: # Parametre olarak alınan her bir stringi itere eder
            word = ""
            for char in string: # String içerisindeki her bir karakteri itere eder
                if char in [".", ",", "!", "?"]:
                    continue #  Noktalama İşaretiyse Ekleme yapılmadı
                word += char                
            txt += word + " " 
        txt = txt[:-1]
        txt += "."
        return txt
    except TypeError:
        return "Hata! Doğru formatta veriler girmelisiniz!"



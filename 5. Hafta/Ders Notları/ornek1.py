# Bu örnekte, gördüğümüz yapıları kullanarak fonksiyonların çalışma sürelerini hesaplayan bir dekoratör tanımlayacagız.

import time
import math
def timer(func):
    def  wrapper(*args, **kwargs):
        initial_time = time.time()
        result = func(*args, **kwargs)
        final_time = time.time()
        print(f"{func.__name__} fonksiyonu çağırıldı. Çalışma süresi: {final_time - initial_time}")
        return result
    return wrapper

@timer
def factorial(x):
    result = math.factorial(x)
    time.sleep(1)
    return result

print(factorial(20))
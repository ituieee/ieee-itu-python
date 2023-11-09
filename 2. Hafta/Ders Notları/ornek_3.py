# Bahsettiğimiz gibi, tuple'lar üzerinde değişiklik yapamayız. Ancak veri tipini değiştirerek bunu gerçekleştirebiliriz. 
# Tuple'ı liste haline çevirerek üzerinde değişiklikler yapan bir program

array = (1, 2, 3, 4, 5, 6)

print(type(array))
array = list(array)
array.append(99)
array.remove(1)
array = tuple(array)
print(array)
print(type(array))
# Bu örnekte, for döngüsü'nün yaptığını yapan bir while döngüsü yazacağız

chars = ("a", "b", "c", "d", "e", "f")

limit = len(chars)
i = 0
while (i < limit):
    print(chars[i])
    i += 1

print("\n")
############################ Aynı İşi yapan for döngüsü:############################

chars = ("a", "b", "c", "d", "e", "f")

for char in chars:
    print(char)
import random

angka = random.randint(1, 10)
tebakan = int(input("Tebak angka dari 1 sampai 10: "))

if tebakan == angka:
    print("Kamu benar!")
else:
    print("Salah, angka yang benar:", angka)
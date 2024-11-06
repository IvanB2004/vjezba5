n=int(input("Koliko brojeva zelize unijeti za provjeru parnosti?"))

parni_brojevi=0
neparni_brojevi=0

for i in range(n):
    broj=int(input(f"unesite broj {i+1}: "))


if broj % 2==0:
    print(f"broj b{broj} je paran.")
    parni_brojevi+=1
else:
    print(f"broj {broj} je neparan.")
    neparni_brojevi+=1


print("/nUkupno parnih brojeva:", parni_brojevi)
print("Ukupno neparnih brojeva:", neparni_brojevi)
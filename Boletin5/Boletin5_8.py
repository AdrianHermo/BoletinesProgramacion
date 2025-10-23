n = int(input("Introduce o número máximo das fichas: "))

for i in range(n + 1):
    for m in range(i, n + 1):
        print("A ficha é:", i, "|", m)
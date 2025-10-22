Articulo = input("Dime el nombre del articulo ")
vendas = int(input("Dime que ventas tuvo "))
if vendas <=100:
    print("baixo")
elif vendas <500:
    print ("medio")
elif vendas <1000:
    print("alto")
elif vendas >=1000:
    print ("primera necesidad")
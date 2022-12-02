etanol = float(input('preço do etanol: '))
gasolina = float(input('preço da gasolina: '))

percentual = (etanol / gasolina) * 100

if (percentual < 70):
    print("E mais vantajoso abastecer com Etanol, pois o % {}".format(round(percentual, 2)))
else:
    print("E mais vantajoso abastecer com Gasolina, pois o % {}".format(round(percentual, 2)))
 


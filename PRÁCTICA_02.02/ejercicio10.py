print("Escribe el número de barras de pan que no son frescas")
panduro = int(input())
precioporbarra = 3.49
descuento = 0.60
coste = panduro * precioporbarra * (1 - descuento)
print("Una barra fresca vale: " + str(precioporbarra) + "€")
print("El descuento de una barra no fresca es del 60%")
print("El total a pagar es: " + str(round(coste, 2)) + "€")
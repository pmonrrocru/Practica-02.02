pesodepayaso = 112
pesodemuneca = 75
print("introduce el número de payasos")
numerodepayasos = int(input())
print("Introduce el numero de munecas")
numerodemunecas = int(input())
pesodepaquete  = pesodepayaso * numerodepayasos + pesodemuneca * numerodemunecas
print("El peso total del paquete es: " + str(pesodepaquete))
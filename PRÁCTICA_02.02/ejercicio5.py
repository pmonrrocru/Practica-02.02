print("Introduce tu peso en kilogramos")
peso = int(input())
print("Introduce tu estatura en metros")
estatura = int(input())
imc = round(float(peso)/float(estatura)**2,2)
print("Tu indice de masa corporal es " + str(imc))
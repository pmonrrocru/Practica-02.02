print("Introduce la cantidad de la inversion inicial")
inversion = float(input())
intereses = 0.04
year1 = inversion * (intereses + 1)
print("Beneficios del priemr año: " + str(round(year1, 2)))
year2 = year1 * (1 + intereses)
print("Beneficios del segundo año: " + str(round(year2, 2)))
year3 = year2 * (1 + intereses)
print("Beneficios del tercer año: " + str(round(year3, 2)))
print("Introduce tu correo electronico")
correo = str(input())
print(correo[:correo.find("@")] + "@ceu.es")

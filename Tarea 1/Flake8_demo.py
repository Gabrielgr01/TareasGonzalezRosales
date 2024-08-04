# Código de errores Flake8

b = True
if (isinstance(type(b), bool)):  # Primer error: comparar tipos
    print(1)
elif (isinstance(type(b), int)):  # Segundo error: espacio en blanco
    print(2)  # Tercer error: falta doble espacio en comentario

#################################
# tarea_1_example_solution.py
#
# Desarrolladores: 
#   Gabriel O. Gonzalez Rodríguez
#   Luis G. Rosales
#################################

def operation_selector(num1, num2, op):
    ##########################
    # Función: Retorna el resultado de la operación indicada 
    #   (+, -, *, &) entre dos numeros enteros.
    # Entradas: num1, num2, op
    # Salidas:  resultado
    ##########################

    nums_are_int = 1
    op_is_str = 1
    res_cod = 0
    res_val = None
    
    # Primera validación: num1 y num2 sean enteros
    if isinstance(num1, bool):
        nums_are_int = 0
    elif (not isinstance(num1, int)):
        nums_are_int = 0

    if isinstance(num2, bool):
        nums_are_int = 0
    elif (not isinstance(num2, int)):
        nums_are_int = 0
    
    if (not nums_are_int):
        # Si el argumento num1 o num2 no es entero, imprime el 1er mensaje de error
        #print ("-E-: Alguno de los argumentos num1 o num2 no es entero.")
        res_cod = -50
        return res_cod, res_val

    # Segunda validación: op sea string
    if (not isinstance(op, str)):
        op_is_str = 0

    if (not op_is_str):
        # Si el argumento "op" no es un string, imprime el 2do mensaje de error
        #print("-E-: El argumento 'op' no es un string.")
        res_cod = -60
        return res_cod, res_val

    # Realiza la operación
    match op:
        case "+":
            res_val = num1 + num2; 
        case "-":
            res_val = num1 - num2;
        case "*":
            res_val = num1 * num2;
        case "&":
            res_val = num1 & num2;
        case _:
            # Si el argumento "op" no es valido, imprime el 3er mensaje de error
            #print("-E-: El argumento 'op' no es válido. Use '+' '-' '*' o '&'.")
            res_cod = -70

    return res_cod, res_val


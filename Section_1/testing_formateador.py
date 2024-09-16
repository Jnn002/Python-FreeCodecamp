def arithmetic_arranger(problems, show_answers=False):
    #* PRIMERA VERIFICACION: NUMERO DE PROBLEMAS NO MAYOR A 5
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    
    for problem in problems:
        #* SEGUNDA VERIFICACION: OPERADOR DEBE SER '+' O '-'
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
        
        # Eliminar espacios en blanco de nuestros problemas
        problem = problem.replace(' ', '')
        
        # Separar los numeros y el operador
        operator = '+' if '+' in problem else '-'   # operador
        num1, num2 = problem.split(operator)        # numeros

        #print(num1.count(' '))
        #num1 = num1.strip()
        #num2 = num2.strip()
        #print(f'num1: "{num1}" num2: "{num2}"')

        #* TERCERA VERIFICACION: NUMEROS DEBEN SER DIGITOS
        if not num1.isdigit() or not num2.isdigit():    # Verificamos que los numeros sean digitos
            return 'Error: Numbers must only contain digits.'
        
        #* CUARTA VERIFICACION: NUMEROS NO MAYORES A 4 DIGITOS
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        max_len = max(len(str(num1)), len(str(num2))) + 2
        
        # Convertir los numeros a enteros
        num1 = int(num1)
        num2 = int(num2)
        
        
        first_line += f'{num1:>{max_len}}    '
        second_line += f'{operator} {num2:>{max_len-2}}    '
        third_line += '-' * max_len + '    '
        
        if show_answers == True:
            if operator == '+':
                result = num1 + num2
            else:
                result = num1 - num2
            fourth_line += f'{result:>{max_len}}    '
    
    if show_answers == True:
        return f'{first_line[:-4]}\n{second_line[:-4]}\n{third_line[:-4]}\n{fourth_line}'
    else:
        return f'{first_line[:-4]}\n{second_line[:-4]}\n{third_line[:-4]}'

# NECESIDAD DE OPERADORES
print(f'\n{arithmetic_arranger(["3801  2", "123 + 49"])}')
# IMPRESION DE OPERACIONES, NORMALES
print(f'\n{arithmetic_arranger(["3801 + 2", "12 + 49"], True)}')
# DESBORDAMIENTO DE OPERACIONES
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) }')
# DESBORDAMIENTO DE NUMEROS
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
# Mostrar resultados
print(f'\n{arithmetic_arranger(["32 -        698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
# 
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')


""" def formateo_aritmetico(problemas, mostrar_solucion = False):
    if len(problemas) > 5:
        return 'Error: Demasiados problemas.'
    
    primera_linea = ''
    segunda_linea = ''
    tercera_linea = ''
    cuarta_linea = ''
    
    for problema in problemas:
        # Eliminar espacios en blanco de nuestros problemas
        problema = problema.replace(' ', '')
        if '+' not in problema and '-' not in problema:
            return "Error: Deber incluir un operador para su  '+' o '-'." """
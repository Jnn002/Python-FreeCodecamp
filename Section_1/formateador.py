def arithmetic_arranger(problems, show_answers=False):
    #* PRIMERA VERIFICACION: NO MÁS DE 5 PROBLEMAS
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # listas para almacenar las lineas de los problemas
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []
    
    for problem in problems:
        #* SEGUNDA VERIFICACION: NECESIDAD DE UN OPERADOR
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
        
        num1, operator, num2 = problem.split()
        
        #* TERCERA VERIFICACION: DIGITOS VALIDOS
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        #* CUARTA VERIFICACION: NUMEROS DE 4 DIGITOS COMO MAXIMO
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Ajustar la longitud de los números
        max_len = max(len(num1), len(num2)) + 2
        
        # Carga de los números en las listas
        first_line.append(f'{num1:>{max_len}}')
        second_line.append(f'{operator} {num2:>{max_len-2}}')
        third_line.append('-' * max_len)
        
        # Carga de linea 4 en caso de mostrar necesitar mostrar respuetas 
        if show_answers:
            result = str(int(num1) + int(num2)) if operator == '+' else str(int(num1) - int(num2))
            fourth_line.append(f'{result:>{max_len}}')
    
    # Unir las listas en un solo string
    #* METODO JOIN PARA UNIR LISTAS
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(third_line)
    # Agregar la cuarta linea si se necesita mostrar respuestas
    if show_answers:
        arranged_problems += '\n' + '    '.join(fourth_line)
    
    # Retornar el string con los problemas
    return arranged_problems

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

# El algoritmo de Luhn es un algoritmo matemático que se utiliza para 
# validar números de tarjetas de crédito y otros números de identificación.
#* TEMAS A CONSIDERAR, SLICING DE LISTAS y STRINGS
#* Metodo de traduccion de caracteres str.maketrans

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    # Invertir el numero de tarjeta
    card_number_reversed = card_number[::-1]
    # Sumar los digitos 'IMPARES DE LA TARJETA POR POSICION' 
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Sumar los digitos 'PARES DE LA TARJETA POR POSICION'
    even_digits = card_number_reversed[1::2]
    # Multiplicar por 2 los digitos pares
    for digit in even_digits:
        number = int(digit) * 2
        # Si el numero es mayor o igual a 10, sumar los digitos
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    # Sumar los digitos pares e impares
    total = sum_of_odd_digits + sum_of_even_digits
    # Verificar si el total es divisible por 10
    return total % 10 == 0

def main():
    # Ejemplo de tarjeta de credito
    card_number = '4111-8133-4555-1141'
    # Eliminar los espacios y guiones
    card_translation = str.maketrans({'-': '', ' ': ''})
    # Traducir el numero de tarjeta
    translated_card_number = card_number.translate(card_translation)

    # Verificar si la tarjeta es valida, llamando a la funcion verify_card_number
    if verify_card_number(translated_card_number):
        print('Tarjeta valida!')
    else:
        print('Tarjeta invalida!')
        
# Llamar a la funcion main
main()

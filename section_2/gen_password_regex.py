# GENERADOR DE CONTRASEÑAS, CON RESTRICCIONES DE NÚMEROS, CARACTERES ESPECIALES, MAYÚSCULAS Y MINÚSCULAS
# USANDO EXPRESIONES REGULARES
import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            # Añade un caracter aleatorio por cada paso en el ciclo,
            # definido por la longitud de la contraseña
            password += secrets.choice(all_characters)
        # Define constraints
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            # Verifica que cada restricción sea menor o igual al número de coincidencias
            constraint <= len(re.findall(pattern, password)) 
            for constraint, pattern in constraints
        ):
            break

    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
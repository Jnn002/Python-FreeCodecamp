# Métodos especiales en python
#* Los métodos especiales son métodos que tienen un significado especial en Python 
#* y que se pueden sobrecargar para modificar el comportamiento de las clases.
#* Algunos ejemplos de métodos especiales son 
#* __init__, __str__, __repr__, __add__, __sub__, __mul__, 
#* __eq__, __ne__, __lt__, __gt__, __le__, __ge__, etc.

class R2Vector:
    def __init__(self, *, x, y):
        # Inicializa un vector en R2 con componentes x e y
        self.x = x
        self.y = y

    def norm(self):
        # Calcula la norma (magnitud) del vector
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        # Devuelve una representación en cadena del vector como una tupla
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        # Devuelve una representación formal del vector
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        # Suma dos vectores si son del mismo tipo
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        # Resta dos vectores si son del mismo tipo
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        # Multiplica el vector por un escalar o realiza el producto punto si es otro vector del mismo tipo
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other):
        # Compara si dos vectores son iguales
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        # Compara si dos vectores son diferentes
        return not self == other

    def __lt__(self, other):
        # Compara si la norma de un vector es menor que la del otro
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        # Compara si la norma de un vector es mayor que la del otro
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        # Compara si la norma de un vector es menor o igual que la del otro
        return not self > other

    def __ge__(self, other):
        # Compara si la norma de un vector es mayor o igual que la del otro
        return not self < other

#* Clase R3Vector hereda todos los métodos de la clase R2Vector
#* este es uno de los beneficios de la herencia en la programación orientada a objetos
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        # Inicializa un vector en R3 con componentes x, y y z
        super().__init__(x=x, y=y)
        self.z = z

#* Además de los métodos de la clase R2Vector, la clase R3Vector tiene un método adicional
#* que calcula el producto cruzado entre dos vectores en R3
    def cross(self, other):
        # Calcula el producto cruzado entre dos vectores en R3
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)

# Ejemplos de uso de la clase R2Vector
v1 = R2Vector(x=2, y=3)
v2 = R2Vector(x=0.5, y=1.25)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
print('---------------------------')

# Ejemplos de uso de la clase R3Vector
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')
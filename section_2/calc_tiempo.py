#
#* FUNCION QUE NOS PERMITE SUMAR TIEMPO A UNA HORA DADA
#* Y NOS DEVUELVE LA HORA RESULTANTE Y LOS DIAS QUE HAN PASADO SI ES EL CASO
#* ADEMÁS PODEMOS INGRESAR QUE DÍA ES Y QUE DIA SERÁ EN EL RESULTADO DEL 
#* AGREGAR LA CANTIDAD DE HORAS DICHA

# variables de ejemplo
inicio = '8:16 PM'
duracion = '466:02'

def add_time(start, duration, day = ''):
    # SEPARAR TIEMPO Y Meridinao
    start_time, meridiano = start.split()
    # Separar Horas y Minutos
    horas, minutos = int(start_time.split(':')[0]), int(start_time.split(':')[1])
    # Preparar duracion 
    horas_agr, minutos_agr = int(duration.split(':')[0]), int(duration.split(':')[1])
    # Preparación y manejo de dias
    day = day.capitalize()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Preparación de variable day
    if day not in days:
        new_time = 'Error: Invalid day'
    
    # Conversión a formato 24 horas, para sencillo manejo
    if meridiano == 'PM' and horas != 12: # 12 PM es especial
        horas += 12
    elif meridiano == 'AM' and horas == 12: # 12 AM es medianoche
        horas = 0
    
    # Proceso para suma, minutos
    minutos += minutos_agr
    if minutos >= 60:
        horas += minutos // 60
        minutos %= 60
        
    # Proceso para suma, horas
    horas += horas_agr
    dias_transcurridos = horas // 24
    horas = horas % 24
    
    # Convertir de nuevo al formato 12h
    if horas >= 12:
        meridiano = 'PM'
        if horas > 12:
            horas -= 12
    else:
        meridiano = 'AM'
        if horas == 0:
            horas = 12
            
    if day == '':
        # Manejo de dias cuando no se especifica
        if dias_transcurridos == 0:
            new_time = f'{horas}:{minutos:02d} {meridiano}'
        elif dias_transcurridos == 1:
            new_time = f'{horas}:{minutos:02d} {meridiano} (next day)'
        else: 
            new_time = f'{horas}:{minutos:02d} {meridiano} ({dias_transcurridos} days later)'
    else: 
        # Manejo de dias cuando se especifica
        day_index = days.index(day)
        day_index += dias_transcurridos
        day_index %= 7
        new_day = days[day_index]
        
        if dias_transcurridos == 0:
            new_time = f'{horas}:{minutos:02d} {meridiano}, {new_day}'
        elif dias_transcurridos == 1:
            new_time = f'{horas}:{minutos:02d} {meridiano}, {new_day} (next day)'
        else: 
            new_time = f'{horas}:{minutos:02d} {meridiano}, {new_day} ({dias_transcurridos} days later)'
    
    return new_time

print(f'Hora inicio: {inicio}\nHora a agregar: {duracion}')
print(add_time(inicio, duracion ))

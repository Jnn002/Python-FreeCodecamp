inicio = '11:29 PM'
duracion = '53:10'

def add_time(start, duration):
    # SEPARAR TIEMPO Y Meridiano
    start_time, meridiano = start.split()
    horas, minutos = map(int, start_time.split(':'))  # Convierte directamente a enteros
    
    # Preparar duracion
    horas_agr, minutos_agr = map(int, duration.split(':'))  # Convierte duración directamente
    
    # Convertir horas a formato 24h
    if meridiano == 'PM' and horas != 12:  # 12 PM es especial
        horas += 12
    elif meridiano == 'AM' and horas == 12:  # 12 AM es medianoche
        horas = 0
    
    # Sumar minutos y ajustar si es necesario
    minutos += minutos_agr
    if minutos >= 60:
        horas += minutos // 60
        minutos %= 60
    
    # Sumar horas y calcular días pasados
    horas += horas_agr
    dias_transcurridos = horas // 24  # Cuenta cuántos días completos
    horas = horas % 24  # Ajusta para formato de 24 horas
    
    # Convertir de nuevo al formato 12h
    if horas >= 12:
        meridiano = 'PM'
        if horas > 12:
            horas -= 12
    else:
        meridiano = 'AM'
        if horas == 0:
            horas = 12
    
    return f'{horas}:{minutos:02d} {meridiano}, {dias_transcurridos} days later' if dias_transcurridos > 0 else f'{horas}:{minutos:02d} {meridiano}'

print(add_time(inicio, duracion))
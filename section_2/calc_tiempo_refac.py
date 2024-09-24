inicio = '8:16 PM'
duracion = '466:02'

def add_time(start, duration, day = ''):

    start_time, meridian = start.split()

    hours, mins = int(start_time.split(':')[0]), int(start_time.split(':')[1])

    add_hours, add_mins = int(duration.split(':')[0]), int(duration.split(':')[1])

    day = day.capitalize()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if day not in days:
        new_time = 'Error: Invalid day'

    # tranlation to 24h format
    if meridian == 'PM' and hours != 12:
        hours += 12
    elif meridian == 'AM' and hours == 12: 
        hours = 0

    #
    mins += add_mins
    if mins >= 60:
        hours += mins // 60
        mins %= 60

    # 
    hours += add_hours
    passd_days = hours // 24
    hours = hours % 24

    if hours >= 12:
        meridian = 'PM'
        if hours > 12:
            hours -= 12
    else:
        meridian = 'AM'
        if hours == 0:
            hours = 12

    if day == '':
        # day handling when not specified
        if passd_days == 0:
            new_time = f'{hours}:{mins:02d} {meridian}'
        elif passd_days == 1:
            new_time = f'{hours}:{mins:02d} {meridian} (next day)'
        else: 
            new_time = f'{hours}:{mins:02d} {meridian} ({passd_days} days later)'
    else: 
        # day handling when specified
        day_index = days.index(day)
        day_index += passd_days
        day_index %= 7
        new_day = days[day_index]
        
        if passd_days == 0:
            new_time = f'{hours}:{mins:02d} {meridian}, {new_day}'
        elif passd_days == 1:
            new_time = f'{hours}:{mins:02d} {meridian}, {new_day} (next day)'
        else: 
            new_time = f'{hours}:{mins:02d} {meridian}, {new_day} ({passd_days} days later)'

    return new_time

print(f'Hora inicio: {inicio}\nHora a agregar: {duracion}')
print(add_time(inicio, duracion ))

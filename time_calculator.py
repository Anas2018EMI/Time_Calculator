def add_time(start: str, duration: str, day_week: str = None):
    # Extracting hours and minutes from start time and converting them to 24 time format
    elements = start.split(':')
    start_hours = int(elements[0])
    start_minutes = int(elements[1].split()[0])
    time_clock_format = elements[1].split()[1]
    if time_clock_format == 'PM' and start_hours != 12:
        start_hours += 12

    if time_clock_format == 'AM' and start_hours == 12:
        start_hours = 0

    # Extracting hours and minutes from duration
    dur_el = duration.split(':')
    duration_hours = int(dur_el[0])
    duration_minutes = int(dur_el[1])

    # Calculating the new time in 24 time format
    minutes = start_minutes+duration_minutes
    hours = start_hours+duration_hours + minutes//60
    days = hours//24

    result_minutes = minutes % 60
    result_hours = hours % 24
    if result_minutes < 10:
        result_minutes = f"0{result_minutes}"

    # converting the result time in AM/PM format
    time_clock_format = 'AM'
    if result_hours > 12:
        result_hours = result_hours % 12
        time_clock_format = 'PM'
    elif result_hours == 12:
        time_clock_format = 'PM'
    elif result_hours == 0:
        result_hours = 12

    new_time = f"{result_hours}:{result_minutes} {time_clock_format}"
    # Determining the new day of the week if needed
    if day_week != None:
        day_week = day_week.lower()
        week = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        i = week.index(day_week)
        new_day_week = week[(days+i) % 7].title()
        new_time += f", {new_day_week}"
    # Presenting the number of days
    if days == 1:
        new_time += f" (next day)"
    elif days > 1:
        new_time += f" ({days} days later)"

    # print(new_time)
    return new_time


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

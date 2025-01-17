from re import match,search, IGNORECASE


def make_time_str(hour: int, minutes: int, meridiem: str) -> str:
    """_Generate the correct 24 time format_

    Args:
        hour (int): _hour as in the 12 hr clock_
        minutes (int): _minutes as in the clock_
        meridiem (str): _Whether it's morning or afternoon_

    Returns:
        str: _24 hr time str_
    
    Example:
        >>> make_time_str(1, 43, 'AM')
            '01:43'
    """
    if hour < 10 and meridiem == 'AM':
        hour = f'0{hour}'
    elif hour >= 10 and hour < 12 and meridiem == 'AM':
        hour = str(hour)
    elif hour > 0 and hour < 12 and meridiem == 'PM':
        hour = f'{12 + hour}'
    elif hour == 12 and meridiem == 'AM':
        hour = f"00"

    if minutes:
        return f'{hour}:{minutes}'
    else:
        return f'{hour}:00'


def convert(hours: str) -> str:

    pattern = r'(?P<begin_hour>[0-9]*)(?::(?P<begin_minutes>[0-9]*))?\s(?P<begining_meridiem>AM|PM){1}\sto\s'\
              r'(?P<ending_hour>[0-9]*)(?::(?P<ending_minutes>[0-9]*))?\s(?P<ending_meridiem>AM|PM){1}'

    time_match = search(pattern=pattern, string=hours, flags=IGNORECASE)
    if time_match:
        begin_hour = int(time_match.group('begin_hour'))
        begin_minutes = int(time_match.group('begin_minutes')) if time_match.group('begin_minutes') else None
        begin_meridiem = time_match.group('begining_meridiem')
        ending_hour = int(time_match.group('ending_hour'))
        ending_minutes = int(time_match.group('ending_minutes')) if time_match.group('ending_minutes') else None
        ending_meridiem = time_match.group('ending_meridiem')
    else:
        raise ValueError
    
    if (begin_hour and (begin_hour < 1 or begin_hour > 12)) or (ending_hour and (ending_hour < 1 or begin_hour > 12)):
        raise ValueError
    if (begin_minutes and (begin_minutes < 0 or begin_minutes > 59)) or (ending_minutes and (ending_minutes < 0 or ending_minutes > 59)):
        raise ValueError
    
    return make_time_str(begin_hour, begin_minutes, begin_meridiem) +' to '+ make_time_str(ending_hour, ending_minutes, ending_meridiem)

def main()->None:
    #hours: str = 'I work from 9 PM to 4 PM'
    #print(convert(hours))
    print(convert(input("Hours: ")))

if __name__ =="__main__":
    main()
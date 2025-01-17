from re import match, IGNORECASE, search

def convert(hours: str)-> str:

    pattern = r'^(?P<begin_hour>[0-9]*)(?::(?P<begin_minutes>[0-9]*))?\s(?P<begining_meridiem>AM|PM){1}\sto\s'\
              r'(?P<ending_hour>[0-9]*)(?::(?P<ending_minutes>[0-9]*))?\s(?P<ending_meridiem>AM|PM){1}$'

    time_match = match(pattern=pattern, string=hours, flags=IGNORECASE)
    if time_match:
        begin_hour = int(time_match.group('begin_hour'))
        begin_minutes = int(time_match.group('begin_minutes'))
        begin_meridiem = time_match.group('begining_meridiem')
        endind_hour = int(time_match.group('ending_hour'))
        ending_minutes = int(time_match.group('ending_minutes'))
        ending_meridiem = time_match.group('ending_meridiem')
    
    if begin_hour and begin_hour < 0 and begin_hour > 12:
        raise ValueError
    
    if begin_minutes and begin_minutes < 0 and begin_minutes > 59:
        raise ValueError
    if ending_minutes and ending_minutes < 0 and ending_minutes > 59:
        raise ValueError


    return time_match
def main()->None:
    hours: str = '12:40 AM to 1:00 PM'
    print(convert(hours))
    #print(convert(input("Hours: ")))

if __name__ =="__main__":
    main()
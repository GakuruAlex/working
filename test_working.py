import pytest
from working import convert

#AM to PM
@pytest.mark.parametrize("hours, converted_hours",[
    ("9 AM to 5 PM", "09:00 to 17:00"),
    ("9:00 AM to 5 PM", "09:00 to 17:00"),
    ("9:40 AM to 5:30 PM", "09:40 to 17:30"),
    ("9 AM to 12:59 PM", "09:00 to 12:59"),
    ("12:00 AM to 12:00 PM", "00:00 to 12:00"),
    ("11:59 AM to 11:59 PM", "11:59 to 23:59")
])
def test_convert_start_ante_to_post_meridiem(hours, converted_hours):
    assert convert(hours) == converted_hours

#PM to AM
@pytest.mark.parametrize("hours, converted_hours", [
    ("7 PM to 4 AM", "19:00 to 04:00"),
    ("10:15 PM to 6:30 AM", "22:15 to 06:30"),
    ("11:55 PM to 8 AM", "23:55 to 08:00"),
    ("12 PM to 12 AM", "12:00 to 00:00"),
    ("7 PM to 2 AM", "19:00 to 02:00")
])
def test_convert_starting_post_to_ante_meridiem(hours, converted_hours):
    assert convert(hours) == converted_hours


def test_convert_raises_value_error_invalid_hours():
    with pytest.raises(ValueError):
        convert("7:66 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("7::00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("700 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("7:00 AMPM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("7:00 AMAM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("7:2222 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("7 AM 1 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")


#Test for failure
@pytest.mark.xfail(reason="This test is meant to fail. Show test will fail on invalid result")
def test_convert_for_failure():
    assert convert("8 AM to 6 PM") == "8:00 AM to 6:00 PM"

#Test raising ValueError for correct time str
@pytest.mark.xfail(reason="Testing that correct time doesn't raise ValueError")
def test_convert_not_raising_value_error_with_correct_time():
    with pytest.raises(ValueError):
        convert("7:59 AM to 4:59 PM")





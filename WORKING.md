# Working 9 to 5 #

Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

# Problem Statement #

Find the 24 hr str equivalent of a given time in 12 hr str format.



## Input ##

A time str in 12 hr format i.e: 

    1) 9:00 AM to 5:00 PM
    2) 9 AM to 5 PM
    3) 9:00 AM to 5 PM
    4) 9 AM to 5:00 PM

## Output ##

A time str in 24 hr format i.e: for above inputs

    1) 09:00 to 17:00
    2) 09:00 to 17:00 
    3) 09:00 to 17:00 
    4) 09:00 to 17:00 

# Tests #

## Possible cases ##

1. A formal format time str with minutes and seconds eg. 9:00 AM to 5:00 PM

2. A general format time str eg 9 AM to 5 PM 

3. A mixed format time str eg 9 AM to 5:00 PM

4. starting ante meridiem and end post meridiem e.g 7 AM to 4 PM

5. starting post meridiem and end ante meridiem e.g 5 PM to 9 AM

6. Invalid format i.e '4:78 AM to 2:60 PM'

tests =
[

    {
        input: "9:00 AM to 5:00 PM",

        output: "09:00 to 17:00"
    },

    {
        input: "9 AM to 5 PM",

        output: "09:00 AM to 17:00 PM"
    },

    {
        input: "10 AM to 8:50 PM",

        output: "10:00 to 20:50"
    },

    {
        input: "5 PM to 9 AM",

        output; "17:00 to 09:00"

    },

    {
        input: "5:30 PM to 7 AM",

        output: "17:30 to 07:00" 
    },
    {
        input: "7:00 PM to 4:00 AM",
        output: "19:00 to 04:00"
    },
    {
        input: "7:60 AM to 5:67 PM",
        output: raise ValueError
    }
]



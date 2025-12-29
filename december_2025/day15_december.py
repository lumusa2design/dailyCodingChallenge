"""Speed Check

Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

    1 mile equals 1.60934 kilometers.
    If you are travelling less than or equal to the speed limit, return "Not Speeding".
    If you are travelling 5 KPH or less over the speed limit, return "Warning".
    If you are travelling more than 5 KPH over the speed limit, return "Ticket".

"""
def speed_check(speed_mph, speed_limit_kph):
    speed_kph = speed_mph * 1.60934
    difference = speed_kph - speed_limit_kph

    if difference <= 0:
        return "Not Speeding"
    elif difference <= 5:
        return "Warning"
    else:
        return "Ticket"
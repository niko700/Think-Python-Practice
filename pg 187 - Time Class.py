#pgs 187 - 188, Chapter 16
#function that takes a Time object, and prints the time

class Time:
    """Represents the time of day,
    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(t):

    hour = t.hour
    minutes = t.minute
    seconds = t.second

    s1 = '%.2d : %.2d : %.2d' % (hour, minutes, seconds)

    s2 = '{0} : {1} : {2}'.format(hour, minutes, seconds)

    print(s1)
    print(s2)

print_time(time)
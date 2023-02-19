class Time:
    """Represents the time of day,
    attributes: hour, minute, second
    """

#print_time function from pg 187 earlier
def print_time(t):
    hour = t.hour
    minutes = t.minute
    seconds = t.second
    s = '{0} : {1} : {2}'.format(hour, minutes, seconds)
    print(s)

#function
#creates new Time object, initializes attributes, returns reference to new object
#pure function - does not modify any of the objects passed to it as an argument
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

#two Time objects
start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)

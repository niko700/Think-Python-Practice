#response to in-text practice prompt Think Python 2

#task: to create a function named is_after that takes two instances of class Time, t1 and t2,
#and returns a boolean True if t1 follows t2 chronologically

class Time:
    """Represents the time of day,
    attributes: hour, minute, second
    """
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

#function that compares two times, and returns True if t1 follows t2 chronologically (i.e. t1 is later than t2)
def is_after(t1, t2):
   if t1.hour > t2. hour:
       return True
   elif t1.hour < t2.hour:
       return False
   elif t1.hour == t2.hour:
       if t1.minute > t2.minute:
           return True
       elif t1.minute < t2. minute:
           return False
       elif t1.minute == t2.minute:
           if t1.second > t2.second:
               return True
           else:
               return False


#two instances of time to test
time1 = Time()
time1.hour = 11
time1.minute = 16
time1.second = 7

time2 = Time()
time2.hour = 11
time2.minute = 16
time2.second = 6


#run function
print(is_after(time1, time2))

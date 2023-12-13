import datetime

e = datetime.datetime.now()
print ("Current date and time: %s" % e)
print ("Today's date: %s/%s/%s" % (e.day, e.month, e.year))
print ("The time is now: %s:%s:%s" % (e.hour, e.minute, e.second))

print("------------")
current = datetime.datetime.now()
one_year = current + datetime.timedelta(days=365)
print("The date in one year:", str(one_year))
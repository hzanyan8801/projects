from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month 
current_day = now.day 

date =  ("%s/%s/%s" %(current_year, current_month, current_day))

time = ("%s:%s:%s" %(now.hour, now.minute, now.second))

print (date + " " + time)

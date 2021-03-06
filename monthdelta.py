from calendar import monthrange
from datetime import datetime, timedelta

def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
            
    return delta
    
date_from = datetime.strptime('2016-01-01', "%Y-%m-%d")
date_to = datetime.strptime('2016-01-31', "%Y-%m-%d")
print monthdelta(date_from,date_to)

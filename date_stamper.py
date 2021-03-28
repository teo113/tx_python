# author: github.com/teo113
# desc: This script prints various date and time formats to the console

from datetime import datetime

# YYYYMMDD
yyyymmdd = datetime.now().strftime('%Y%m%d')
print(yyyymmdd)

# YYYYMMDD_HHMM
date_time = datetime.today().strftime('%Y%m%d_%H%M%S')
print(date_time)

# MONYY
monyear = datetime.today().strftime('%b%y')
print(monyear.upper())

# pretty date
if datetime.today().day == 1:
    pretty_date = datetime.today().strftime('%dst %B %Y')
    print(pretty_date)
elif datetime.today().day == 2:
    pretty_date = datetime.today().strftime('%dnd %B %Y')
    print(pretty_date)
elif datetime.today().day == 3:
    pretty_date = datetime.today().strftime('%drd %B %Y')
    print(pretty_date)
elif datetime.today().day == 21:
    pretty_date = datetime.today().strftime('%dst %B %Y')
    print(pretty_date)
elif datetime.today().day == 22:
    pretty_date = datetime.today().strftime('%dnd %B %Y')
    print(pretty_date)
elif datetime.today().day == 23:
    pretty_date = datetime.today().strftime('%drd %B %Y')
    print(pretty_date)
elif datetime.today().day == 31:
    pretty_date = datetime.today().strftime('%dst %B %Y')
    print(pretty_date)
else:
    pretty_date = datetime.today().strftime('%dth %B %Y')
    print(pretty_date)

# locale
locale = datetime.today().strftime('%c')
print(locale)

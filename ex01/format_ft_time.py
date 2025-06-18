import time
import datetime

seconds = time.time()
formeted_seconds = "{:,.4f}".format(seconds)
#: starts format
#, adds commas as thousands separator
#.4f 4 decimals

formated_scientific_notation = "{:.2e}".format(seconds)
#.2e exponential with 2 decimals


print("Seconds since January 1, 1970: {} or {} in scientific notation".format(formeted_seconds, formated_scientific_notation))

today = datetime.date.today()

print(today.strftime("%b %d %Y"))
import fetchscript
import time
from datetime import datetime
import pytz

while(True):
    fetch_data = fetchscript.runFetch()
    if (fetch_data is None):
        tz_NY = pytz.timezone('America/New_York')
        datetime_NY = datetime.now(tz_NY)
        fetch_data = "last fetch (NY time):", datetime_NY.strftime("%H:%M:%S")
    log_file = open('log.txt', "w")
    log_file.write(str(fetch_data))
    log_file.close()
    time.sleep(3600)

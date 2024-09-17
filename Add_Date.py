import datetime

date_time = datetime.datetime.now().strftime('%Y%m%d')
filename = f'filename_{date_time}.csv' #filename wth whatever you wnat to put

print(f'Report saved to {filename}')

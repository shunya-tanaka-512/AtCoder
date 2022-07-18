import datetime


K = int(input())
dt = datetime.datetime(2022, 7, 2, 21)
td_Km = datetime.timedelta(minutes=K)
dt_Km = dt + td_Km
print(dt_Km.strftime("%H:%M"))

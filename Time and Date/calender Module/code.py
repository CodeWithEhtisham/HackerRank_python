import calendar

m,d,y=input().split(" ")

# print(date)

print(calendar.datetime.datetime(int(y),int(m),int(d)).strftime("%A").upper())


while True:
    ordate = input().replace(" ","")
    month,day,year = ordate.split("/")
    month,day,year = int(month),int(day),int(year)
    print(f"{year}-{month:02}-{day:02}")


while True:
    ordate = input().replace(" ","")
    month,day,year = ordate.split("/")
    print(year+"-"+month+"-"+day)
month =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        ordate = input().replace(" ","")
        month,day,year = ordate.split("/")
        month,day,year = int(month),int(day),int(year)
        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        for m in month:
            if ordate.startswith(m):
                
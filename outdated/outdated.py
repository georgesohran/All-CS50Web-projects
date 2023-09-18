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
    ordate = input().replace(" ","")
    try:
        month1,day,year = ordate.split("/")
        month1,day,year = int(month1),int(day),int(year)
        break
    except ValueError:
        for m in month:
            if ordate.startswith(m):
                month_name_check = m
                month1 = month.index(m)+1
                ordate = ordate.replace(m,'')
                day,year = ordate.split(",")
                day,year = int(day),int(year)
                break

    if (month_name_check in month) and (0<month1<=12) and (0<day<=31):
        break
    else:
        continew


print(f"{year}-{month1:02}-{day:02}")
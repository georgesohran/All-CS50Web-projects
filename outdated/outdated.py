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

def format_check1(s):
    sasa = s.replace("/","")
    if sasa.isdigit() and s.find("/") != -1:
        return True

def format_check2(s):
    for m in month:
        if s.startswith(m) and s.find("/") == -1:
            return True
    return False

while True:
    ordate = input("Date: ").replace(" ","")
    if format_check1(ordate) or format_check2(ordate) :
        try:
            month1,day,year = ordate.split("/")
            month1,day,year = int(month1),int(day),int(year)
        except ValueError:
            for m in month:
               if ordate.startswith(m):
                    month1 = month.index(m)+1
                    ordate = ordate.replace(m,'')
                    day,year = ordate.split(",")
                    day,year  = int(day),int(year)
                    break
        except EOFError:
            break

        if (0<month1<=12) and (0<day<=31):
            print(f"{year}-{month1:02}-{day:02}")
            break
        else:
            pass
    else:
        pass




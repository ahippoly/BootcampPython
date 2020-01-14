import datetime

t = (3,30,2019,9,25)

def format_num(data) :
    if data < 10 :
        return ('0' + str(data))
    return (str(data))

t = list(map(format_num, t))

hour = t[0]
minutes = t[1]
year = t[2]
month = t[3]
day = t[4]

print("%s/%s/%s %s:%s" % (month, day, year, hour, minutes))


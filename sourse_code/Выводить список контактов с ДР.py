from datetime import datetime, timedelta

def get_user_birthday(days_forward):
    year = 93
    month = 8 #(datetime.strptime((i['birthday']), '%d-%m-%y').month)
    day = 30 #((datetime.strptime((i['birthday']), '%d-%m-%y').day)

    bd = datetime(year,month,day)
    now = datetime.now()
    bd = datetime(now.year, bd.month, bd.day)

    present = bd
    future = datetime.now() + timedelta(days = days_forward)
    if present < future:
        print("birthday")
    else:
        print("skip")

get_user_birthday(3)
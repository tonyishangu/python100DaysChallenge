# import smtplib

email =''
password=''

# with smtplib.SMTP('stmp.gmail.com') as connection:
#     connection.starttls()        #secures the connection
#     connection.login(email, password)  ##enter your email and password here
#     connection.sendmail(from_addr=email, to_addrs='tonyishangu@gmail.com', msg='subject:hello\n\n my guy')
    

import datetime as dt

now = dt.datetime.now()
year =now.year
month = now.month
day = now.day
day_of_th_Week = now.weekday()
print(year, month, day, day_of_th_Week)

birthday = dt.datetime(year=1997, month=5, day=1)
print(birthday)
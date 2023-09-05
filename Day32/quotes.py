import smtplib
import datetime as dt
import random

email = 'tonysaiglo@gmail.com'
password = 'qwrty456'
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open('quotes.txt') as quote:
        all_quotes = quote.readlines()
        r_quote = random.choice(all_quotes)

    print(r_quote)
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(email, password)
        conn.sendmail(
            from_addr=email,
            to_addrs=email, 
            msg=f'Subject:Monday Motivation\n\n{r_quote}'
        )
import datetime as dt
import pandas
import random
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv('birthday.csv')
email = 'tonysaigelo@gmail.com'
password = 'Cana1es!!'


birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    person = birthday_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1,3)}'
    with open (file_path) as letter:
        content = letter.read()
        content = content.replace('[NAME]',person['name'])
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(email, password)
        conn.sendmail(
            from_addr=email, 
            to_addrs=person['email'], 
            msg=f'Subject:Happy Birthday\n\n{content}')

print(today)
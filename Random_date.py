import datetime
import random
d1=input("Enter the starting date in dd-mm-yy format: ").split("-")
d2=input("Enter the starting date in dd-mm-yy format: ").split("-")

for i in range(len(d1)):
    d1[i]=int(d1[i])

for i in range(len(d1)):
    d2[i]=int(d2[i])


start_date = datetime.date(d1[2], d1[1], d1[0])
end_date = datetime.date(d2[2], d2[1], d2[0])

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)
random_date=str(random_date)
s=random_date.split("-")
s=s[::-1]
d=str()
for i in s:
    d=d+str(i)+"-"
d=d.rstrip("-")
print("The random date is: \n")
print(d)

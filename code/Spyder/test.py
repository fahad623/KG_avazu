from datetime import date

a = '14102100'
new_date= date(int("20"+a[0:2]),int(a[2:4]),int(a[4:6]))
day = new_date.strftime("%A")
dict_week ={'Sunday':1, 'Monday':2, 'Tuesday':3, 'Wednesday':4, 'Thursday':5, 'Friday':6, 'Saturday':7}

print dict_week[day]

hour= a[6:8]
print day
from datetime import *
td=date.today()
print("today's date is :")
print(td)
class mydate():
    def adddays(self,td):
        d=int(input("enter the number of days to be added"))
        print(td+timedelta(days=d))

    def add_months(self,td):
        m=int(input("enter the number of months to be added"))
        m1=m*30
        print(td + timedelta(days=m1))

    def add_years(self, td):
        y = int(input("enter the number of years to be added"))
        y1=y*365
        print(td + timedelta(days=y1))

    def week_days(self,td):5
        s=td.strftime("%A")
        print("Today is ",s)

    def diff_date(self,td):
        d2,m2,y2=[int(x) for x in input("enter a date:").split('/')]
        d=date(y2,m2,d2)
        dt=d-td
        print(dt)

    def future_date(self,td):
        d = int(input("enter the number of days to be added"))
        m = int(input("enter the number of months to be added"))
        y = int(input("enter the number of years to be added"))
        m1 = m * 30
        y1 = y * 365
        sum=d+m1+y1
        print(td + timedelta(days=sum))

    def pass_date(self, td):
        d = int(input("enter the number of days to be subtract"))
        m = int(input("enter the number of months to be subtract"))
        y = int(input("enter the number of years to be subtract"))
        m1 = m * 30
        y1 = y * 365
        sum = d + m1 + y1
        print(td - timedelta(days=sum))


s=mydate()
s.adddays(td)
s.add_months(td)
s.add_years(td)
s.week_days(td)
s.diff_date(td)
s.future_date(td)
s.pass_date(td)

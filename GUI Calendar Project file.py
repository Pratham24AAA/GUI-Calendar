from tkinter import *

import calendar

root = Tk()
root.title("Calendar Operation")
root.geometry("650x750")
root.resizable(0,0)

def show():
    t = str(spin0.get())
    d = int(spin1.get())
    a = int(spin2.get())
    b = int(spin3.get())
    c = int(spin4.get()) 
    e = int(spin5.get())
    if t == "Print a month                                      [Month,Year]":
        cal = calendar.month(c,b)
        txt.delete(0.0, END)
        txt.insert(INSERT, cal)
    elif t == "Print whole calendar                               [Year]":
        cal = calendar.calendar(c,2,1,6)
        txt.delete(0.0, END)
        txt.insert(INSERT, cal)
    elif t == "Check leap year                                    [Year] ":
        if (calendar.isleap(c)):
           cal = "The year is leap" 
        else : 
           cal = "The year is not leap"
        txt.delete(0.0, END)
        txt.insert(INSERT, cal)
    elif t == "Find number of leap years in some interval of years               [Year,Year2]":
        cal = calendar.leapdays(c, e)
        txt.delete(0.0, END)
        txt.insert(INSERT, cal)
    elif t == "Print the range of month                          [Month,Year]":
        cal = calendar.monthrange(b, a)
        ca = "Starting weekday no. and no. of days of the month is"
        txt.delete(0.0, END)
        txt.insert(INSERT,(ca,cal))
    elif t == "Print the weekday of a date                         [Date,Month,Year]":
        cal = calendar.weekday(c,b,a)
        if cal==0: 
           ca = "Monday"
        elif cal==1:
           ca = "Tuesday"
        elif cal==2:
           ca = "Wednesday"
        elif cal==3:
           ca = "Thursday"
        elif cal==4:
           ca = "Friday"
        elif cal==5:
           ca = "Saturday"
        else :
           ca = "Sunday"
        txt.delete(0.0, END)
        txt.insert(INSERT, ca)
    elif t == "Print the starting date of weekday in each month             [Weekday,Year]":
        txt.delete(0.0, END)
        if d==0:
            for month in range(1, 13):
                mycal = calendar.monthcalendar(c, month)
                week1 = mycal[0]
                week2 = mycal[1]
                if week1[calendar.MONDAY] != 0:
                   day = week1[calendar.MONDAY]
                else:
                   day = week2[calendar.MONDAY]
                w = (calendar.month_name[month],day)
                txt.insert(INSERT, w)
                txt.insert(INSERT,'\n')
        elif d==1:
            for month in range(1, 13):
                mycal = calendar.monthcalendar(c, month)
                week1 = mycal[0]
                week2 = mycal[1]
                if week1[calendar.TUESDAY] != 0:
                  day = week1[calendar.TUESDAY]
                else:
                  day = week2[calendar.TUESDAY]
                w = (calendar.month_name[month],day)
                txt.insert(INSERT, w)
                txt.insert(INSERT,'\n')
        elif d==2:
            for month in range(1, 13):
                mycal = calendar.monthcalendar(c, month)
                week1 = mycal[0]
                week2 = mycal[1]
                if week1[calendar.WEDNESDAY] != 0:
                    day = week1[calendar.WEDNESDAY]
                else:
                    day = week2[calendar.WEDNESDAY]
                w = (calendar.month_name[month],day)
                txt.insert(INSERT, w)
                txt.insert(INSERT,'\n')
        elif d==3:
            for month in range(1, 13):
                mycal = calendar.monthcalendar(c, month)
                week1 = mycal[0]
                week2 = mycal[1]
                if week1[calendar.THURSDAY] != 0:
                    day = week1[calendar.THURSDAY]
                else:
                    day = week2[calendar.THURSDAY]
                w = (calendar.month_name[month],day)
                txt.insert(INSERT, w)
                txt.insert(INSERT,'\n')
        elif d==4:
            for month in range(1, 13):
                mycal = calendar.monthcalendar(c, month)
                week1 = mycal[0]
                week2 = mycal[1]
                if week1[calendar.FRIDAY] != 0:
                    day = week1[calendar.FRIDAY]
                else:
                    day = week2[calendar.FRIDAY]
                w = (calendar.month_name[month],day)
                txt.insert(INSERT, w)
                txt.insert(INSERT,'\n')
        elif d==5:
            for month in range(1, 13):
                mycal = calendar.monthcalendar(c, month)
                week1 = mycal[0]
                week2 = mycal[1]
                if week1[calendar.SATURDAY] != 0:
                    day = week1[calendar.SATURDAY]
                else:
                    day = week2[calendar.SATURDAY]
                w = (calendar.month_name[month],day)
                txt.insert(INSERT, w)
                txt.insert(INSERT,'\n')
        elif d==6:
            for month in range(1, 13):
                mycal = calendar.monthcalendar(c, month)
                week1 = mycal[0]
                week2 = mycal[1]
                if week1[calendar.SUNDAY] != 0:
                    day = week1[calendar.SUNDAY]
                else:
                    day = week2[calendar.SUNDAY]
                w = (calendar.month_name[month],day)
                txt.insert(INSERT, w)
                txt.insert(INSERT,'\n')


lbl1 = Label(root,text="Task",font=('arial',9,'bold')).place(x=15,y=0)
lbl2 = Label(root,text="Weekday",font=('arial',9,'bold')).place(x=15,y=30)
lbl3 = Label(root,text="Date",font=('arial',9,'bold')).place(x=130,y=30)
lbl4 = Label(root,text="Month",font=('arial',9,'bold')).place(x=215,y=30)
lbl5 = Label(root,text="Year",font=('arial',9,'bold')).place(x=315,y=30)
lbl6 = Label(root,text="Year2",font=('arial',9,'bold')).place(x=415,y=30)

spin0 = Spinbox(root,values=("Print a month                                      [Month,Year]",
"Print whole calendar                               [Year]",
"Check leap year                                    [Year] ",
"Find number of leap years in some interval of years               [Year,Year2]",
"Print the range of month                          [Month,Year]",
"Print the weekday of a date                         [Date,Month,Year]",
"Print the starting date of weekday in each month             [Weekday,Year]") ,width=65)
spin0.place(x=68,y=0)

spin1 = Spinbox(root,from_= 0,to_= 6,width=4)
spin1.place(x=75,y=30)

spin2 = Spinbox(root,from_= 1,to_= 31,width=4)
spin2.place(x=160,y=30)

spin3 = Spinbox(root,from_= 1,to_= 12,width=4)
spin3.place(x=260,y=30)

spin4 = Spinbox(root,from_= 1999,to_= 2100,width=4)
spin4.place(x=350,y=30)

spin5 = Spinbox(root,from_= 1999,to_= 2100,width=4)
spin5.place(x=455,y=30)

btn = Button(root,text="Show",font=('arial',9,'bold'),command=show).place(x=250,y=60)

txt = Text(root,width=75,height=37)
txt.place(x=24,y=100)

root.mainloop()
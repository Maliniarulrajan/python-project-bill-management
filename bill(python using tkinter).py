from tkinter import *
root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

Total_bill = StringVar()

def Reset():
    en_dosa.delete(0,END)
    en_idly.delete(0,END)
    en_poori.delete(0,END)
    en_meals.delete(0,END)
    en_cofee_tea.delete(0,END)
    en_chappathi.delete(0,END)
    en_juice.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except: a1=0
    try:a2=int(idly.get())
    except: a2=0
    try:a3=int(poori.get())
    except: a3=0
    try:a4=int(meals.get())
    except: a4=0
    try:a5=int(cofee_tea.get())
    except: a5=0
    try:a6=int(chappathi.get())
    except: a6=0
    try:a7=int(juice.get())
    except: a7=0
    
    #define cost of each item per quantity
    c1=70*a1
    c2=40*a2
    c3=50*a3
    c4=90*a4
    c5=20*a5
    c6=50*a6
    c7=25*a7

    lb_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lb_total.place(x=0,y=50)

    en_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightblue")
    en_total.place(x=20,y=100)
    
    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)


Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calbori",33),width="300",height="2").pack()

#menu card
f=Frame(root,bg="lightblue",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightblue").place(x=80,y=0)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa....Rs.70/plate",fg="black",bg="lightblue").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Idly....Rs.40/plate",fg="black",bg="lightblue").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Poori....Rs.50/plate",fg="black",bg="lightblue").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Meals....Rs.90/plate",fg="black",bg="lightblue").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Coffee/Tea....Rs.20/cup",fg="black",bg="lightblue").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="chappathi....Rs.50/plate",fg="black",bg="lightblue").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="juice....Rs.25/Glass",fg="black",bg="lightblue").place(x=10,y=260)

#Bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("Calbri",20),bg="lightyellow")
Bill.place(x=120,y=10)

#entry work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()
dosa=StringVar()
idly=StringVar()
poori=StringVar()
meals=StringVar()
cofee_tea=StringVar()
chappathi=StringVar()
juice=StringVar()
total_bill=StringVar()

#label
lb_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
lb_idly=Label(f1,font=("aria",20,'bold'),text="Idly",width=12,fg="blue4")
lb_poori=Label(f1,font=("aria",20,'bold'),text="Poori",width=12,fg="blue4")
lb_meals=Label(f1,font=("aria",20,'bold'),text="Meals",width=12,fg="blue4")
lb_cofee_tea=Label(f1,font=("aria",20,'bold'),text="Coffee/Tea",width=12,fg="blue4")
lb_chappathi=Label(f1,font=("aria",20,'bold'),text="Chappathi",width=12,fg="blue4")
lb_juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=12,fg="blue4")

lb_dosa.grid(row=1,column=0)
lb_idly.grid(row=2,column=0)
lb_poori.grid(row=3,column=0)
lb_meals.grid(row=4,column=0)
lb_cofee_tea.grid(row=5,column=0)
lb_chappathi.grid(row=6,column=0)
lb_juice.grid(row=7,column=0)

#Entry
en_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=dosa,bd=6,width=8,bg="lightpink")
en_idly=Entry(f1,font=("aria",20,'bold'),textvariable=idly,bd=6,width=8,bg="lightpink")
en_poori=Entry(f1,font=("aria",20,'bold'),textvariable=poori,bd=6,width=8,bg="lightpink")
en_meals=Entry(f1,font=("aria",20,'bold'),textvariable=meals,bd=6,width=8,bg="lightpink")
en_cofee_tea=Entry(f1,font=("aria",20,'bold'),textvariable=cofee_tea,bd=6,width=8,bg="lightpink")
en_chappathi=Entry(f1,font=("aria",20,'bold'),textvariable=chappathi,bd=6,width=8,bg="lightpink")
en_juice=Entry(f1,font=("aria",20,'bold'),textvariable=juice,bd=6,width=8,bg="lightpink")

en_dosa.grid(row=1,column=1)
en_idly.grid(row=2,column=1)
en_poori.grid(row=3,column=1)
en_meals.grid(row=4,column=1)
en_cofee_tea.grid(row=5,column=1)
en_chappathi.grid(row=6,column=1)
en_juice.grid(row=7,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("araial",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)
btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("araial",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)



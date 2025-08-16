from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import mysql.connector as sql
from tkcalendar import Calendar
from tabulate import tabulate
from random import randrange
from datetime import date


con = sql.connect(host='localhost', user="root", password='Gundamma@123', database='bus_reservation')
cur = con.cursor()
g = ''


def login():
    vid()
    global userid
    global Login_page
    global img
    global g
    global img1
    global img2
    Login_page = Tk(className=" Login Page")
    Login_page.geometry("500x600")
    Login_page.resizable('False','False')
    #
    g+='1'
    # image = Image.open("assets\\bus_login.png")
    # bg = ImageTk.PhotoImage(image)
    # background_label = Label(Login_page, image=bg)
    # background_label.pack()

    img = PhotoImage(file="assets\\bus_login.png")
    bg = Label(Login_page, image=img)
    bg.place(anchor="center", x=250, y=300)

    Label(Login_page, text='User id:', font=("courier", 18), bg='#b1ceeb').place(y=200)
    # Label(Login_page, text='          ', font=("courier", 20), bg='#b1ceeb').place(y=260)
    Label(Login_page, text='password:', font=("courier", 18), bg='#b1ceeb').place(y=280)

    Label(Login_page, text='Login Page', font=("Arial", 25), bg='#9abae0').place(y=10, x=180)
    # login_text.pack()

    id = Entry(Login_page, borderwidth=3)
    paswd = Entry(Login_page, show="*", borderwidth=3)
    id.place(x=200, y=210)
    paswd.place(x=200, y=285)

    def get_input():
        global userid, passwd
        userid = id.get()
        passwd = paswd.get()

        if userid != '' and passwd != '':
            cur.execute("Select * from passenger;")
            rec = cur.fetchall()
            a = 0
            l = []
            for i in rec:
                l.append((i[0], i[1]))
            t = (userid, passwd)
            if t in l:
                cur.execute("select type from passenger where passengerid = (%s)", (userid,))
                urr = cur.fetchall()
                # print(urr)
                typee = urr[0][0]
                if typee == 'user':
                    login_destroyer()
                else:
                    admin_login_destroyer()
            else:
                messagebox.showerror("Incorrect Credentials", "Wrong Password or User Id")
        else:
            messagebox.showwarning("All fields are required",
                                   "All fields are required so fill all fields to login")

    button = Button(Login_page, text="login", command=get_input, height=1, width=20, bg='#b1ceeb')
    
    button.place(x=280, y=500)

    button = Button(Login_page, text="Sign Up", command=signup, height=1, width=20, bg='#b1ceeb')
    button.place(x=80, y=500)

    Login_page.mainloop()


def signup():
    global Login_page
    Login_page.destroy()
    signup_wind()


def dest_signp():
    add_sql_login()


def signup_wind():
    global address
    global name
    global usr_id
    global paswd
    global ph_no
    global conf_paswd
    global signpage
    signpage = Tk(className=" Sign Up page")
    signpage.geometry('500x700')
    signpage.configure(bg='#b1ceeb')
    signpage.resizable('False','False')


    signup_tst = Label(signpage, text="Sign Up", font=('courier', 30), bg='#b1ceeb')
    signup_tst.pack()

    Label(signpage, text='Name:', font=("courier", 18), bg='#b1ceeb').place(y=100)
    Label(signpage, text='Address:', font=("courier", 18), bg='#b1ceeb').place(y=180)
    Label(signpage, text="Phone Number:", font=("courier", 18), bg='#b1ceeb').place(y=260)
    Label(signpage, text='User Id:', font=("courier", 18), bg='#b1ceeb').place(y=340)
    Label(signpage, text='Password:', font=("courier", 18), bg='#b1ceeb').place(y=420)
    Label(signpage, text='Confirm Password:', font=("courier", 18), bg='#b1ceeb').place(y=520)

    name = Entry(signpage, borderwidth=3)
    address = Entry(signpage, borderwidth=3)
    ph_no = Entry(signpage, borderwidth=3)
    usr_id = Entry(signpage, borderwidth=3)
    paswd = Entry(signpage, show="*", borderwidth=3)
    conf_paswd = Entry(signpage, show="*", borderwidth=3)

    ph_no.place(x=200, y=265)
    address.place(x=200, y=185)
    name.place(x=200, y=105)
    usr_id.place(x=200, y=345)
    paswd.place(x=200, y=425)
    conf_paswd.place(x=250, y=525)
    button = Button(signpage, text="Sign Up", command=dest_signp, height=2, width=40, bg='#00A86b')
    button.place(x=110, y=600)

    signpage.mainloop()


p = ''


def add_sql_login():
    global address
    global name
    global usr_id
    global paswd
    global ph_no
    global conf_paswd
    global signpage
    global p
    global n
    global usr
    global addr
    global phno
    # print(address, name, usr_id, paswd, ph_no, conf_paswd, '\n', sep="$")
    usr = usr_id.get()
    p = paswd.get()
    n = name.get()
    addr = address.get()
    phno = ph_no.get()
    con_pas = conf_paswd.get()

    # print(addr, n, usr, p, phno, con_pas, sep="#")
    # cur.execute("INSERT INTO login (passengerid, password, n, phone_no, addr) VALUES (%s, %s, %s, %s, %s)", (usr, p, n, phno,addr))
    # con.commit()
    # password_checker()
    cur.execute("Select passengerid from passenger")
    usr_lst = cur.fetchall()
    if len(usr) > 0 and len(p) > 0 and len(addr) > 0 and len(phno) > 0 and len(n) > 0:
        if (usr,) not in usr_lst:
            if "@" in usr and len(usr.split('@')[0]) > 0 and len(usr.split('@')[1]) > 0:
                if len(phno)==10 and phno.isnumeric():
                    if password_checker(p):
                        if con_pas == p:
                            # print(usr, p)
                            signpage.destroy()
                            bank_commit()

                        else:
                            messagebox.showwarning("Password doesnt match", "New Password and Confirm Password doesnt march")

                            # signup_wind()
                    else:
                        messagebox.showwarning("Password Error",
                                               "Choose strong password with least 6 characters, 1 upper case,lowercase and digit")
                else:
                    messagebox.showerror("Phone no Error", "Phone number should be an integer of 10 charecters")
            else:
                messagebox.showerror("User ID error", "User id should have '@' and somethin before and after it...")

        else:
            messagebox.showerror("User id taken", "User ID is already taken... Choose another one")
                # signup_wind()
    else:
        messagebox.showwarning("All fields are required",
                               "All fields are required so fill all fields to continue to signup")
        # signup_wind()


def check_date(date):
    # print(date)
    # print(type(date))
    date=str(date)
    from datetime import datetime
    date_format = "%Y-%m-%d"
    end = datetime.strptime(date, date_format)
    now1 = datetime.now()
    # print(str(now1)[:10], date)
    now = datetime.strptime(str(now1)[:10], date_format)

    if end < now:
        # print("past")
        return False
    elif end > now:
        # print("future")
        return True
        # event in future
    else:
        # print("now")
        return True
    # print("Terminated")


def bank_commit():
    global bnk_usr
    global usr
    global bnk_pswd
    global bank_wind
    messagebox.showinfo("Connect to bank", "Connect your account to your bank account to proceed")
    bank_wind = Tk(className=" Bank page")
    bank_wind.geometry("600x600")
    bank_wind.configure(bg='#b1ceeb')
    # bank_wind.resizable('False','False')

    Label(bank_wind, text="Enter your bank username: ", font=("courier",18), bg='#b1ceeb').place(x=20, y=100)
    Label(bank_wind, text="Enter your bank password: ", font=("courier",18), bg='#b1ceeb').place(x=20, y=180)

    bnk_usr = Entry(bank_wind, borderwidth=3)
    bnk_pswd = Entry(bank_wind, borderwidth=3)

    bnk_usr.place(x=400, y=100)
    bnk_pswd.place(x=400, y=180)
    Button(bank_wind, text="Record bank details", command=get_bnk_inp, bg='#b1ceeb', font=("courier",18), background='#b1ceeb').place(anchor='center', x=250, y=500)


def get_bnk_inp():
    global bnk_usr
    global bnk_pswd
    global bank_wind
    global p
    global n
    global usr
    global addr
    global phno
    # print(bnk_usr,bnk_pswd)
    bnk_user = bnk_usr.get()
    bnk_psswd = bnk_pswd.get()
    cur.execute("Select user_id from bank_balence")
    if (bnk_user, ) not in cur.fetchall():
        if bnk_psswd.isnumeric() and len(bnk_psswd)==4:
            bank_wind.destroy()
            t=(bnk_user, randrange(50000,170000),bnk_psswd, usr)
            cur.execute(
                "INSERT INTO passenger (passengerid, password, name, phone_no, address, type) VALUES (%s, %s, %s, %s, %s,'user')",
                (usr, p, n, phno, addr))
            con.commit()
            cur.execute("Insert into bank_balence values((%s),(%s),(%s),(%s))",t)
            con.commit()
            login()
        else:
            messagebox.showerror("Pin Error", "Pin should be a 4 digit number")
    else:
        messagebox.showerror("user error", "Bank username should be unique... Try a differnt one.")


def vid():
    import pygame
    import moviepy.editor
    pygame.display.set_caption("bus_startup")
    pygame.init()
    video = moviepy.editor.VideoFileClip("assets\\bus_sample.mp4")
    video.preview()
    pygame.quit()


def password_checker(p):
    # paswd = paswd.get()
    d = {'l': 0, "u": 0, 'd': 0, 's': 0, 't': 0}
    for i in p:
        if i.isupper():
            d['u'] += 1
        elif i.islower():
            d['l'] += 1
        elif i.isnumeric():
            d['d'] += 1
        else:
            d['s'] += 1
    d['t'] += len(p)

    if d['u'] >= 1 and d['l'] >= 1 and d['d'] >= 1 and d['t'] >= 6:
        return True
    else:
        return False


passwod = ''
def login_destroyer():
    global Login_page
    global passwd
    global passwod
    passwod = passwd
    Login_page.destroy()
    # print(passwod)
    home_page()


def home_page():
    global g
    global img2
    global userid
    global nam
    global img1
    global home_pg
    global passwod

    home_pg = Tk(className=' Home Page')
    home_pg.resizable('False','False')
    img1 = PhotoImage(file="assets\\bus_login.png")
    home_pg.geometry("500x600")
    bg = Label(home_pg, image=img1)
    bg.place(anchor="center", x=250, y=300)

    cur.execute("Select name from passenger where password = (%s)", (passwod,))
    nam = cur.fetchall()
    # print(nam)
    nam = nam[0][0]
    Label(home_pg, text="Welcome " + nam, font=("Arial", 25), bg='#9abae0').place(y=39, x=254, anchor="center")
    Label(home_pg, text='Home Page', font=("courier", 20), bg='#9abae0').place(y=90, x=250, anchor="center")
    Label(home_pg, text='What  would  you  like  to  do  today ' + nam, font=("Arial", 13), bg='#b1ceeb').place(y=140,
                                                                                                                x=10)
    img2 = PhotoImage(file="assets\\user_icon.png")
    book_ticket = Button(home_pg, image=img2, command=dest_home)
    book_ticket.place(y=80, anchor="center", x=445)
    book_ticket = Button(home_pg, text="Book Ticket", command=book_tick, height=2, width=35, bg='#00A86b')
    book_ticket.place(y=200, anchor="center", x=250)
    book_ticket = Button(home_pg, text="See Booked Tickets", command=booked_tic, height=2, width=35,
                         bg='#00A86b')
    book_ticket.place(y=300, anchor="center", x=250)
    book_ticket = Button(home_pg, text="Cancel booked tickets", command=cancel_tickt, height=2, width=35,
                         bg='#00A86b')
    book_ticket.place(y=400, anchor="center", x=250)
    book_ticket = Button(home_pg, text="Bus Schedules", command=show_bus, height=2, width=35,
                         bg='#00A86b')
    book_ticket.place(y=500, anchor="center", x=250)

    home_pg.mainloop()


c=0
def book_tick():
    global depart
    global dest
    global cal
    global bus_class
    global ticket_book
    global seats_want
    global c

    # tuple(passwod)
    if c==0:
        global home_pg
        home_pg.destroy()

    ticket_book = Tk(className="ticket  booking")
    ticket_book.geometry("600x700")
    ticket_book.configure(background="#1e90ff")
    ticket_book.resizable('False','False')
    Label(ticket_book, text="Tell us where you would like to go", font=("Arial", 18), bg="#1e90ff").place(
        anchor="center", x=300, y=40)
    Label(ticket_book, text="Departure station:", font=("courier", 18), bg="#1e90ff").place(x=10, y=100)
    Label(ticket_book, text="Destination station:", font=("courier", 18), bg="#1e90ff").place(x=10, y=180)
    Label(ticket_book, text="Select a date:", font=("courier", 18), bg="#1e90ff").place(x=10, y=260)
    Label(ticket_book, text="Select a Class:", font=("courier", 18), bg="#1e90ff").place(x=10, y=520)
    Label(ticket_book, text="No of seats want", font=("courier", 18), bg="#1e90ff").place(x=10, y=580)



    cur.execute("Select depart from bus")
    dep1 = cur.fetchall()
    dep = []
    for i in dep1:
        if i[0] not in dep:
            dep.append(i[0])

    cur.execute("Select dest from bus")
    des1 = cur.fetchall()
    des = []
    for i in des1:
        if i[0] not in des:
            des.append(i[0])

    cur.execute("Select type_bus from bus")
    bus_type = cur.fetchall()
    buty = []
    for i in bus_type:
        if i[0] not in buty:
            buty.append(i[0])

    # print(dep, des, sep='\n')
    depart = ttk.Combobox(ticket_book, values=dep)
    depart.set(dep[0])
    dest = ttk.Combobox(ticket_book, values=des)
    dest.set(des[0])
    now = str(date.today())
    # print(now)
    cal = Calendar(ticket_book, selectmode='day', year=int(now[:4]), month=int(now[5:7]), day=int(now[8:]))
    bus_class = ttk.Combobox(ticket_book, values=buty)
    seats_want = Entry(ticket_book, borderwidth=3)
    bus_class.set("A/C")
    depart.place(x=300, y=107)
    dest.place(y=187, x=300)
    cal.place(anchor="nw", x=250, y=260)
    bus_class.place(x=250, y=527)
    seats_want.place(x=250, y=580)

    search_for_bus = Button(ticket_book, text="Check for bus", command=get_inp, height=2, width=35, bg='#00A86b')
    search_for_bus.place(x=170, y=640)

    ticket_book.mainloop()


def dest_home():
    global home_pg
    home_pg.destroy()
    user_settings()


def get_inp():
    global depart
    global dest
    global cal
    global bus_class
    global seats_want
    global cla
    global dep
    global des
    global calc
    global seats
    global l
    dep = depart.get()
    des = dest.get()
    calc = cal.selection_get()
    cla = bus_class.get()
    seats = seats_want.get()
    j=0
    if seats.isnumeric():
        if check_date(calc):
            check_for_bus()
        else:
            messagebox.showerror("Date Error", "Choose date in present or future!")
    else:
        messagebox.showerror("Type Error", "Seats required should be an integer")

    # if calc[0] >= l[2] and calc[1] >= l[0] and calc[


def check_for_bus():
    global dep
    global dest
    global calc
    global cla
    global bus_det

    cur.execute("select * from bus;")
    rec = cur.fetchall()
    d = (dep, des, cla)
    l = []
    for i in rec:
        l.append((i[2], i[3], i[4]))
    # print(l)
    # print(d)
    if d in l:
        print("Showing results for", dep, "to", des, "on", calc, "in", cla, "class")
        cur.execute("select * from bus where depart = (%s) and dest = (%s) and type_bus = (%s)",
                    (dep, des, cla))
        bus_det = cur.fetchall()
        if len(bus_det) > 1:
            print(tabulate(bus_det, headers=['bus number', 'Travels Agency name', 'Departure', "Destination", "Bus class",
                                             "Total number of seats", "Fare", "Status", "Available Seats"],
                           tablefmt='psql'))
        global ticket_book
        ticket_book.destroy()
        seat_check()
    else:
        messagebox.showerror("No bus found", "No bus found for entered details...")


def seat_check():
    global seats
    global bus_det
    global avail_seat
    avail_seat = []
    seats = int(seats)

    bus_avail = []
    for i in range(len(bus_det)):
        avail_seat.append(bus_det[i][8])
        bus_avail.append(bus_det[i][1])
    c = 0

    if len(bus_det) >= 1:
        for i in avail_seat:
            if int(i) >= seats:
                c += 1

    if c > 1:
        bus_want = input("What bus do you want? <Case Sensitive> : ")
        bus_want = bus_want.strip()
        s = ''
        c = 0
        for i in bus_want.split():
            if c == 0:
                s += i.strip()
                c+=1
            else:
                s +=  ' '+i.strip()
        bus_want = s
        print(bus_want)
        if bus_want in bus_avail:
            # print(bus_det)
            for i in range(len(bus_det)):
                if bus_det[i][1] == bus_want:
                    bus_det = [bus_det[i]]
                    avail_seat = int(bus_det[0][8])
                    payment()
                    break
        else:
            print("Bus not available for your needs.....")
            home_page()

    elif c == 1:
        for i in range(len(avail_seat)):
            if avail_seat[i] >= seats:
                bus_det = [bus_det[i]]
                avail_seat = int(bus_det[0][8])
                print(tabulate(bus_det,
                               headers=['bus number', 'Travels Agency name', 'Departure', "Destination", "Bus class",
                                        "Total number of seats", "Fare", "Status", "Available Seats"],
                               tablefmt='psql'))
        proceed = input("Proceed to payment? <yes, no>: ").lower()
        if proceed == 'yes':
            payment()
        else:
            home_page()
    else:
        print(seats, "seats are not available...","Only",avail_seat,"seats aare available...", '\n', "We are sorry for the "
                                                                                                "inconvenience")
        home_page()


def payment():
    global bus_det
    global seats
    global avail_seat
    global name
    global fare
    global payment_page
    global pin

    payment_page = Tk(className="payment")
    payment_page.geometry('750x450')
    payment_page.configure(background='#1e90ff')
    payment_page.resizable('False','False')
    fare = int(bus_det[0][6])*seats
    if avail_seat >= seats:
        Label(payment_page, text="Payment", font=("courier", 20), bg="#1e90ff").place(anchor="center", x=350, y=60)
        Label(payment_page, text="Amount to be paid: "+str(fare), font=("courier", 20), bg="#1e90ff").place(anchor="center", x=350, y=150)
        Label(payment_page, text="Enter Your bank ID: ",font=("courier", 17),bg="#1e90ff").place(anchor="center", x=270, y=230)
        Label(payment_page, text="Enter Your Bank Pin: ", font=("courier", 17), bg="#1e90ff").place(anchor="center", x=270, y=310)

        name = Entry(payment_page, borderwidth=3)
        name.place(anchor="center", x=580, y=230)
        pin = Entry(payment_page, show='$', borderwidth=3)
        pin.place(anchor="center", x=580, y=310)

        Button(payment_page, text="Pay", command=proceed_to_pay, height=2, width=35, bg='#00A86b').place(anchor='n', x=350, y=370)
        payment_page.mainloop()
    else:
        print(seats, "seats are not available...  Refer the table for more information.", '\n', "We are sorry for the "
                                                                                                "inconvenience")


def proceed_to_pay():
    global payment_page
    global name
    global fare
    global pin
    global bus_det
    global seats
    global avail_seat
    global nam
    busno = bus_det[0][0]
    na = name.get()
    pin = pin.get()
    t=(na,pin)
    payment_page.destroy()
    dep = bus_det[0][2]
    des = bus_det[0][3]
    cls = bus_det[0][4]
    cur.execute("select user_id,password from bank_balence")
    bank_det = cur.fetchall()
    if t not in bank_det:
        messagebox.showerror("Incorrect Credentials", "Incorrect Credentials... Incorrect ID or Pin")
        home_page()

    cur.execute("Select * from bank_balence where user_id = (%s)",(na,))
    bal = cur.fetchall()
    seat_change = avail_seat-seats
    # print(seats,avail_seat,seat_change, busno, sep='$')
    cur_bal = bal[0][1]
    if cur_bal >= fare:
        new_bal = cur_bal - fare
        # print(fare, bal, cur_bal, new_bal, sep='#')
        cur.execute("UPDATE bank_balence SET balence = (%s) WHERE user_id = (%s);",(new_bal, na))
        cur.execute("UPDATE bus SET avail_tickt = (%s) WHERE busno = (%s);",(seat_change, busno))
        cur.execute("select ticket_no from passenger_travel")
        no = cur.fetchall()
        for i in no:
            no = i
        no = no[0]
        tic_no = no+1
        today = date.today()
        today = str(today)
        # print(today)
        today = today[8:] + '-' + today[5:7] + '-' + today[0:4]
        cur.execute("Insert into passenger_travel values((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))",(nam, busno, dep, des, cls, fare, seats, tic_no, today))
        if seat_change==0:
            cur.execute("UPDATE bus SET statuss = 'Unavailable' WHERE busno = (%s);",(busno,))
        con.commit()
        print("Ticket Sucessfully Booked")
        home_page()
    else:
        messagebox.showerror("No cash", "You dont have sufficient bank balence to prodeed to payment")
        home_page()


def display(data):
    global book_show
    book_show= Tk(className=' Ticket Display')
    book_show.resizable('False','False')
    book_show.configure(bg='#9abae0')

    if len(data) > 0:
        Label(book_show, text="Name", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=0, padx=5, pady=5)
        Label(book_show, text="Bus_No", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=1, padx=5, pady=5)
        Label(book_show, text="Departure", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=2, padx=5, pady=5)
        Label(book_show, text="Destination", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=3, padx=5, pady=5)
        Label(book_show, text="Type", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=4, padx=5, pady=5)
        Label(book_show, text="Fare", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=5, padx=5, pady=5)
        Label(book_show, text="Seats", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=6, padx=5, pady=5)
        Label(book_show, text="Ticket No", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=7, padx=5, pady=5)
        Label(book_show, text="Date", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=8, padx=5, pady=5)

        for i in range(9):
            book_show.columnconfigure(i, weight=1)

        for i, row_data in enumerate(data):
            for j, value in enumerate(row_data):
                frame = Frame(book_show, relief=RIDGE,bg='#9abae0')
                frame.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
                label = Label(frame, text=value, font=('Arial', 12),bg='#9abae0')
                label.pack(padx=5,pady = 5)

    #print(tabulate(booked_tic,headers=["Name", "Bus Number", "Departure", 'Destination', "Bus Type", "Cash Transacted", "No of seats booked", 'Ticket Number', 'Date'], tablefmt='psql'))

    # home_page()


def booked_tic():
    global nam
    global userid
    global book_show
    cur.execute("Select * from passenger_travel where  name = (%s)", (nam,))
    booked_tic = cur.fetchall()
    if len(booked_tic) != 0:
        display(booked_tic)
    else:
        messagebox.showerror("no data", 'You have not booked any tickets')


# cancel tiket original
def cancel_tickt():
    global home_pg
    global nam

    cur.execute("Select * from passenger_travel where name = (%s)", (nam,))
    home_pg.destroy()
    booked_tic = cur.fetchall()

    if len(booked_tic) > 0:
        print(tabulate(booked_tic,
                       headers = ["Name", "Bus Number", "Departure", 'Destination', "Bus Type", "Cash Transacted",
                                "No of seats booked", "Ticket No.", "Date"], tablefmt='psql'),'\n\n')
        tic = input("Enter the ticket no you want to cancel: ")
        if tic.isnumeric():
            s_nos = []
            for i in range(len(booked_tic)):
                s_nos.append(str(booked_tic[i][7]))
                if str(booked_tic[i][7]) == tic:
                    booked_tic = booked_tic[i]
                    break
            l=[]
            l.append(booked_tic)
            # print(s_nos, booked_tic)
            # print(booked_tic)
            if tic in s_nos:
                print("Are you confirm that you want to cancel this ticket? This action cannot be undone")
                cur.execute("Select * from passenger_travel where ticket_no = (%s)", (tic, ))
                booked_tic = cur.fetchall()
                print(tabulate(booked_tic,
                               headers=["Name", "Bus Number", "Departure", 'Destination', "Bus Type", "Cash Transacted",
                                        "No of seats booked", "Ticket No.", "Date"], tablefmt='psql'), '\n\n')
                conf = input("<'yes', 'no'> :  ").lower()
                booked_tic = l
                if conf == 'yes':
                    usr = input("Enter Bank ID for refund: ")
                    psw = input('Enter the password for the above ID: ')
                    cur.execute("Select user_id, password from bank_balence")
                    det = cur.fetchall()
                    if (usr, psw) in det:
                        cur.execute("Select balence from bank_balence where user_id = (%s)",(usr,))
                        old_bal = int(list(cur.fetchall()[0])[0])
                        # print(old_bal, booked_tic[0][5])
                        new_bal = booked_tic[0][5] + old_bal
                        cur.execute("Delete from passenger_travel where ticket_no = (%s)",(tic,))
                        cur.execute("update bank_balence set balence = (%s) where user_id = (%s)",(new_bal, usr))
                        con.commit()
                        messagebox.showinfo("Done", "Ticket Sucessfully Canceled")
                        home_page()
                    else:
                        print("Wrong Bank ID or Password....")
                        home_page()
                else:
                    home_page()
            else:
                print("Incorrect ticket no...")
                home_page()
        else:
            print("Ticket no should be numeric....")
            home_page()
    else:

        messagebox.showinfo("NO INFO", "You have not booked any tickets yet....")
        home_page()


def show_bus():
    cur.execute("Select * from bus")
    bus = cur.fetchall()
    display_bus_all(bus)
    #print(tabulate(bus, headers=["Bus no.", "Travels Name", "Departure", "Destination",
    #                             "Type of Bus", "No of seats", "Fare", "Status", "Available_tickets"], tablefmt="psql"))
    # home_page()
b=0


def display_bus_all(data):
    global book_show
    book_show= Tk(className=' Ticket Display')
    book_show.resizable('False','False')
    book_show.configure(bg='#9abae0')

    if len(data) > 0:
        Label(book_show, text="Bus no.", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=0, padx=5, pady=5)
        Label(book_show, text="Travels name", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=1, padx=5, pady=5)
        Label(book_show, text="Departure", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=2, padx=5, pady=5)
        Label(book_show, text="Destination", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=3, padx=5, pady=5)
        Label(book_show, text="Type", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=4, padx=5, pady=5)
        Label(book_show, text="Total seats", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=5, padx=5, pady=5)
        Label(book_show, text="Fare", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=6, padx=5, pady=5)
        Label(book_show, text="Status", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=7, padx=5, pady=5)
        Label(book_show, text="Available Tickets", font=('Arial', 24, 'bold'),bg='#9abae0').grid(row=0, column=8, padx=5, pady=5)

        for i in range(9):
            book_show.columnconfigure(i, weight=1)

        for i, row_data in enumerate(data):
            for j, value in enumerate(row_data):
                frame = Frame(book_show, relief=RIDGE,bg='#9abae0')
                frame.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
                label = Label(frame, text=value, font=('Arial', 12),bg='#9abae0')
                label.pack(padx=5,pady = 5)

    #print(tabulate(booked_tic,headers=["Name", "Bus Number", "Departure", 'Destination', "Bus Type", "Cash Transacted", "No of seats booked", 'Ticket Number', 'Date'], tablefmt='psql'))

    # home_page()



def user_settings():
    # global home_pg
    global b
    global passwod
    global setting_pg
    global frame
    global name
    global usr_id

    b+=1
    p = passwod
    cur.execute("Select * from passenger where password = (%s)", (p, ))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]

    setting_pg = Tk(className="user profile")
    frame = Frame(setting_pg)
    setting_pg.geometry('500x550')
    setting_pg.resizable('False','False')
    frame.pack(side="top", expand=True, fill="both")
    frame.configure(bg="#1e90ff")

    Label(frame, text="User Profile", font=('Arial', 20), bg="#1e90ff").pack()
    Label(frame, text="Name:   "+name, font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(frame, text="User ID:   "+usr_id, font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(frame, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(frame, text="Phone Number:   "+ph_no, font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(frame, text="Address:   "+address, font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    Button(frame, text="Log Out", font=("courier", 10), bg='#00A86b', command=back_to_login).pack()
    Button(frame, text="Change User name", font=("courier", 10), bg='#00A86b', command=name_chng).place(x=345, y=80)
    Button(frame, text="Change User ID", font=("courier", 10), bg='#00A86b', command=usr_chng).place(x=350, y=160)
    Button(frame, text="Change Password", font=("courier", 10), bg='#00A86b', command=paswd_chng).place(x=350, y=240)
    Button(frame, text="Change Phone number", font=("courier", 10), bg='#00A86b', command=phno_chng).place(x=320, y=320)
    Button(frame, text="Change Address", font=("courier", 10), bg='#00A86b', command=address_chng).place(x=350, y=440)


    setting_pg.mainloop()


def back_to_login():
    global setting_pg
    setting_pg.destroy()
    login()


def address_chng():
    global setting_pg
    global tick
    global frame
    global new_addrs
    global passwod
    global name
    p = passwod
    for widgets in frame.winfo_children():
        widgets.destroy()

    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    setting_pg.configure(background="#1e90ff")
    setting_pg.resizable('False','False')
    Label(setting_pg, text="Change User Details", font=('Arial', 20), bg="#1e90ff").pack()
    Label(setting_pg, text="Name:   "+name, font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(setting_pg, text="User ID:   "+usr_id, font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(setting_pg, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(setting_pg, text="Phone number:   "+ph_no , font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(setting_pg, text="Enter your new address:", font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    new_addrs = Entry(setting_pg, borderwidth=3)
    new_addrs.place(x=320, y=400)

    tick = PhotoImage(file="assets\\conf.png")
    Button(setting_pg, image=tick, bg='#00C055', command=change_address).place(x=427, y=420)



def change_address():
    global img1
    global img2
    global new_addrs
    global usr_id
    global setting_pg
    usr_id = usr_id
    new_addr = new_addrs.get()
    if len(new_addr.split()) > 2 and len(new_addr) < 65:
        setting_pg.destroy()
        cur.execute("update passenger set address = (%s) where passengerid = (%s)",(new_addr, usr_id))
        con.commit()
        home_page()
    else:
        messagebox.showerror("Address Error","Address should have atleast 3 words and donot exceed 40 charecters")


def phno_chng():
    global setting_pg
    global tick
    global frame
    global new_phno
    global passwod
    global name
    p = passwod
    for widgets in frame.winfo_children():
        widgets.destroy()

    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    setting_pg.configure(background="#1e90ff")
    setting_pg.resizable('False','False')
    Label(setting_pg, text="Change User Details", font=('Arial', 20), bg="#1e90ff").pack()
    Label(setting_pg, text="Name:   "+name, font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(setting_pg, text="User ID:   "+usr_id, font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(setting_pg, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(setting_pg, text="Enter your new phone number:" , font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(setting_pg, text="Address:   " + address, font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    new_phno = Entry(setting_pg, borderwidth=3)
    new_phno.place(x=320, y=320)

    tick = PhotoImage(file="assets\\conf.png")
    Button(setting_pg, image=tick, bg='#00C055', command=change_phno).place(x=420, y=420)


def change_phno():
    global img1
    global img2
    global new_phno
    global usr_id
    global setting_pg
    usr_id = usr_id
    new_phn = new_phno.get()
    if len(new_phn) == 10 and new_phn.isnumeric():
        cur.execute("update passenger set phone_no = (%s) where passengerid = (%s)",(new_phn, usr_id))
        con.commit()
        setting_pg.destroy()
        home_page()
    else:
        messagebox.showerror("Phone no Error", "Phone number should be an integer of 10 charecters")


o=0
def paswd_chng():
    global setting_pg
    global tick
    global frame
    global old_pswd
    global new_pswd
    global conf_pswd
    global passwod
    global name
    p = passwod
    for widgets in frame.winfo_children():
        widgets.destroy()

    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    setting_pg.configure(background="#1e90ff")
    setting_pg.resizable('False','False')
    Label(setting_pg, text="Change password", font=('Arial', 20), bg="#1e90ff").pack()
    Label(setting_pg, text="Enter your old password:", font=("Arial", 15), bg="#1e90ff").place(x=20, y=130)
    Label(setting_pg, text="Enter new password:" , font=("Arial", 15), bg="#1e90ff").place(x=20, y=260)
    Label(setting_pg, text="Confirm new password:", font=("Arial", 15), bg="#1e90ff").place(x=20, y=390)

    old_pswd = Entry(setting_pg, show='*' , borderwidth=3)
    old_pswd.place(x=320, y=130)

    new_pswd = Entry(setting_pg, show='*' , borderwidth=3)
    new_pswd.place(x=320, y=260)

    conf_pswd = Entry(setting_pg, show='*', borderwidth=3)
    conf_pswd.place(x=320, y=390)

    tick = PhotoImage(file="assets\\conf.png")
    Button(setting_pg, image=tick, bg='#00C055', command=change_passwd).place(x=420, y=420)


def change_passwd():
    global img1
    global img2
    global old_pswd
    global new_pswd
    global conf_pswd
    global usr_id
    global setting_pg
    usr_id = usr_id
    new_pswd = new_pswd.get()
    old_pswd = old_pswd.get()
    conf_pswd = conf_pswd.get()
    setting_pg.destroy()
    cur.execute("select password from passenger where passengerid = (%s)", (usr_id, ))
    crt_pswd = cur.fetchall()
    if (old_pswd, ) in crt_pswd:
        if password_checker(new_pswd):
            if new_pswd == conf_pswd:
                cur.execute("update passenger set password = (%s) where passengerid = (%s)", (new_pswd, usr_id))
                con.commit()
                login()
            else:
                messagebox.showwarning("Password doesnt match", "New Password and Confirm Password doesnt march")
                user_settings()
                # signup_wind()
        else:
            messagebox.showwarning("Password Error",
                                   "Choose strong password with least 6 characters, 1 upper case,lowercase and digit")
            user_settings()
    else:
        messagebox.showerror("Password doesnt match", "Incorrect old password....")
        user_settings()


def name_chng():
    global setting_pg
    global tick
    global frame
    global new_name
    global passwod
    global name
    p = passwod

    setting_pg.destroy()
    setting_pg = Tk(className="user profile")
    frame = Frame(setting_pg)
    setting_pg.geometry('500x500')
    setting_pg.resizable('False','False')
    frame.pack(side="top", expand=True, fill="both")
    frame.configure(bg="#1e90ff")

    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    # setting_pg.configure(background="#1e90ff")
    Label(frame, text="Change User Details", font=('Arial', 20), bg="#1e90ff").pack()
    Label(frame, text="Enter your new name:   ", font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(frame, text="User ID:   "+usr_id, font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(frame, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(frame, text="Phone Number:   " + ph_no, font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)

    Label(frame, text="Address:   " + address, font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    new_name = Entry(frame, borderwidth=3)
    new_name.place(x=320, y=80)

    tick = PhotoImage(file="assets\\conf.png")
    Button(frame, image=tick, bg='#00C055', command=change_name).place(x=420, y=420)


def change_name():
    global img1
    global img2
    global new_name
    global usr_id
    global name
    global setting_pg
    usr_id = usr_id
    name1 = new_name.get()
    # print(usr_id,name)
    if len(name)>2:
        setting_pg.destroy()
        cur.execute("update passenger set name = (%s) where passengerid = (%s)",(name1, usr_id))
        cur.execute("update passenger_travel set name = (%s) where name = (%s)", (name1, name))
        con.commit()
        home_page()
    else:   
        messagebox.showerror("name error",'name should have atlest 3 letters')
        user_settings()


def usr_chng():
    global setting_pg
    global tick
    global frame
    global new_user_id
    global passwod
    p = passwod
    for widgets in frame.winfo_children():
        widgets.destroy()



    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    setting_pg.configure(background="#1e90ff")
    setting_pg.resizable('False','False')
    Label(setting_pg, text="Change User Details", font=('Arial', 20), bg="#1e90ff").pack()
    Label(setting_pg, text="Name:   " + name, font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(setting_pg, text="Enter your new User ID:   ", font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(setting_pg, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(setting_pg, text="Phone Number:   " + ph_no, font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(setting_pg, text="Address:   " + address, font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    new_user_id = Entry(setting_pg, borderwidth=3)
    new_user_id.place(x=320, y=160)

    tick = PhotoImage(file="assets\\conf.png")
    Button(setting_pg, image=tick, bg='#00C055', command=change_usr).place(x=420, y=420)


def change_usr():
    global new_user_id
    global usr_id
    global setting_pg
    usr_id = usr_id
    usr = new_user_id.get()
    cur.execute("Select passengerid from passenger")
    usr_lst = cur.fetchall()
    if "@" in usr and len(usr.split('@')[0]) > 0 and len(usr.split('@')[1]) > 0:
        if (usr, ) in usr_lst:
            setting_pg.destroy()
            cur.execute("update passenger set passengerid = (%s) where passengerid = (%s)",(new_user_id, usr_id))
            con.commit()
            login()
        else:
            messagebox.showerror('user id error', 'User id already taken... Choose another one.')
    else:
        messagebox.showerror("user if error", 'user id should have an "@", something before it and after it...')






################################################### ADMIN SIDE #################################################




def admin_login_destroyer():
    global Login_page
    global passwd
    global passwod
    passwod = passwd
    Login_page.destroy()
    admin_home()


def admin_home():
    global passwod
    global img1
    global home_pg
    home_pg = Tk()
    img1 = PhotoImage(file="assets\\bus_login.png")
    home_pg.geometry("500x600")
    home_pg.resizable('False','False')

    bg = Label(home_pg, image=img1)
    bg.place(anchor="center", x=250, y=300)

    cur.execute("Select name from passenger where password = (%s)", (passwod,))
    nam = cur.fetchall()
    # print(nam)
    nam = nam[0][0]
    Label(home_pg, text="Welcome " + nam, font=("Arial", 25), bg='#9abae0').place(y=39, x=254, anchor="center")
    Label(home_pg, text='Home Page', font=("courier", 20), bg='#9abae0').place(y=90, x=250, anchor="center")
    Label(home_pg, text='What  would  you  like  to  do  today ' + nam, font=("Arial", 13), bg='#b1ceeb').place(y=140,
                                                                                                                x=10)
    img2 = PhotoImage(file="assets\\user_icon.png")
    book_ticket = Button(home_pg, image=img2, command=admin_home_destroyer)
    book_ticket.place(y=80, anchor="center", x=445)

    book_ticket = Button(home_pg, text="Add Bus", command=add_bus, height=2, width=35, bg='#00A86b')
    book_ticket.place(y=220, anchor="center", x=250)

    book_ticket = Button(home_pg, text="Remove Bus", command=remove_bus, height=2, width=35,
                         bg='#00A86b')
    book_ticket.place(y=300, anchor="center", x=250)

    book_ticket = Button(home_pg, text="Remove Passenger", command=remove_passenger, height=2, width=35,
                         bg='#00A86b')
    book_ticket.place(y=380, anchor="center", x=250)

    book_ticket = Button(home_pg, text="Add passenger", command=add_passenger, height=2, width=35,
                         bg='#00A86b')
    book_ticket.place(y=460, anchor="center", x=250)

    book_ticket = Button(home_pg, text="Add admin", command=add_admin, height=2, width=35,
                         bg='#00A86b')
    book_ticket.place(y=540, anchor="center", x=250)

    home_pg.mainloop()


def add_admin():
    global home_pg
    home_pg.destroy()
    cur.execute('select * from passenger where type = "user"')
    usrs = cur.fetchall()
    print(tabulate(usrs, headers=['Passenger ID', 'Password', 'Name', "Phone Number", "Address",
                                     "Type"],
                   tablefmt='psql'))
    print("Who do you want to make as admin? : ")
    usr = input("Enter user ID: ")
    l = []
    for i in usrs:
        if usr == i[0]:
            l = i
    if l == []:
        print("Not valid user id..")
        admin_home()
    else:
        cur.execute("update passenger set type = 'admin' where passengerid = (%s)",(usr,))
        con.commit()
        print("Sucessfuly Completed..")
        admin_home()


def admin_home_destroyer():
    global home_pg
    home_pg.destroy()
    admin_settings()


def admin_settings():
    global passwod
    global setting_pg
    global frame
    global usr_id

    p = passwod

    cur.execute("Select * from passenger where password = (%s)", (p, ))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]

    setting_pg = Tk(className="admin profile")
    frame = Frame(setting_pg)
    setting_pg.geometry('600x550')
    setting_pg.resizable('False','False')
    frame.pack(side="top", expand=True, fill="both")
    frame.configure(bg="#1e90ff")

    Label(frame, text="Admin Profile", font=('Arial', 20), bg="#1e90ff").pack()
    Label(frame, text="Name:   "+name, font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(frame, text="User ID:   "+usr_id, font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(frame, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(frame, text="Phone Number:   "+ph_no, font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(frame, text="Address:   "+address, font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    Button(frame, text="Log Out", font=("courier", 10), bg='#00A86b', command=back_to_login).pack()
    Button(frame, text="Change User name", font=("courier", 10), bg='#00A86b', command=admin_name_chng).place(x=350, y=80)
    Button(frame, text="Change User User ID", font=("courier", 10), bg='#00A86b', command=admin_usr_chng).place(x=320, y=160)
    Button(frame, text="Change Password", font=("courier", 10), bg='#00A86b', command=admin_paswd_chng).place(x=350, y=240)
    Button(frame, text="Change Phone number", font=("courier", 10), bg='#00A86b', command=admin_phno_chng).place(x=320, y=320)
    Button(frame, text="Change Address", font=("courier", 10), bg='#00A86b', command=admin_address_chng).place(x=350, y=440)
    Button(frame, text='Back to home', font=('Arial',12), bg='#00A86b', command = return_home1).place(x=70, y=500)


    setting_pg.mainloop()



def admin_address_chng():
    global setting_pg
    global tick
    global frame
    global new_addrs
    global passwod
    global name
    p = passwod
    for widgets in frame.winfo_children():
        widgets.destroy()

    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    setting_pg.configure(background="#1e90ff")
    setting_pg.resizable('False','False')
    Label(setting_pg, text="Change User Details", font=('Arial', 20), bg="#1e90ff").pack()
    Label(setting_pg, text="Name:   "+name, font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(setting_pg, text="User ID:   "+usr_id, font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(setting_pg, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(setting_pg, text="Phone number:   "+ph_no , font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(setting_pg, text="Enter your new address:", font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    new_addrs = Entry(setting_pg, borderwidth=3)
    new_addrs.place(x=320, y=400)

    tick = PhotoImage(file="assets\\conf.png")
    Button(setting_pg, image=tick, bg='#00C055', command=admin_change_address).place(x=427, y=420)


def admin_change_address():
    global img1
    global img2
    global new_addrs
    global usr_id
    global setting_pg
    usr_id = usr_id
    new_addr = new_addrs.get()
    if len(new_addr.split()) > 2 and len(new_addr) < 65:
        setting_pg.destroy()
        cur.execute("update passenger set address = (%s) where passengerid = (%s)",(new_addr, usr_id))
        con.commit()
        admin_home()
    else:
        messagebox.showerror("Address Error","Address should have atleast 3 words and donot exceed 40 charecters")


def admin_phno_chng():
    global setting_pg
    global tick
    global frame
    global new_phno
    global passwod
    global name
    p = passwod
    for widgets in frame.winfo_children():
        widgets.destroy()

    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    setting_pg.configure(background="#1e90ff")
    setting_pg.resizable('False','False')
    Label(setting_pg, text="Change User Details", font=('Arial', 20), bg="#1e90ff").pack()
    Label(setting_pg, text="Name:   "+name, font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(setting_pg, text="User ID:   "+usr_id, font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(setting_pg, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(setting_pg, text="Enter your new phone number:" , font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(setting_pg, text="Address:   " + address, font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    new_phno = Entry(setting_pg, borderwidth=3)
    new_phno.place(x=320, y=320)

    tick = PhotoImage(file="assets\\conf.png")
    Button(setting_pg, image=tick, bg='#00C055', command=admin_change_phno).place(x=420, y=420)


def admin_change_phno():
    global img1
    global img2
    global new_phno
    global usr_id
    global setting_pg
    usr_id = usr_id
    new_phn = new_phno.get()
    if len(new_phn) == 10 and new_phn.isnumeric():
        cur.execute("update passenger set phone_no = (%s) where passengerid = (%s)",(new_phn, usr_id))
        con.commit()
        setting_pg.destroy()
        admin_home()
    else:
        messagebox.showerror("Phone no Error", "Phone number should be an integer of 10 charecters")


o=0
def admin_paswd_chng():
    global setting_pg
    global tick
    global frame
    global old_pswd
    global new_pswd
    global conf_pswd
    global passwod
    global name
    p = passwod
    for widgets in frame.winfo_children():
        widgets.destroy()

    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    setting_pg.configure(background="#1e90ff")
    setting_pg.resizable('False','False')
    Label(setting_pg, text="Change password", font=('Arial', 20), bg="#1e90ff").pack()
    Label(setting_pg, text="Enter your old password:", font=("Arial", 15), bg="#1e90ff").place(x=20, y=130)
    Label(setting_pg, text="Enter new password:" , font=("Arial", 15), bg="#1e90ff").place(x=20, y=260)
    Label(setting_pg, text="Confirm new password:", font=("Arial", 15), bg="#1e90ff").place(x=20, y=390)

    old_pswd = Entry(setting_pg, borderwidth=3)
    old_pswd.place(x=320, y=130)

    new_pswd = Entry(setting_pg, borderwidth=3)
    new_pswd.place(x=320, y=260)

    conf_pswd = Entry(setting_pg, borderwidth=3)
    conf_pswd.place(x=320, y=390)

    tick = PhotoImage(file="assets\\conf.png")
    Button(setting_pg, image=tick, bg='#00C055', command=admin_change_passwd).place(x=420, y=420)


def admin_change_passwd():
    global img1
    global img2
    global old_pswd
    global new_pswd
    global conf_pswd
    global usr_id
    global setting_pg
    usr_id = usr_id
    new_pswd = new_pswd.get()
    old_pswd = old_pswd.get()
    conf_pswd = conf_pswd.get()
    setting_pg.destroy()
    cur.execute("select password from passenger where passengerid = (%s)", (usr_id, ))
    crt_pswd = cur.fetchall()
    if (old_pswd, ) in crt_pswd:
        if password_checker(new_pswd):
            if new_pswd == conf_pswd:
                cur.execute("update passenger set password = (%s) where passengerid = (%s)", (new_pswd, usr_id))
                con.commit()
                admin_home()
            else:
                messagebox.showwarning("Password doesnt match", "New Password and Confirm Password doesnt march")
                admin_settings()
                # signup_wind()
        else:
            messagebox.showwarning("Password Error",
                                   "Choose strong password with least 6 characters, 1 upper case,lowercase and digit")
            admin_settings()
    else:
        messagebox.showerror("Password doesnt match", "Incorrect old password....")
        admin_settings()


def admin_name_chng():
    global setting_pg
    global tick
    global frame
    global new_name
    global passwod
    global name
    p = passwod

    setting_pg.destroy()
    setting_pg = Tk(className="user profile")
    frame = Frame(setting_pg)
    setting_pg.geometry('500x500')
    setting_pg.resizable('False','False')
    frame.pack(side="top", expand=True, fill="both")
    frame.configure(bg="#1e90ff")

    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    # setting_pg.configure(background="#1e90ff")
    Label(frame, text="Change User Details", font=('Arial', 20), bg="#1e90ff").pack()
    Label(frame, text="Enter your new name:   ", font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(frame, text="User ID:   "+usr_id, font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(frame, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(frame, text="Phone Number:   " + ph_no, font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(frame, text="Address:   " + address, font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    new_name = Entry(frame, borderwidth=3)
    new_name.place(x=320, y=80)

    tick = PhotoImage(file="assets\\conf.png")
    Button(frame, image=tick, bg='#00C055', command=admin_change_name).place(x=420, y=420)


def admin_change_name():
    global img1
    global img2
    global new_name
    global usr_id
    global setting_pg
    usr_id = usr_id
    name = new_name.get()
    # print(usr_id,name)
    if len(name)>2:
        setting_pg.destroy()
        cur.execute("update passenger set name = (%s) where passengerid = (%s)",(name, usr_id))
        con.commit()
        admin_home()
    else:
        messagebox.showerror("name error",'name should have atlest 3 letters')
        admin_settings()


def admin_usr_chng():
    global setting_pg
    global tick
    global frame
    global new_user_id
    global passwod
    p = passwod
    for widgets in frame.winfo_children():
        widgets.destroy()



    cur.execute("Select * from passenger where password = (%s)", (p,))
    stat = cur.fetchall()
    stat = stat[0]
    usr_id = stat[0]
    paswd = stat[1]
    name = stat[2]
    ph_no = stat[3]
    address = stat[4]
    setting_pg.configure(background="#1e90ff")
    setting_pg.resizable('False','False')
    Label(setting_pg, text="Change User Details", font=('Arial', 20), bg="#1e90ff").pack()
    Label(setting_pg, text="Name:   " + name, font=("Arial", 15), bg="#1e90ff").place(x=20, y=80)
    Label(setting_pg, text="Enter your new User ID:   ", font=("Arial", 15), bg="#1e90ff").place(x=20, y=160)
    Label(setting_pg, text="Password:   *******", font=("Arial", 15), bg="#1e90ff").place(x=20, y=240)
    Label(setting_pg, text="Phone Number:   " + ph_no, font=("Arial", 15), bg="#1e90ff").place(x=20, y=320)
    Label(setting_pg, text="Address:   " + address, font=("Arial", 15), bg="#1e90ff").place(x=20, y=400)

    new_user_id = Entry(setting_pg, borderwidth=3)
    new_user_id.place(x=320, y=160)

    tick = PhotoImage(file="assets\\conf.png")
    Button(setting_pg, image=tick, bg='#00C055', command=admin_change_usr).place(x=420, y=420)


def admin_change_usr():
    global new_user_id
    global usr_id
    global setting_pg
    usr_id = usr_id
    usr = new_user_id.get()
    cur.execute("Select passengerid from passenger")
    usr_lst = cur.fetchall()
    if "@" in usr and len(usr.split('@')[0]) > 0 and len(usr.split('@')[1]) > 0:
        if (usr, ) in usr_lst:
            setting_pg.destroy()
            cur.execute("update passenger set passengerid = (%s) where passengerid = (%s)",(new_user_id, usr_id))
            con.commit()
            login()
        else:
            messagebox.showerror('user id error', 'User id already taken... Choose another one.')
    else:
        messagebox.showerror("user if error", 'user id should have an "@", something before it and after it...')





def return_home1():
    global setting_pg
    setting_pg.destroy()
    admin_home()


def remove_passenger():
    global home_pg
    home_pg.destroy()
    global usr
    global user_remove

    user_remove = Tk(className=" Remove Bus")
    user_remove.geometry("600x200")
    user_remove.configure(background="#1e90ff")
    user_remove.resizable('False','False')
    Label(user_remove, text='Remove Passenger', font=("courier", 20), bg="#1e90ff").pack()
    Label(user_remove, text="Enter the user name of ", font=("courier", 16),
          bg="#1e90ff").place(x=5, y=60)
    Label(user_remove, text="the user you want to remove:", font=("courier", 16),
          bg="#1e90ff").place(x=5, y=90)

    usr = Entry(user_remove, borderwidth=3)
    usr.place(x=400, y=75)

    Button(user_remove, text="Remove Passenger", bg="#1e90ff", command=removeuser).place(anchor='center', x=300, y=170)



def removeuser():
    global usr

    user_id = usr.get()
    cur.execute("select passengerid from passenger")
    user = cur.fetchall()
    # print(user)
    users = []
    for i in user:
        users.append(i[0])
    if user_id in users:
        cur.execute("delete from passenger where passengerid = (%s)", (user_id, ))
        cur.execute("delete from bank_balence where passengerid = (%s)", (user_id, ))
        con.commit()
        global user_remove
        user_remove.destroy()
        admin_home()
    else:
        messagebox.showerror("", "User with this userid is not available")


def remove_bus():
    global buno
    global bus_remove
    global home_pg
    home_pg.destroy()

    bus_remove = Tk(className=" Remove Bus")
    bus_remove.geometry("600x200")
    bus_remove.configure(background="#1e90ff")
    bus_remove.resizable('False','False')
    Label(bus_remove, text='Remove Bus', font=("courier", 20), bg="#1e90ff").pack()
    Label(bus_remove, text="Enter the bus number of ", font=("courier", 16),
          bg="#1e90ff").place(x=5, y=60)
    Label(bus_remove, text="the bus you want to remove:", font=("courier", 16),
          bg="#1e90ff").place(x=5, y=90)

    buno = Entry(bus_remove, borderwidth=3)
    buno.place(x=400, y=75)

    Button(bus_remove, text="Remove Bus", bg="#1e90ff", command=removebus).place(anchor='center', x=300, y=170)


def removebus():
    global buno
    global bus_remove
    busno = buno.get()

    cur.execute("select busno from bus")
    bno = cur.fetchall()
    # print(buno)
    busnos = []
    for i in bno:
        busnos.append(i[0])

    if busno.isnumeric():
        if int(busno) in busnos:
            cur.execute("delete from bus where busno = (%s)", (busno,))
            con.commit()
            global bus_remove
            bus_remove.destroy()
            admin_home()
        else:
            messagebox.showerror("","Bus in this bus number is not available")
            bus_remove.destroy()
            admin_home()
    else:
        messagebox.showerror("","Bus number should be a number...")
        bus_remove.destroy()
        admin_home()


def add_bus():
    global depart
    global dest
    global cls
    global agency
    global busno
    global tot_seat
    global fare
    global avail_seat
    global ticket_book

    # tuple(passwod)
    global home_pg
    home_pg.destroy()

    ticket_book = Tk(className=" Bus Adding")
    ticket_book.geometry("600x700")
    ticket_book.configure(background="#1e90ff")
    ticket_book.resizable('False','False')
    Label(ticket_book, text="Add Bus", font=("Arial", 18), bg="#1e90ff").place(
        anchor="center", x=300, y=40)
    Label(ticket_book, text="Bus Number:", font=("courier", 18), bg="#1e90ff").place(x=10, y=100)
    Label(ticket_book, text="Travels Name:", font=("courier", 18), bg="#1e90ff").place(x=10, y=160)
    Label(ticket_book, text="Departure station:", font=("courier", 18), bg="#1e90ff").place(x=10, y=220)
    Label(ticket_book, text="Destination station:", font=("courier", 18), bg="#1e90ff").place(x=10, y=280)
    Label(ticket_book, text="Type of bus:", font=("courier", 18), bg="#1e90ff").place(x=10, y=340)
    Label(ticket_book, text="Total no of seats:", font=("courier", 18), bg="#1e90ff").place(x=10, y=400)
    Label(ticket_book, text="Fare", font=("courier", 18), bg="#1e90ff").place(x=10, y=460)
    Label(ticket_book, text="No of available seats:", font=("courier", 18), bg="#1e90ff").place(x=10, y=520)


    busno = Entry(ticket_book, borderwidth=3)
    busno.place(x=320, y=100)
    agency = Entry(ticket_book, borderwidth=3)
    agency.place(x=320, y=160)
    depart = Entry(ticket_book, borderwidth=3)
    depart.place(x=320, y=220)
    dest = Entry(ticket_book, borderwidth=3)
    dest.place(x=320, y=280)
    cls = ttk.Combobox(ticket_book, values=['A/C','Non A/C'])
    cls.set('A/C')
    cls.place(x=320, y=340)
    tot_seat = Entry(ticket_book, borderwidth=3)
    tot_seat.place(x=320, y=400)
    fare = Entry(ticket_book, borderwidth=3)
    fare.place(x=320, y=460)
    avail_seat = Entry(ticket_book, borderwidth=3)
    avail_seat.place(x=320, y=520)

    search_for_bus = Button(ticket_book, text="Check for bus", command=get_bus_inp, height=2, width=35, bg='#00A86b')
    search_for_bus.place(x=170, y=640)

    ticket_book.mainloop()


def get_bus_inp():
    global depart
    global dest
    global cls
    global agency
    global busno
    global tot_seat
    global fare
    global avail_seat
    global ticket_book
    # print(depart,dest,cls,agency,busno,tot_seat,fare,avail_seat)

    dep = depart.get()
    des = dest.get()
    cla = cls.get()
    travels = agency.get()
    bno = busno.get()
    t_seat = tot_seat.get()
    cost = fare.get()
    seat_avail = avail_seat.get()

    cur.execute("select busno from bus")
    buno = cur.fetchall()
    # print(buno)
    busnos = []
    for i in buno:
        busnos.append(i[0])
    # print(busnos)
    # print(bno,dep,des,cla,t_seat,seat_avail,cost,travels, sep='# ')
    # print(alpha(dep), alpha(des), alpha(travels))
    if "" not in  [bno,dep,des,cla,t_seat,seat_avail,cost,travels]:
        if bno.isnumeric():
            if int(bno) not in busnos:
                if t_seat.isnumeric():
                    if cost.isnumeric():
                        if seat_avail.isnumeric():
                            if int(t_seat) >= int(seat_avail):
                                if alpha(dep) and alpha(des) and alpha(travels):
                                    if  cla in ['A/C', 'Non A/C']:
                                        if int(seat_avail) > 0:
                                            cur.execute("insert into bus values((%s),(%s),(%s),(%s),(%s),(%s),(%s),'Available',(%s))",
                                                        (bno,travels,dep,des,cla,t_seat,cost, seat_avail))
                                            ticket_book.destroy()
                                            con.commit()
                                            admin_home()
                                        else:
                                            cur.execute(
                                                "insert into bus values((%s),(%s),(%s),(%s),(%s),(%s),(%s),'Unavailable',(%s),(%s))",
                                                (bno, travels, dep, des, cla, t_seat, cost, seat_avail))
                                            ticket_book.destroy()
                                            con.commit()

                                            admin_home()
                                    else:
                                        messagebox.showerror("", "Bus type or class should be <'AC' or 'Non A/C'> Case Sensitive")
                                else:
                                    messagebox.showerror("", "Departure, Destination, travels agency name, shold be string...."
                                                             "   Bus type or class should be <A/C or Non A/C> Case sensitive")
                            else:
                                messagebox.showerror("", "available seats should be less than total seats")
                        else:
                            messagebox.showerror("","No. of available seats should be integer")
                    else:
                        messagebox.showerror("","Fare should be an integer value")
                else:
                    messagebox.showerror("","Total seats should be an integer value")
            else:
                messagebox.showerror("","Bus no should be unique..")
        else:
            messagebox.showerror("","Bus number should be a integer value")
    else:
        messagebox.showerror("","all fields are required")
    # print(dep,des,cla,travels,bno,t_seat,cost,seat_avail)


def alpha(a):
    q=0
    a = a.split()
    if len(a) == 0:
        return False
    for i in a:
        if i == ' ':
            q-=1
        elif i.isalpha():
            q+=1
        # print(i, end='$')
    if q == len(a):
        return True


l=0
def add_passenger():
    global address
    global name
    global usr_id
    global paswd
    global ph_no
    global conf_paswd
    global signpage
    global l
    global home_pg
    l+=1
    signpage = Tk(className=" Sign Up page")
    signpage.geometry('500x700')
    signpage.configure(bg='#b1ceeb')
    signpage.resizable('False','False')

    if l ==1:
        home_pg.destroy()

    signup_tst = Label(signpage, text="Add Passenger", font=('courier', 30), bg='#b1ceeb')
    signup_tst.pack()

    Label(signpage, text='Name:', font=("courier", 18), bg='#b1ceeb').place(y=100)
    Label(signpage, text='Address:', font=("courier", 18), bg='#b1ceeb').place(y=180)
    Label(signpage, text="Phone Number:", font=("courier", 18), bg='#b1ceeb').place(y=260)
    Label(signpage, text='User Id:', font=("courier", 18), bg='#b1ceeb').place(y=340)
    Label(signpage, text='Password:', font=("courier", 18), bg='#b1ceeb').place(y=420)
    Label(signpage, text='Confirm Password:', font=("courier", 18), bg='#b1ceeb').place(y=520)

    name = Entry(signpage, borderwidth=3)
    address = Entry(signpage, borderwidth=3)
    ph_no = Entry(signpage, borderwidth=3)
    usr_id = Entry(signpage, borderwidth=3)
    paswd = Entry(signpage, show="*", borderwidth=3)
    conf_paswd = Entry(signpage, show="*", borderwidth=3)

    ph_no.place(x=200, y=265)
    address.place(x=200, y=185)
    name.place(x=200, y=105)
    usr_id.place(x=200, y=345)
    paswd.place(x=200, y=425)
    conf_paswd.place(x=250, y=525)
    button = Button(signpage, text="Add passenger", command=dest_signp, height=2, width=40, bg='#00A86b')
    button.place(x=110, y=600)

    signpage.mainloop()


login()
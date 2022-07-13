from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
import mysql.connector as sql
import requests
import json
import os

mycon = sql.connect(host='localhost', user='root', passwd='root', database='test')
cur = mycon.cursor()
p1=""
p2=""
p3=""
p4=""
p5=""


count1 = 0
count2 = 0


class Register:
    def __init__(self, root):

        self.Namedata = StringVar()
        self.pricedata = StringVar()
        self.ramdata = StringVar()
        self.ISdata = StringVar()
        self.fcdata = StringVar()
        self.rcdata = StringVar()
        self.Namedata2 = StringVar()
        self.pricedata2 = StringVar()
        self.ramdata2 = StringVar()
        self.ISdata2 = StringVar()
        self.fcdata2 = StringVar()
        self.rcdata2 = StringVar()
        self.searchTerm1 = StringVar()
        self.searchTerm2 = StringVar()
        self.root = root
        self.root.title("Registration window")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg="orange")
        self.rec = StringVar()
        global frame1
        # bg
        self.bg = ImageTk.PhotoImage(file="C:\\Users\\Nisarg Saraiya\\Downloads\\joel-filipe-QwoNAhbmLLo-unsplash.png")
        bg = Label(self.root, image=self.bg).place(x=300, y=0, relwidth=1, relheight=1)
        # left
        self.left = ImageTk.PhotoImage(file="C:\\loginwithdatabase\\space2.png")
        bg = Label(self.root, image=self.left).place(x=0, y=200, width=300, height=168)
        # ===frame===
        frameA = Frame(self.root, bg="khaki1")
        frameA.place(x=0, y=368, width=300, height=400)
        frame0 = Frame(self.root, bg="green")
        frame0.place(x=0, y=0, width=300, height=200)
        self.logo = ImageTk.PhotoImage(file="C:\\Users\\Nisarg Saraiya\\Downloads\\sample logo.png")
        bg = Label(frame0, image=self.logo).place(x=0, y=0, width=300, height=200)
        frame1 = Frame(self.root, bg="black")
        frame1.place(x=480, y=100, width=700, height=400)

        title = Label(frame1, text="LOGIN", font=("times new roman", 20, "bold"), fg="black", bg="orange").place(x=300,
                                                                                                                 y=50)

        lbluname = Label(frame1, text="Username", font=("times new roman", 20, "bold"), fg="black", bg="orange").place(
            x=50, y=150)
        self.u_name = Entry(frame1, text="enter username", font=("times new roman", 20, "bold"))
        self.u_name.place(x=200, y=150)
        lblpass = Label(frame1, text="Password", font=("times new roman", 20, "bold"), fg="black", bg="orange").place(
            x=50, y=250)

        self.password = Entry(frame1, text="enter password", font=("times new roman", 20, "bold"))
        self.password.place(x=200, y=250)
        self.b1 = Button(frame1, text='SUBMIT', font=('normal', 15), command=self.register_data)
        self.b1.place(x=330, y=300)
        url = "https://api.covid19india.org/data.json"
        page = requests.get(url)
        data = json.loads(page.text)
        self.lbl = Label(frameA, text="Total active cases:-" + data["statewise"][0]["active"],
                         font=("times new roman", 15, "bold"), bg="orange", fg="green")
        self.lbl1 = Label(frameA, text="Total confirmed cases:-" + data["statewise"][0]["confirmed"],
                          font=("times new roman", 15, "bold"), bg="orange", fg="red")
        self.lbl.place(x=20, y=120)
        self.lbl1.place(x=20, y=160)
        self.title = Label(frameA, text="COVID - 19", font=("times new roman", 20, "bold"), fg="black",
                           bg="orange").place(x=30, y=30)
        self.lbl = Label(frameA, text="STAY HOME,STAY SAFE",
                         font=("times new roman", 15, "bold"), bg="orange", fg="green")
        self.lbl.place(x=20, y=220)

    def retrieve1(self):
      try:

        ModelName = self.searchTerm1.get()
        selectSQL = """SELECT Modelname,Price,RAM,Internalstorage,Frontcam,Rearcam FROM details WHERE Modelname=%s"""
        cur.execute(selectSQL, (ModelName,))
        myresult = cur.fetchone()
        print(myresult)
        self.Namedata.set(myresult[0])
        self.pricedata.set(myresult[1])
        self.ramdata.set(myresult[2])
        self.ISdata.set(myresult[3])
        self.fcdata.set(myresult[4])
        self.rcdata.set(myresult[5])

        pass

      except Exception as es:
          messagebox.showerror("Error", f"ERROR DUE TO: {str(es)} ", parent=self.root)

    def retrieve2(self):
      try:

        ModelName = self.searchTerm2.get()
        selectSQL = """SELECT Modelname,Price,RAM,Internalstorage,Frontcam,Rearcam FROM details WHERE Modelname=%s"""
        cur.execute(selectSQL, (ModelName,))
        myresult = cur.fetchone()
        print(myresult)
        self.Namedata2.set(myresult[0])
        self.pricedata2.set(myresult[1])
        self.ramdata2.set(myresult[2])
        self.ISdata2.set(myresult[3])
        self.fcdata2.set(myresult[4])
        self.rcdata2.set(myresult[5])

        pass

      except Exception as es:
          messagebox.showerror("Error", f"ERROR DUE TO: {str(es)} ", parent=self.root)

    def register_data(self):
        def register_home(self):
            def check_cbox1(event):
                global p1
                global count
                if   self.priority1.get() == 'LOW PRICE':
                     p1 = self.priority1.get()
                elif self.priority1.get() == 'RAM':
                    p1 = self.priority1.get()

                elif self.priority1.get() == 'INTERNAL STORAGE':
                    p1 = self.priority1.get()

                elif self.priority1.get() == 'GOOD FRONTCAM':
                     p1 = self.priority1.get()
                elif self.priority1.get() == 'GOOD REARCAM':
                    p1 = self.priority1.get()

            def check_cbox2(event):
                global p2
                global count

                if self.priority2.get() == 'LOW PRICE':
                    p2 = self.priority2.get()
                elif self.priority2.get() == 'RAM':
                    p2 = self.priority2.get()

                elif self.priority2.get() == 'INTERNAL STORAGE':
                    p2 = self.priority2.get()

                elif self.priority2.get() == 'GOOD FRONTCAM':
                    p2 = self.priority2.get()

                elif self.priority2.get() == 'GOOD REARCAM':
                    p2 = self.priority2.get()

            def check_cbox3(event):
                global p3
                global count

                if self.priority3.get() == 'LOW PRICE':
                    p3 = self.priority3.get()

                elif self.priority3.get() == 'RAM':
                    p3 = self.priority3.get()

                elif self.priority3.get() == 'INTERNAL STORAGE':
                    p3 = self.priority3.get()
                elif self.priority3.get() == 'GOOD FRONTCAM':
                    p3 = self.priority3.get()
                elif self.priority3.get() == 'GOOD REARCAM':
                    p3 = self.priority3.get()

            def check_cbox4(event):
                global p4
                global count

                if  self.priority4.get() == 'LOW PRICE':
                    p4 = self.priority4.get()

                elif self.priority4.get() == 'RAM':
                    p4 = self.priority4.get()
                elif self.priority4.get() == 'INTERNAL STORAGE':
                    p4 = self.priority4.get()
                elif self.priority4.get() == 'GOOD FRONTCAM':
                    p4 = self.priority4.get()
                elif self.priority4.get() == 'GOOD REARCAM':
                    p4 = self.priority4.get()

            def check_cbox5(event):
                global p5
                global count

                if self.priority5.get() == 'LOW PRICE':
                        p5 = self.priority5.get()
                elif self.priority5.get() == 'RAM':
                        p5 = self.priority5.get()
                elif self.priority5.get() == 'INTERNAL STORAGE':
                        p5 = self.priority5.get()
                elif self.priority5.get() == 'GOOD FRONTCAM':
                        p5 = self.priority5.get()
                elif self.priority5.get() == 'GOOD REARCAM':
                        p5 = self.priority5.get()

            def priority():
                   global count1
                   global count2
                   count1 = 0
                   count2 = 0
                   if p1 == 'LOW PRICE':
                      if self.pricedata.get() <  self.pricedata2.get():
                          count1 = count1 + 4
                      elif self.pricedata.get() >  self.pricedata2.get():
                          count2 = count2 + 4
                   elif p1 == 'RAM':
                       if self.ramdata.get() > self.ramdata2.get():
                           count1 = count1 + 4
                       elif self.ramdata.get() < self.ramdata2.get():
                           count2 = count2 + 4
                   elif p1 == 'INTERNAL STORAGE':
                       if self.ISdata.get() < self.ISdata2.get():
                           count1 = count1 + 4
                       elif self.ISdata.get() > self.ISdata2.get():
                           count2 = count2 + 4
                   elif p1 == 'GOOD FRONTCAM':
                       if self.fcdata.get() < self.fcdata2.get():
                           count1 = count1 + 4
                       elif self.fcdata.get() > self.fcdata2.get():
                           count2 = count2 + 4
                   elif p1 == 'GOOD REARCAM':
                       if self.rcdata.get() < self.rcdata2.get():
                           count1 = count1 + 4
                       elif self.rcdata.get() > self.rcdata2.get():
                           count2 = count2 + 4

                   if p2 == 'LOW PRICE':
                       if self.pricedata.get() < self.pricedata2.get():
                           count1 = count1 + 2
                       elif self.pricedata.get() > self.pricedata2.get():
                           count2 = count2 + 2
                   elif p2 == 'RAM':
                       if self.ramdata.get() > self.ramdata2.get():
                           count1 = count1 + 2
                       elif self.ramdata.get() < self.ramdata2.get():
                           count2 = count2 + 2
                   elif p2 == 'INTERNAL STORAGE':
                       if self.ISdata.get() < self.ISdata2.get():
                           count1 = count1 + 2
                       elif self.ISdata.get() > self.ISdata2.get():
                           count2 = count2 + 2
                   elif p2 == 'GOOD FRONTCAM':
                       if self.fcdata.get() < self.fcdata2.get():
                           count1 = count1 + 2
                       elif self.fcdata.get() > self.fcdata2.get():
                           count2 = count2 + 2
                   elif p2 == 'GOOD REARCAM':
                       if self.rcdata.get() < self.rcdata2.get():
                           count1 = count1 + 2
                       elif self.rcdata.get() > self.rcdata2.get():
                           count2 = count2 + 2
                   if p3 == 'LOW PRICE':
                       if self.pricedata.get() < self.pricedata2.get():
                           count1 = count1 + 2
                       elif self.pricedata.get() > self.pricedata2.get():
                           count2 = count2 + 2
                   elif p3 == 'RAM':
                       if self.ramdata.get() > self.ramdata2.get():
                           count1 = count1 + 2
                       elif self.ramdata.get() < self.ramdata2.get():
                           count2 = count2 + 2
                   elif p3 == 'INTERNAL STORAGE':
                       if self.ISdata.get() < self.ISdata2.get():
                           count1 = count1 + 2
                       elif self.ISdata.get() > self.ISdata2.get():
                           count2 = count2 + 2
                   elif p3 == 'GOOD FRONTCAM':
                       if self.fcdata.get() < self.fcdata2.get():
                           count1 = count1 + 2
                       elif self.fcdata.get() > self.fcdata2.get():
                           count2 = count2 + 2
                   elif p3 == 'GOOD REARCAM':
                       if self.rcdata.get() < self.rcdata2.get():
                           count1 = count1 + 2
                       elif self.rcdata.get() > self.rcdata2.get():
                           count2 = count2 + 2
                   if p4 == 'LOW PRICE':
                       if self.pricedata.get() < self.pricedata2.get():
                           count1 = count1 + 1
                       elif self.pricedata.get() > self.pricedata2.get():
                           count2 = count2 + 1
                   elif p4 == 'RAM':
                       if self.ramdata.get() > self.ramdata2.get():
                           count1 = count1 + 1
                       elif self.ramdata.get() < self.ramdata2.get():
                           count2 = count2 + 1
                   elif p4 == 'INTERNAL STORAGE':
                       if self.ISdata.get() < self.ISdata2.get():
                           count1 = count1 + 1
                       elif self.ISdata.get() > self.ISdata2.get():
                           count2 = count2 + 1
                   elif p4 == 'GOOD FRONTCAM':
                       if self.fcdata.get() < self.fcdata2.get():
                           count1 = count1 + 1
                       elif self.fcdata.get() > self.fcdata2.get():
                           count2 = count2 + 1
                   elif p4 == 'GOOD REARCAM':
                       if self.rcdata.get() < self.rcdata2.get():
                           count1 = count1 + 1
                       elif self.rcdata.get() > self.rcdata2.get():
                           count2 = count2 + 1
                   print(count1)
                   print(count2)
                   if count1 > count2:
                       self.rec.set("PHONE1")
                   else :
                       self.rec.set("PHONE2")

            global frameR
            frame1.destroy()
            frameR = Frame(self.root, bg="black")
            frameR.place(x=0, y=0, relwidth=1, relheight=1)
            self.background_image = ImageTk.PhotoImage(file="C:\\Users\\Nisarg Saraiya\\Downloads\\bg4.png")
            self.background_label = Label(frameR, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.label = Label(frameR, text="AppleCompare.US", font=("Calibri Bold", 60), bg="black",
                               fg="white").place(x=400, y=2)
            framecovid1 = LabelFrame(frameR, width=210, height=400, bg="cadetblue4").place(x=80, y=170)
            framephone1 = LabelFrame(frameR, width=300, height=400, bg="violetred4").place(x=400, y=170)
            framephone2 = LabelFrame(frameR, width=300, height=400, bg="violetred4").place(x=800, y=170)
            plist = ['LOW PRICE', 'RAM', 'INTERNAL STORAGE', 'GOOD FRONTCAM', 'GOOD REARCAM']

            self.priority1 = ttk.Combobox(frameR, width=25,values = plist )
            self.priority1.set("Pick first preference")
            self.priority1.place(x=80,y=100)
            self.priority1.state(['readonly'])
            self.priority1.bind("<<ComboboxSelected>>", check_cbox1)
            self.priority2 = ttk.Combobox(frameR, width=25, values=plist)
            self.priority2.set("Pick second preference")
            self.priority2.place(x=80, y=140)
            self.priority2.state(['readonly'])
            self.priority2.bind("<<ComboboxSelected>>", check_cbox2)
            self.priority3 = ttk.Combobox(frameR, width=25, values=plist)
            self.priority3.set("Pick third preference")
            self.priority3.place(x=400, y=100)
            self.priority3.state(['readonly'])
            self.priority3.bind("<<ComboboxSelected>>", check_cbox3)
            self.priority4 = ttk.Combobox(frameR, width=25, values=plist)
            self.priority4.set("Pick 4th preference")
            self.priority4.place(x=400, y=140)
            self.priority4.state(['readonly'])
            self.priority4.bind("<<ComboboxSelected>>", check_cbox4)
            self.priority5 = ttk.Combobox(frameR, width=25, values=plist)
            self.priority5.set("Pick 5th preference")
            self.priority5.place(x=800, y=100)
            self.priority5.state(['readonly'])
            self.priority5.bind("<<ComboboxSelected>>", check_cbox5)
            self.recommendation = Label(framephone1, textvariable=self.rec, bg='orange',
                                        font=("times new roman", 9, "bold"),
                                        fg='blue', width=10).place(x=800,y=140)

            button = ttk.Button(frameR, text="Recommendation", command=priority)
            button.place(x=980, y=140)

            self.phone1 = Label(frameR, text="PHONE 1:", font=("Calibri Bold", 20), bg="black",
                                fg="white").place(x=480, y=200)
            self.phone2 = Label(frameR, text="PHONE 2:", font=("Calibri Bold", 20), bg="black",
                                fg="white").place(x=880, y=200)

            self.phone1button = Button(frameR, text="Buy").place(x=530, y=520)
            self.phone2button = Button(frameR, text="Buy").place(x=930, y=520)
            self.n1 = Label(framephone1, text="NAME:", font=("times new roman", 9, "bold"), bg="black",
                            fg="white").place(
                x=420, y=400)
            self.pr1 = Label(framephone1, text="PRICE", font=("times new roman", 9, "bold"), bg="orange",
                             fg="white").place(
                x=420, y=420)
            self.ram1 = Label(framephone1, text="RAM:", font=("times new roman", 9, "bold"), bg="pink",
                              fg="white").place(
                x=420, y=440)
            self.IS1 = Label(framephone1, text="INTERNAL STORAGE:", font=("times new roman", 9, "bold"), bg="red",
                             fg="white").place(x=420, y=460)
            self.fc1 = Label(framephone1, text="FRONT CAMERA:", font=("times new roman", 9, "bold"), bg="blue",
                             fg="white").place(x=420, y=480)
            self.bc1 = Label(framephone1, text="REAR CAMERA:", font=("times new roman", 9, "bold"), bg="green",
                             fg="white").place(x=420, y=500)
            nameList = []
            cur.execute("""SELECT modelname FROM details""")
            myresults = cur.fetchall()
            for i in myresults:
                name = i[0]
                nameList.append(name)
            searchOM = OptionMenu(framephone1, self.searchTerm1, *nameList)
            searchOM.place(x=420, y=250)

            self.bt = Button(framephone1, text="Search",command= self.retrieve1).place(x=600, y=250)
            self.namedatalabel = Label(framephone1, textvariable=self.Namedata,  bg='lightblue',font=("times new roman", 9, "bold"),
                                       fg='blue',width = 10)
            self.namedatalabel.place(
                x=600, y=400)
            self.pricedatalabel = Label(framephone1, textvariable=self.pricedata,  bg='lightblue',font=("times new roman", 9, "bold"),
                                   fg='blue',width = 10)
            self.pricedatalabel.place(
                x=600, y=420)
            self.ramdatalabel = Label(framephone1, textvariable=self.ramdata,  bg='lightblue',font=("times new roman", 9, "bold"),
                                      fg='blue',width = 10)
            self.ramdatalabel.place(
                x=600, y=440)
            self.ISdatalabel = Label(framephone1, textvariable=self.ISdata, bg='lightblue',font=("times new roman", 9, "bold"),
                                     fg='blue',width = 10)
            self.ISdatalabel.place(
                x=600, y=460)
            self.fcdatalabel = Label(framephone1, textvariable=self.fcdata,  bg='lightblue',font=("times new roman", 9, "bold"),
                                     fg='blue',width = 10)
            self.fcdatalabel.place(
                x=600, y=480)
            self.bcdatalabel = Label(framephone1, textvariable=self.rcdata,  bg='lightblue',font=("times new roman", 9, "bold"),
                                fg='blue',width = 10)
            self.bcdatalabel.place(
                x=600, y=500)

            searchOM2 = OptionMenu(framephone2, self.searchTerm2, *nameList)
            searchOM2.place(x=820, y=250)

            self.bt = Button(framephone2, text="Search",command= self.retrieve2).place(x=1000, y=250)
            self.namedatalabel = Label(framephone1, textvariable=self.Namedata2,  bg='lightblue',font=("times new roman", 9, "bold"),
                                       fg='blue',width = 10)
            self.namedatalabel.place(
                x=1000, y=400)
            self.pricedatalabel = Label(framephone2, textvariable=self.pricedata2,  bg='lightblue',font=("times new roman", 9, "bold"),
                                   fg='blue',width = 10)
            self.pricedatalabel.place(
                x=1000, y=420)
            self.ramdatalabel = Label(framephone2, textvariable=self.ramdata2,  bg='lightblue',font=("times new roman", 9, "bold"),
                                      fg='blue',width = 10)
            self.ramdatalabel.place(
                x=1000, y=440)
            self.ISdatalabel = Label(framephone2, textvariable=self.ISdata2, bg='lightblue',font=("times new roman", 9, "bold"),
                                     fg='blue',width = 10)
            self.ISdatalabel.place(
                x=1000, y=460)
            self.fcdatalabel = Label(framephone2, textvariable=self.fcdata2,  bg='lightblue',font=("times new roman", 9, "bold"),
                                     fg='blue',width = 10)
            self.fcdatalabel.place(
                x=1000, y=480)
            self.bcdatalabel = Label(framephone2, textvariable=self.rcdata2,  bg='lightblue',font=("times new roman", 9, "bold"),
                                fg='blue',width = 10)
            self.bcdatalabel.place(
                x=1000, y=500)


            self.n2 = Label(framephone1, text="NAME:", font=("times new roman", 9, "bold"), bg="black",
                            fg="white").place(
                x=820, y=400)
            self.pr2 = Label(framephone1, text="PRICE", font=("times new roman", 9, "bold"),
                             bg="orange", fg="white").place(x=820, y=420)
            self.ram2 = Label(framephone1, text="RAM:", font=("times new roman", 9, "bold"), bg="pink",
                              fg="white").place(x=820, y=440)
            self.IS2 = Label(framephone1, text="INTERNAL STORAGE:", font=("times new roman", 9, "bold"),
                             bg="red", fg="white").place(x=820, y=460)
            self.fc2 = Label(framephone1, text="FRONT CAMERA:", font=("times new roman", 9, "bold"),
                             bg="blue", fg="white").place(x=820, y=480)
            self.bc2 = Label(framephone1, text="REAR CAMERA:", font=("times new roman", 9, "bold"),
                             bg="green", fg="white").place(x=820, y=500)

            url = "https://api.covid19india.org/data.json"
            page = requests.get(url)
            data = json.loads(page.text)
            self.lbl = Label(framecovid1, text="Total active cases:-" + data["statewise"][0]["active"],
                             font=("times new roman", 9, "bold"), bg="orange", fg="green")
            self.lbl1 = Label(framecovid1, text="Total confirmed cases:-" + data["statewise"][0]["confirmed"],
                              font=("times new roman", 9, "bold"), bg="orange", fg="red")
            self.lbl.place(x=100, y=300)
            self.lbl1.place(x=100, y=360)
            self.title = Label(framecovid1, text="COVID - 19", font=("times new roman", 20, "bold"), fg="black",
                               bg="orange").place(x=100, y=200)
            self.lbl = Label(framecovid1, text="STAY HOME,STAY SAFE",
                             font=("times new roman", 10, "bold"), bg="orange", fg="green")
            self.lbl.place(x=100, y=420)




        if self.u_name.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "ALL FIELDS ARE REQUIRED", parent=self.root)
        else:
            try:

                cur.execute("")
                cur.execute('select username,password from register')
                total = cur.fetchall()
                username = self.u_name.get()
                password = self.password.get()


                for i in total:
                    if username == i[0] and password == i[1]:
                        return register_home(self)


                    elif username != i[0] and password != i[1]:
                        messagebox.showinfo('ALERT!', 'PASSWORD AND USERNAME ARE ENTERED WRONG')
                        self.u_name.delete(0, END)
                        self.password.delete(0, END)
                        break

                    elif username != i[0] and password == i[1]:
                        messagebox.showinfo('ALERT!', 'ENTER CORRECT USERNAME')
                        self.u_name.delete(0, END)
                        break
                    elif username == i[0] and password != i[1]:
                        messagebox.showinfo('ALERT!', 'ENTER CORRECT PASSWORD')
                        self.password.delete(0, END)
                        break
                    elif username == "" and password != "":
                        messagebox.showinfo('ALERT!', 'ACCOUNT IS NOT REGISTERED')
                        self.u_name.delete(0, END)
                        self.password.delete(0, END)


            except Exception as es:
                messagebox.showerror("Error", f"ERROR DUE TO: {str(es)} ", parent=self.root)


root = Tk()
obj = Register(root)
root.mainloop()


import tkinter
window = tkinter.Tk()
window.title("GUI")

background_image = tkinter.PhotoImage(file = "C:\\Users\\joshy\\Pictures\\bg4.png")
background_label = tkinter.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
label = tkinter.Label(window, text="AppleCompare.US", font=("Calibri Bold",60), bg = "black", fg = "white").place(x = 480, y = 2)

txt = tkinter.Entry(window, width =130).place(x = 398, y = 120)
bt = tkinter.Button(window, text = "Search").place(x= 1137, y = 120)

frame = tkinter.LabelFrame(window, width = 210, height = 400,bg = "cadetblue4").place(x = 80, y = 220)

frame = tkinter.LabelFrame(window, width = 300, height = 400, bg = "violetred4").place(x = 650, y = 220)
b = tkinter.Label(frame, text="Best Option:", font=("Calibri Bold", 20),bg ="black", fg= "white" ).place(x = 730, y = 230)
tkinter.Button(frame, text = "Buy").place(x = 790, y = 580)



window.mainloop()
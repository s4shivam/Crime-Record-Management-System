from tkinter import *
def click():
    text_entry=textentry.get()
    if text_entry == "password" :
        print("Login Approved")
        root.destroy()
        import os
        os.system('front.py')
    else :
        print("Access Denied")
        label1=Label(bottomFrame,text="Wrong Password. Try again",fg="black",bg="red")
        label1.grid(row=1,column=1)


root = Tk()
root.title("Login Window")
root.geometry("620x520+100+00")
root.configure(background = "dark blue")

topFrame = Frame(root,bg="light blue")
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side =BOTTOM)
photo = PhotoImage(file = "dea2.gif")
Label(topFrame ,image = photo).grid(row=1 ,column = 1 ,sticky = W)
label = Label(topFrame, text="CRIMINAL \n RECORD \n DATABASE ",fg="black",bg="light blue",font=(None, 25)).grid(row=1,column = 3,sticky= E)


Label(topFrame, text="Enter Password",fg="black",bg="light blue",font=(None, 15)).grid(row=4,column=3)
textentry = Entry(topFrame , width =30 ,fg="black" ,bg="white",show = "*")
textentry.grid(row=5, column = 3,sticky=W)
Button(topFrame ,text="Submit",width=10 ,command = click).grid(row=6,column=3,sticky=W)

def close():
    exit()
Label(bottomFrame,text="Caution: Information entered incorrectly by an agency \n representaion  in Database will be reflected on the laboratory \n report. NYPD will make corrections requested by the customer at\n any point before the laboratory report is issued.",fg="red",bg="white").grid(row=6 ,column=1,sticky=W)
Button(bottomFrame,text="Click to Exit",width=10,command=close).grid(row = 7,column =1,sticky = S)



root.mainloop()
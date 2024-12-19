from tkinter import *
import tkinter as tk
from tkinter import messagebox
import database

window = tk.Tk()

window.geometry("400x400")
window.title("app")

usernameLable = tk.Label(text="user name")



usernameLable.pack()

entryName = tk.Entry()

entryName.pack()

passwordLable = tk.Label(text="password")

passwordLable.pack()

entryPassword = tk.Entry(window, show="*")

entryPassword.pack()

def saveData():
    if entryPassword.get() == "" or entryName.get() == "" :
        msg = messagebox.showinfo("info", "please enter the value!")

    
    else :
         mydict = {"name": entryName.get(), "password": entryPassword.get()}
         database.mycol.insert_one(mydict)
         msg = messagebox.showinfo("info", "your data been saved in mongodb/mydb/customers!")
    

def editData():
    myquery = { "name": entryName.get(), "password": entryPassword.get()}
    
    mydoc = database.mycol.find_one(myquery)
    
    if mydoc:
        
        # new window
        secondary_window = tk.Toplevel()
        secondary_window.title("Secondary Window")
        secondary_window.geometry("300x200")
        second_passwordLable = tk.Label(secondary_window, text="old password")
        second_passwordLable.pack()
        second_entryPassword = tk.Entry(secondary_window)
        second_entryPassword.pack()
        second_newPasswordLable = tk.Label(secondary_window, text="new password")
        second_newPasswordLable.pack()
        second_entryNewPassword = tk.Entry(secondary_window)
        second_entryNewPassword.pack()
        
        def changeData():
            if second_newPasswordLable != "" and second_entryPassword != "":
                if second_entryPassword.get() == mydoc['password']:
                    database.mycol.update_one({'name': mydoc['name']}, {"$set":{"password":second_entryNewPassword.get()} })
                    msg = messagebox.showinfo('info', "change happend!")
            else:
                    msg = messagebox.showinfo('info', "please enter value!")
                
        button4 = tk.Button(secondary_window,
                text="save change!",
                width=10,
                height=1,
                bg="forest green",
                fg="white", command= changeData
                )
        button4.place(x=109, y=140)
        
    else:
            msg = messagebox.showinfo("info", "wrong value!")

    
    
#delete data    
def deleData():
    if entryPassword.get() == "" or entryName.get() == "" :
        msg = messagebox.showinfo("info", "please enter the value!")
        
    if entryName.get() != "" and entryPassword.get() != "":
         myquery = { "name": entryName.get(), "password": entryPassword.get()}
    
         mydoc = database.mycol.find_one(myquery)
         
         if mydoc:
             database.mycol.delete_one(myquery)
             msgDelete = messagebox.showinfo("info", "one item removed successfully")
         else:
             msgDeleteError = messagebox.showinfo("info", "your item not been found in database!")
    
    
       

button1 = tk.Button(
    text="save it!",
    width=10,
    height=1,
    bg="forest green",
    fg="white", command= saveData
)
button1.place(x=57, y=180)


button2 = tk.Button(
    text="edit it!",
    width=10,
    height=1,
    bg="RoyalBlue1",
    fg="white", command= editData
)
button2.place(x=157, y=180)

button3 = tk.Button(
    text="delete it!",
    width=10,
    height=1,
    bg="red3",
    fg="white", command= deleData
)
button3.place(x=256, y=180)



window.mainloop()
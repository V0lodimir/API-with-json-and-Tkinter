import requests
import json
import tkinter as tk


w = tk.Tk()

w.geometry("500x200")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

lbl_id = tk.Label(master=frm_form, text="Id:")
ent_id = tk.Entry(master=frm_form, width=50)

lbl_id.grid(row=0, column=0)
ent_id.grid(row=0, column=1)
 
lbl_balance = tk.Label(master=frm_form, text="Balance:")
ent_balance = tk.Entry(master=frm_form, width=50)

lbl_balance.grid(row=1, column=0)
ent_balance.grid(row=1, column=1)

new_list = []

def new_balance():
    get_id = ent_id.get()
    get_balance = ent_balance.get()
    setbalance = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={}&balance={}".format(get_id, get_balance)
    requests.get(setbalance)

    url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={}".format(get_id)
    res = requests.get(url)

    json = res.json()
    
    for x in json:
        user_id = x["id"]
        user_name = x["name"]
        user_surname = x["surname"]
        user_email = x["email"]
        user_school_group = x["school_group"]
        user_status = x["status"]
        user_balance = x["balance"]

        if x["id"] is None:
            label.config(text="Error")
        else:
            label.config(text="Id: {}\nName: {}\nSurname: {}\nEmail: {}\nGroup: {}\nStatus: {}\nBalance: {}"
            .format(user_id, user_name, user_surname, user_email, user_school_group, user_status, user_balance))

label = tk.Label(
    text="",
    bg="white", 
    fg="black"
)
label.pack()


frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Push", command=new_balance)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

w.mainloop()
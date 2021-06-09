from tkinter import *
from tkinter import filedialog
from instabot import Bot
import os
import glob

cookie_delete = glob.glob("config/financial_freedom68_uuid_and_cookie.json")
os.remove(cookie_delete[0])

bot = Bot()
root = Tk()
root.geometry('500x500')

label_username = Label(root, text="Username").pack()
username = Entry(root)
username.pack()

label_password = Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

label_caption = Label(root, text="Caption").pack()
caption = Entry(root)
caption.pack()

def fileDialog():
    path = filedialog.askopenfilename()
    bot.login(username=username.get(), password=password.get())
    bot.upload_photo(path, caption=caption.get())

Button(root, text="Choose the image", command=fileDialog).pack()

root.mainloop()

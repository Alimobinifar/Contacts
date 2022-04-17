from tkinter import *
import tkinter
from tkinter import ttk
from turtle import width
from controller import DataBase


class Contact :

    def __init__(self):
        self.root = Tk()
        self.root.title("Contacts")
        self.root.geometry("400x300")
        self.second_ui()
        
    
    def second_ui(self):
        show_btn = Button(self.root,text = "Show Contacts")
        show_btn.place(x=90,y=30)
        y=DataBase()
        data = y.information()
        print(data)
        columns= ("name","family","phone")
        tree = ttk.Treeview(self.root, columns=columns,show="headings")
        tree.column("name",anchor=CENTER, stretch=NO, width=100)
        tree.heading("name", text="name")
        tree.column("family",anchor=CENTER, stretch=NO, width=100)
        tree.heading("family", text="family")
        tree.column("phone",anchor=CENTER, stretch=NO, width=100)
        tree.heading("phone", text="phone")
        tree.place(x=50,y=50,height=200,width=350)
        self.root.mainloop()


x= Contact()
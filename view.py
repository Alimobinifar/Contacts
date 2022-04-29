
from tkinter import *
from tkinter import ttk
from base import Connection
from tkinter import messagebox


class Contact:

    def __init__(self):
        self.root = Tk()
        self.root.title("Contacts")
        self.root.geometry("500x300")
        self.second_ui()
       
    
    def second_ui(self):
         
        columns = ("id","name", "family", "phone")
        tree = ttk.Treeview(self.root, columns=columns,show="headings")
        tree.column("id",anchor=CENTER, stretch=NO, width=100)
        tree.heading("id", text="id")
        tree.column("name",anchor=CENTER, stretch=NO, width=100)
        tree.heading("name", text="name")
        tree.column("family",anchor=CENTER, stretch=NO, width=100)
        tree.heading("family", text="family")
        tree.column("phone",anchor=CENTER, stretch=NO, width=145)
        tree.heading("phone", text="phone")
        tree.place(x=30,y=20,height=200,width=420)

        show_btn = Button(self.root, text="Show Contacts", bg="yellow",\
             command=lambda: self.insert_into_tree(tree))
        show_btn.place(x=30,y=230, height=40, width=100)
        
        add_btn = Button(self.root, text="add Contacts",bg="yellow", \
            command=lambda :AddContact().second_ui())
        add_btn.place(x=150, y=230,height=40, width=100)

        delete_btn = Button(self.root, text="Delete Selected", bg= "yellow", \
            command=lambda:self.delete_contact(tree))
        delete_btn.place(x=270, y=230, height=40, width=100)
        
        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                global contact_id
                contact_id = record[0]
                print(contact_id)
                
        tree.bind("<<TreeviewSelect>>",item_selected)
        

        self.root.mainloop()

    def insert_into_tree(self,tree_name):
        conn_db = Connection()
        data =conn_db.information()
        self.clear_tree(tree_name)
        for i in data:
            tree_name.insert("", "end", values=i)
        return data

    def clear_tree(self,tree_name):
        for i in tree_name.get_children():
                tree_name.delete(i)
    
    def delete_contact(self,tree_name):
        msg = messagebox.askquestion("Be carfull ?", "Do you wanna  Delete Contact ?")
        if msg=="yes":
            App = Connection()
            App.delete_contact(contact_id)
            self.insert_into_tree(tree_name)
            messagebox.showinfo("success", "Deleted Successfully")
        else:
            pass

    

class AddContact:

    def __init__(self):
        self.root = Tk()
        self.root.title("Add Contact")
        self.root.geometry('250x250')

    def add_contact(self, name, family, phone):
        if name and family and phone:
            App = Connection()
            App.register_on_db(name, family, phone)
            messagebox.showinfo("successfull", "registred Successfully")
        else:
            messagebox.showerror("Error", "please fill all required fields")

    def second_ui(self):
        name_entry = Entry(self.root, font=("arial", 15, "bold"))
        name_entry.place(x=90, y=10, height=30, width=150)
        name_lbl = Label(self.root, text="Name : ")
        name_lbl.place(x=10, y=15)

        family_entry = Entry(self.root, font=("arial", 15, "bold"))
        family_entry.place(x=90, y=65, height=30, width=150)
        family_lbl = Label(self.root, text="Family : ")
        family_lbl.place(x=10, y=65)

        phone_entry = Entry(self.root, font=("arial", 15, "bold"))
        phone_entry.place(x=90, y=115, height=30, width=150)
        phone_lbl = Label(self.root, text="Phone : ")
        phone_lbl.place(x=10, y=120)

             
        register_btn = Button(self.root, text="Add Contact", bg="yellow",\
             command=lambda:self.add_contact(name_entry.get(), family_entry.get(), phone_entry.get()))
        register_btn.place(x=60, y=165, height=40, width=100)
        

        self.root.mainloop()


if __name__ == "__main__":
    App = Contact()

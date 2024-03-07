import sqlite3
from tkinter import *
from tkinter import messagebox

def create_table():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                     (name TEXT, phone_number TEXT, email TEXT)''')
    conn.commit()
    conn.close()

def add_contact():
    name = name_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()

    if not name or not phone_number or not email:
        messagebox.showerror('Error', 'Please enter all fields')
        return

    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts VALUES (?, ?, ?)", (name, phone_number, email))
    conn.commit()
    conn.close()

    name_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    email_entry.delete(0, END)

    messagebox.showinfo('Success', 'Contact added successfully')

def view_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    if not rows:
        messagebox.showinfo('No Contacts', 'No contacts to display')
        return

    result = ''
    for row in rows:
        result += f'Name: {row[0]}\nPhone Number: {row[1]}\nEmail: {row[2]}\n\n'

    messagebox.showinfo('Contacts', result)

app = Tk()
app.title('Contact Book')

name_label = Label(app, text='Name')
name_label.grid(row=0, column=0)

name_entry = Entry(app)
name_entry.grid(row=0, column=1)

phone_number_label = Label(app, text='Phone Number')
phone_number_label.grid(row=1, column=0)

phone_number_entry = Entry(app)
phone_number_entry.grid(row=1, column=1)

email_label = Label(app, text='Email')
email_label.grid(row=2, column=0)

email_entry = Entry(app)
email_entry.grid(row=2, column=1)

add_button = Button(app, text='Add Contact', command=add_contact)
add_button.grid(row=3, column=0, pady=10)

view_button = Button(app, text='View Contacts', command=view_contacts)
view_button.grid(row=3, column=1, pady=10)

create_table()

app.mainloop()
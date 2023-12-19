# Importing required packages
import sys
import pandas as pd
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import tkinter as tk

# Recalling updated data in code blocks
def data():
    df = pd.read_csv("Flights.csv")
    return df

# Function for available flights based on user input
def get_data():
    for item in tree.get_children():
        tree.delete(item)
    # type conversion
    x=str(val2.get()).title()
    y=str(val3.get()).title()
    df=data()
    z=df.loc[(df['Source'] == x)&(df['Destination']==y)]
    if z.empty == False:
        a=z[['Flight ID','Airline','Seats Available']]
        for x in range(len(a.index.values)): # use for loop to get values in each line, _ is the number of lines.
            tree.insert('',tk.END,value=tuple(a.iloc[x].values))
    else:
        for item in tree.get_children():
            tree.delete(item)
        messagebox.showinfo("Information!!!", "No Flights are available.")

# Resetting text fields of the Available Flights 
def reset_sd():
    val2.set("")
    val3.set("")
    for item in tree.get_children():
        tree.delete(item)

# Checking Flight ID to add or update data
def check_id():
    df=data()
    z=df.loc[df['Flight ID'] == int(val1.get())]

    if z.empty == False:
        modify_yn()
    else:
        add_data()

#Updating data function
def modify_yn():
    response = messagebox.askokcancel("Modify Flight Data", "Are you sure you want to modify existing data?")
    if response == True:
        # code that performs deletion
        ttk.Label(tab2, text ="Source :").grid(column = 0,row = 2, padx = 5, pady = 5)
        ttk.Entry(tab2, textvariable=val6).grid(column = 1, row = 2,padx = 10,pady = 10)
        
        ttk.Label(tab2, text="Destination :").grid(column = 0,row = 3, padx = 5, pady = 5)
        ttk.Entry(tab2, textvariable=val7).grid(column = 1, row = 3,padx = 10,pady = 10)

        ttk.Label(tab2, text ="Airline Type :").grid(column = 0,row = 4, padx = 5, pady = 5)
        ttk.Entry(tab2, textvariable=val4).grid(column = 1, row = 4,padx = 10,pady = 10)

        ttk.Label(tab2, text="Available Seats :").grid(column = 0,row = 5, padx = 5, pady = 5)
        ttk.Entry(tab2, textvariable=val5).grid(column = 1, row = 5,padx = 10,pady = 10)
       
        ttk.Button(tab2, text="Update Data",command=save_data).grid(column = 0,row = 6, padx = 15, pady = 15)
    else:
        val1.set("")

# Saving the updated data to the CSV File
def save_data():
    df=data()
    #df.loc[df['Flight ID'] == 1] = 1,"United",290,"Chicago","Boston"
    df.loc[df['Flight ID'] == int(val1.get())] = int(val1.get()),val4.get(),int(val5.get()),val6.get(),val7.get()
    df.to_csv("Flights.csv",index=False)
    messagebox.showinfo("Successful!", "Data is updated.")

# Adding new flight data
def add_data():
    response = messagebox.askokcancel("Add Data", "Are you sure you want to add data?")
    if response == True:
        # Code that performs deletion
        ttk.Label(tab2, text ="Source :").grid(column = 0,row = 2, padx = 5, pady = 5)
        ttk.Entry(tab2, textvariable=val6).grid(column = 1, row = 2,padx = 10,pady = 10)
        
        ttk.Label(tab2, text="Destination :").grid(column = 0,row = 3, padx = 5, pady = 5)
        ttk.Entry(tab2, textvariable=val7).grid(column = 1, row = 3,padx = 10,pady = 10)
        
        ttk.Label(tab2, text ="Airline Type :").grid(column = 0,row = 4, padx = 5, pady = 5)
        ttk.Entry(tab2, textvariable=val4).grid(column = 1, row = 4,padx = 10,pady = 10)

        ttk.Label(tab2, text="Available Seats :").grid(column = 0,row = 5, padx = 5, pady = 5)
        ttk.Entry(tab2, textvariable=val5).grid(column = 1, row = 5,padx = 10,pady = 10)
        
        ttk.Button(tab2, text="Add Data",command=add_row).grid(column = 0,row = 6, padx = 15, pady = 15)
        ttk.Button(tab2, text="Reset",command=reset_col).grid(column = 1,row = 6, padx = 10, pady = 10)
        
        
        
    else:
        val1.set("")

# Adding data to CSV File
def add_row():
    df=data()
    x={"Flight ID":int(val1.get()),"Airline":val4.get(),"Seats Available":int(val5.get()),"Source":val6.get(),"Destination":val7.get()}
    #x={"Flight ID":9,"Airline":2,"Seats Available":3,"Source":3,"Destination":4}
    df2=df.append(x,ignore_index=True)
    df2.to_csv("Flights.csv",index=False)
    messagebox.showinfo("Information!", "Flight data added successfully.")

# Resetting all fields
def reset_flightid():
    val1.set("")
    val6.set("")
    val7.set("")
    val4.set("")
    val5.set("")

# Main Function
def start_gui():
    global root
    df=data()
    root = Tk()
    tabControl = ttk.Notebook(root)
    root.iconbitmap("flight_img.ico")
    root.title("Flight Information Application")
    root.geometry("680x450")

    # style configuration
    style = ttk.Style(root)
    style.configure('TLabel', background='#9f99c4', font=('Times New Roman', 13, 'bold'), foreground = '#5d656e')
    style.configure('TFrame', background='#9f99c4')
    style.configure('TButton', font=('Times New Roman', 10, 'bold'), foreground = '#5d656e', background='#7b6e91',  relief='RAISED')

    style.map('TButton', foreground=[('active', '!disabled', '#9eb55b')], background=[('active', 'black')])

    global tab1,tab2
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Available Flights')
    tabControl.add(tab2, text='Alter Flight Data')
    tabControl.pack(expand=1, fill="both")

    global val1,val2,val3,val4,val5,val6,val7
    val1 = StringVar()
    val2 = StringVar()
    val3 = StringVar()
    val4 = StringVar()
    val5 = StringVar()
    val6 = StringVar()
    val7 = StringVar()

    # For Available Flights
    ttk.Label(tab1, text ="Source :").grid(column=0, row=0, padx=5, pady=5)
    ttk.Entry(tab1, textvariable=val2).grid(column=1, row=0, padx=10, pady=10)

    ttk.Label(tab1, text="Destination :").grid(column=0, row=1, padx=5, pady=5)
    ttk.Entry(tab1, textvariable=val3).grid(column=1, row=1, padx=10, pady=10)

    ttk.Button(tab1, text="Get Data",command=get_data).grid(column=0, row=2, padx=15, pady=15)
    ttk.Button(tab1, text="Reset S|D",command=reset_sd).grid(column=1, row=2, padx=15, pady=15)

    columns=['one','two','three']
    global tree
    tree=ttk.Treeview(tab1, columns=columns, show='headings', height=3)
    tree.heading("one", text="FlightID")
    tree.heading("two", text="Airline Type")
    tree.heading("three", text="Available Seats")
    tree.column("one", width=100, anchor=CENTER)
    tree.column("two", width=200, anchor=CENTER)
    tree.column("three", width=100, anchor=CENTER)
    tree.grid(row=7, column=1, columnspan=2)


    # For Altering Flight Data

    ttk.Label(tab2, text ="Enter Flight ID :").grid(column=0, row=0, padx=10, pady = 10)
    ttk.Entry(tab2, textvariable=val1).grid(column=1, row=0, padx=10, pady=10)

    ttk.Label(tab2, text="Check the Database").grid(column=0, row=1, padx=10, pady=10)
    ttk.Button(tab2, text="Check",command=check_id).grid(column=1,row=1, padx=10, pady=10)
    ttk.Button(tab2, text="Reset",command=reset_flightid).grid(column=1, row=7, padx=15, pady=15)
    ttk.Button(tab2, text="Restart",command=refresh).grid(column=2, row=7, padx=15, pady=15)

    root.mainloop()
    
if __name__ == "__main__":
    def refresh():
        root.destroy()
        start_gui()
    start_gui()


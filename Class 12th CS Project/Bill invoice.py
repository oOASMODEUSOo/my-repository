# Importing the modules and intialising the stuff

from tkinter import *
import mysql.connector
from datetime import datetime
import tkinter.messagebox as tkmessage
from tkinter import ttk

master = Tk()
# master.iconbitmap("store.ico")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testinghy"
)

master.geometry("500x300")
master.minsize(300, 300)
master.title("bill invoice")


# defining global functions

# This happens when i click new bill----------------------------------------------------------------------------------

def new_bill():
    # print("generating new bill")
    newbill = Tk()
    newbill.title("New Bill")
    newbill.geometry("850x700")
    newbill.maxsize(850, 700)
    # newbill.iconbitmap("store.ico")

    #mycur=mydb.cursor()
    #create=f"CREATE TABLE {Customer_name}(Item CHAR(30) PRIMARY KEY,Price INT, Quantity INT)"
    #print(create)
    #mycur.execute(create)


    # def under func under
    def add():
        # sql commands and treeview commands togo

        mycursor = mydb.cursor()
        mycursor.execute("show tables")

        itemval.delete(0, 'end')
        priceval.delete(0, 'end')
        quantityval.delete(0, 'end')

    def remove():
        pass
        '''
        #psedo sql command:

        '''

    def total():
        tkmessage.showinfo("Total", "Total amount is: ")

    def exit():
        newbill.destroy()

    upper_frame = Frame(newbill, bg="skyblue", borderwidth=3, relief="raised")
    upper_frame.pack(fill=X)
    title = Label(upper_frame, text=f"Bill Generated at {datetime.now()}", fg="orange", font="goldman 19 bold")
    title.pack()

    lower_frame = Frame(newbill, bg="skyblue", borderwidth=3, relief="raised")
    lower_frame.pack(side="bottom", anchor="s", fill=X)

    bu3_total = Button(lower_frame, text="Total Amount", bg="grey", font="11", relief="raised", command=total)
    bu3_total.grid(row=1, column=5, ipadx=164)
    bu4_exit = Button(lower_frame, text="Close Bill", bg="grey", font="11", relief="raised", command=exit)
    bu4_exit.grid(row=1, column=6, ipadx=165)

    left_frame = Frame(newbill, bg="orange", borderwidth=4, relief="ridge")
    left_frame.place(x=615, y=43, width=234, height=620)
    item_label = Label(left_frame, text="Item", font="15")
    item_label.place(x=20, y=200, width=60, height=20)
    price_label = Label(left_frame, text="Price", font="15")
    price_label.place(x=20, y=230, width=60, height=20)
    quantity_label = Label(left_frame, text="Quantity", font="15")
    quantity_label.place(x=20, y=260, width=60, height=20)
    bu1_add = Button(left_frame, text="Add To List", bg="lightgrey", font="11", relief="raised", command=add)
    bu2_remove = Button(left_frame, text="Remove", bg="lightgrey", font="11", relief="raised", command=remove)
    bu1_add.place(x=60, y=300, width=100, height=20)
    bu2_remove.place(x=60, y=330, width=100, height=20)

    # treeview data--------------------------------------------------------------------------------------------------

    right_frame = Frame(newbill, bg="cyan", borderwidth=1, relief="ridge")
    right_frame.pack(side="left", anchor="nw")

    tree_scroll = Scrollbar(right_frame)
    tree_scroll.pack(side="right", fill=Y)

    my_tree = ttk.Treeview(right_frame, yscrollcommand=tree_scroll.set)
    my_tree.pack(fill=Y, ipady=200)

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ("Item", "Price", "Quantity", "T. Price")

    my_tree.column("#0", width=0, stretch=0)
    my_tree.column("Item", anchor="w", width=200)
    my_tree.column("Price", anchor="w", width=120)
    my_tree.column("Quantity", anchor="center", width=120)
    my_tree.column("T. Price", anchor="w", width=152)

    my_tree.heading("#0", text="", anchor="w")
    my_tree.heading("Item", text="Item", anchor="w")
    my_tree.heading("Price", text="Price", anchor="w")
    my_tree.heading("Quantity", text="Quantity", anchor="center")
    my_tree.heading("T. Price", text="Total Price", anchor="w")

    # Enrty of the values--------------------------------------------------------------------------------------------

    item_entry = StringVar()
    price_entry = IntVar()
    quantity_entry = IntVar()

    itemval = Entry(left_frame, textvariable=item_entry)
    priceval = Entry(left_frame, textvariable=price_entry)
    quantityval = Entry(left_frame, textvariable=quantity_entry)

    itemval.place(x=90, y=200, width=110, height=20)
    priceval.place(x=90, y=230, width=110, height=20)
    quantityval.place(x=90, y=260, width=110, height=20)

    # Enrty of the values--------------------------------------------------------------------------------------------

    newbill.mainloop()


# This happens when i click new bill----------------------------------------------------------------------------------

# This happens when i click Remove Previous Bills---------------------------------------------------------------------

def remove():
    # print("")
    def del_tables():
        tkmessage.showinfo("Alert", "All The Previous Bills Have Been Removed")
        remove_window.destroy()

        mycursor = mydb.cursor()

        mycursor.execute("SHOW TABLES")
        result=mycursor.fetchall()

        for x in result:
            sql=f"DROP TABLE {x[0]};"    #if sql doesnt accept f string then what u can do is make variable and pass that variablle in execute command
            #print(sql)

            mycursor.execute(sql)


    remove_window = Tk()
    remove_window.geometry("360x200")
    remove_window.minsize(380, 200)
    remove_window.maxsize(380, 200)
    # remove_window.iconbitmap("store.ico")

    frame_remove_bill = Frame(remove_window, bg="cyan", borderwidth=4, relief="ridge")
    frame_remove_bill.pack(fill=X)
    label_del = Label(frame_remove_bill, text="Are You Sure You Want To\nRemove All Previous Bills?", font="goldman 20")
    label_del.pack()
    Button(remove_window, text="YES", relief="raised", font="goldman 15", command=del_tables).pack()

    def del_tables():
        tkmessage.showinfo("Alert", "All The Previous Bills Have Been Removed")
        remove_window.destroy()


    remove_window.mainloop()


# This happens when i click Remove Previous Bills---------------------------------------------------------------------

# This happens when i click LogOff------------------------------------------------------------------------------------

def LogOff():
    master.destroy()


# This happens when i click LogOff------------------------------------------------------------------------------------


# starter window------------------------------------------------------------------------------------------------------

frame = Frame(master, bg="yellow", borderwidth=3, relief="raised")
frame.pack(fill=BOTH, anchor="c")
Label(frame, text="Exit Counter Bill Manager", fg="blue", relief="sunken", font="goldman 19 bold").pack()

frame_for_add = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_add.pack(anchor="center", pady=20)
b1_add = Button(frame_for_add, text="New Bill", command=new_bill)
b1_add.pack(anchor="center")

frame_for_remove = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_remove.pack(anchor="center", pady=20)
b2_remove = Button(frame_for_remove, text="Remove Previous Bills", command=remove)
b2_remove.pack(anchor="center")

frame_for_quit = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_quit.pack(anchor="center", pady=10)
b3_quit = Button(frame_for_quit, text="Log Off", command=LogOff)
b3_quit.pack()

master.mainloop()

# starter window-----------------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import pymysql
from datetime import datetime
from config import *

class bank():
    def __init__(self,root):
        self.root = root
        self.root.title("Bank Management")

        scrn_width = self.root.winfo_screenwidth()
        scrn_height = self.root.winfo_screenheight()

        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")

        mainLabel = tk.Label(self.root, text="Bank Account Management System", font=("Arial",40,"bold"), bg="light green", bd=5, relief="groove")
        mainLabel.pack(side="top",fill="x")

        maninFrame = tk.Frame(self.root, bg="light gray", bd=5, relief="ridge")
        maninFrame.place(x=500, y=100, width=450, height=550)

        openAcBtn = tk.Button(maninFrame, command= self.openAc, width=20, text="Open Account", bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        openAcBtn.grid(row=0, column=0, padx=40, pady=40)

        depBtn = tk.Button(maninFrame, command=self.deposit,width=20, text="Deposit", bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        depBtn.grid(row=1, column=0, padx=40, pady=40)

        wdBtn = tk.Button(maninFrame, command=self.wd, width=20, text="Withdraw", bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        wdBtn.grid(row=2, column=0, padx=40, pady=40)

        stmtBtn = tk.Button(maninFrame, command=self.show_stmt, width=20, text="Balance & Mini-Statement", bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        stmtBtn.grid(row=3, column=0, padx=40, pady=40)


    def openAc(self):
        self.openAcFrame = tk.Frame(self.root, bg="light gray", bd=5, relief="ridge")
        self.openAcFrame.place(x=500, y=100, width=450, height=550)

        uNameLabel = tk.Label(self.openAcFrame, text="User Name:", bg="light gray",font=("Arial", 15, "bold"))
        uNameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.uNameIn = tk.Entry(self.openAcFrame, width=15, font=("Arial", 15))
        self.uNameIn.grid(row=0, column=1, padx=5, pady=30)

        uPWLabel = tk.Label(self.openAcFrame, text="Enter Password:", bg="light gray",font=("Arial", 15, "bold"))
        uPWLabel.grid(row=1, column=0, padx=20, pady=30)
        self.uPWIn = tk.Entry(self.openAcFrame, width=15, font=("Arial", 15),show="*")
        self.uPWIn.grid(row=1, column=1, padx=5, pady=30)

        confirmLabel = tk.Label(self.openAcFrame, text="Confirm Password:", bg="light gray",font=("Arial", 15, "bold"))
        confirmLabel.grid(row=2, column=0, padx=20, pady=30)
        self.confirmIn = tk.Entry(self.openAcFrame, width=15, font=("Arial", 15),show="*")
        self.confirmIn.grid(row=2, column=1, padx=5, pady=30)
        
        self.show_pass = tk.IntVar()
        show_check = tk.Checkbutton(self.openAcFrame, text="Show Password",bg="light gray", font=("Arial", 12),variable=self.show_pass, command=self.toggle_pass)
        show_check.grid(row=3, column=1, sticky="w")

        okBtn = tk.Button(self.openAcFrame, command=self.insert, text="Ok", width=10, bg = "light Blue", bd=3, relief="raised", font=("Arial", 15, "bold"))
        okBtn.grid(row=4, column=0, padx=40, pady=120)

        closeBtn = tk.Button(self.openAcFrame, command=self.close_openAc, text="Close", width=10, bg = "light Blue", bd=3, relief="raised", font=("Arial", 15, "bold"))
        closeBtn.grid(row=4, column=1, padx=40, pady=120)

    def toggle_pass(self):
        if self.show_pass.get() == 1:
            self.uPWIn.config(show="")
            self.confirmIn.config(show="")
        else:
            self.uPWIn.config(show="*")
            self.confirmIn.config(show="*")

    def close_openAc(self):
        self.openAcFrame.destroy()

    def insert(self):
        uName = self.uNameIn.get()
        uPW = self.uPWIn.get()
        confirm = self.confirmIn.get()

        if uPW == confirm:
            con = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
            cur = con.cursor()
            cur.execute("Insert into account(userName, userPW) values(%s, %s)",(uName,uPW))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","Account Opened Successfully!")
            self.clear()
        else:
            tk.messagebox.showerror("Error","Passwords are not same!")
            self.clear()

    def clear(self):
        self.uNameIn.delete(0,tk.END)
        self.uPWIn.delete(0,tk.END)
        self.confirmIn.delete(0,tk.END)

    def deposit(self):
        self.depFrame = tk.Frame(self.root, bg="light gray", bd=5, relief="ridge")
        self.depFrame.place(x=500, y=100, width=450, height=550)

        NameLabel = tk.Label(self.depFrame, text="User Name:", bg="light gray",font=("Arial", 15, "bold"))
        NameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.NameIn = tk.Entry(self.depFrame, width=15, font=("Arial", 15))
        self.NameIn.grid(row=0, column=1, padx=5, pady=30)

        amountLabel = tk.Label(self.depFrame, text="Enter Amount:", bg="light gray",font=("Arial", 15, "bold"))
        amountLabel.grid(row=1, column=0, padx=20, pady=30)
        self.amountIn = tk.Entry(self.depFrame, width=15, font=("Arial", 15))
        self.amountIn.grid(row=1, column=1, padx=5, pady=30)

        okBtn = tk.Button(self.depFrame, command=self.deposit_fun, text="Deposit", width=10, bg = "light Blue", bd=3, relief="raised", font=("Arial", 15, "bold"))
        okBtn.grid(row=2, column=0, padx=40, pady=150)

        closeBtn = tk.Button(self.depFrame, command=self.close_deposit, text="Close", width=10, bg = "light Blue", bd=3, relief="raised", font=("Arial", 15, "bold"))
        closeBtn.grid(row=2, column=1, padx=40, pady=150)

    def deposit_fun(self):
        name = self.NameIn.get()
        amount = int(self.amountIn.get())
        con = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cur = con.cursor()
        cur.execute("select balance from account where userName=%s", (name,))
        data = cur.fetchone()
        if data:
            balance = data[0]
            if data[0] is None:
                balance=0
            update = balance +amount
            cur.execute("update account set balance=%s where userName=%s",(update,name))
            cur.execute("insert into transactions(userName, type, amount) values(%s, %s, %s)",(name,"Deposit",amount))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","Amount deposited Successfully!")
            self.clear_dep()
        else:
            tk.messagebox.showerror("Error","Invalid customer name!")
            self.clear_dep()
        
    def close_deposit(self):
        self.depFrame.destroy()

    def clear_dep(self):
        self.NameIn.delete(0,tk.END)
        self.amountIn.delete(0,tk.END)

    def wd(self):
        self.wdFrame = tk.Frame(self.root, bg="light gray", bd=5, relief="ridge")
        self.wdFrame.place(x=500, y=100, width=450, height=550)

        wNameLabel = tk.Label(self.wdFrame, text="User Name:", bg="light gray",font=("Arial", 15, "bold"))
        wNameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.wNameIn = tk.Entry(self.wdFrame, width=15, font=("Arial", 15))
        self.wNameIn.grid(row=0, column=1, padx=5, pady=30)

        wPWLabel = tk.Label(self.wdFrame, text="Enter Password:", bg="light gray",font=("Arial", 15, "bold"))
        wPWLabel.grid(row=1, column=0, padx=20, pady=30)
        self.wPWIn = tk.Entry(self.wdFrame, width=15, font=("Arial", 15),show="*")
        self.wPWIn.grid(row=1, column=1, padx=5, pady=30)

        self.show_wpass = tk.IntVar()
        wshow_check = tk.Checkbutton(self.wdFrame, text="Show Password",bg="light gray", font=("Arial", 12),variable=self.show_wpass, command=self.toggle_wpass)
        wshow_check.grid(row=2, column=1, sticky="w")


        wdLabel = tk.Label(self.wdFrame, text="Enter Amount:", bg="light gray",font=("Arial", 15, "bold"))
        wdLabel.grid(row=3, column=0, padx=20, pady=30)
        self.wdIn = tk.Entry(self.wdFrame, width=15, font=("Arial", 15))
        self.wdIn.grid(row=3, column=1, padx=5, pady=30)

        okBtn = tk.Button(self.wdFrame, command=self.wd_fun, text="Withdraw", width=10, bg = "light Blue", bd=3, relief="raised", font=("Arial", 15, "bold"))
        okBtn.grid(row=4, column=0, padx=40, pady=120)

        closeBtn = tk.Button(self.wdFrame, command=self.close_wd, text="Close", width=10, bg = "light Blue", bd=3, relief="raised", font=("Arial", 15, "bold"))
        closeBtn.grid(row=4, column=1, padx=40, pady=120)

    def wd_fun(self):
        name = self.wNameIn.get()
        pw = self.wPWIn.get()
        amount = int(self.wdIn.get())
        con = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cur = con.cursor()
        cur.execute("select userPW, balance from account where userName=%s",name)
        data = cur.fetchone()
        if data:
            if data[0]==pw:
                if data[1]>=amount:
                    update = data[1] - amount
                    cur.execute("update account set balance=%s where userName=%s",(update,name))
                    cur.execute("insert into transactions(userName, type, amount) values(%s, %s, %s)",(name,"Withdraw",amount))
                    con.commit()
                    con.close()
                    tk.messagebox.showinfo("Success","Amount withdrew Successfully!")
                    self.clear_wd()
                else:
                    tk.messagebox.showerror("Error","Insufficient balance!")
                    con.close()
                    self.clear_wd()
            else:
                tk.messagebox.showerror("Error","Invalid customer password!")
                con.close()
                self.clear_wd()
        else:
            tk.messagebox.showerror("Error","Invalid customer name!")
            con.close()
            self.clear_wd()
    def toggle_wpass(self):
        if self.show_wpass.get() == 1:
            self.wPWIn.config(show="")
        else:
            self.wPWIn.config(show="*")

    def close_wd(self):
        self.wdFrame.destroy()

    def clear_wd(self):
        self.wNameIn.delete(0,tk.END)
        self.wPWIn.delete(0,tk.END)
        self.wdIn.delete(0,tk.END)

    def show_stmt(self):
        self.stmtFrame = tk.Frame(self.root, bg="light gray", bd=5, relief="ridge")
        self.stmtFrame.place(x=500, y=100, width=450, height=550)

        uLabel = tk.Label(self.stmtFrame, text="User Name:", bg="light gray", font=("Arial", 15, "bold"))
        uLabel.grid(row=0, column=0, padx=20, pady=30)

        self.stmtUser = tk.Entry(self.stmtFrame, width=15, font=("Arial", 15))
        self.stmtUser.grid(row=0, column=1, padx=5, pady=30)

        okBtn = tk.Button(self.stmtFrame, command=self.get_stmt, text="Show", width=10, bg="light blue", font=("Arial", 15, "bold"))
        okBtn.grid(row=1, column=0, padx=40, pady=30)

        closeBtn = tk.Button(self.stmtFrame, command=self.close_stmt, text="Close", width=10, bg="light blue", font=("Arial", 15, "bold"))
        closeBtn.grid(row=1, column=1, padx=40, pady=30)

        self.output = tk.Text(self.stmtFrame, width=40, height=15, font=("Arial", 12))
        self.output.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

    def get_stmt(self):
        name = self.stmtUser.get()

        con = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cur = con.cursor()

        cur.execute("select balance from account where userName=%s", (name,))
        acc = cur.fetchone()

        if not acc:
            tk.messagebox.showerror("Error", "Invalid User Name!")
            return

        balance = acc[0]

        cur.execute("select type, amount, datetime from transactions where userName=%s order by id desc limit 10", (name,))
        rows = cur.fetchall()

        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"Current Balance: ₹{balance}\n")
        self.output.insert(tk.END, "\nRecent Transactions:\n")
        self.output.insert(tk.END, "-"*40 + "\n")

        for r in rows:
            raw_dt = r[2]
            dt_12 = datetime.strptime(str(raw_dt), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S %p")
            self.output.insert(tk.END, f"{dt_12} - {r[0]} - ₹{r[1]}\n")
        con.close()

    def close_stmt(self):
        self.stmtFrame.destroy()

root = tk.Tk()
obj = bank(root)
root.mainloop()
"""
Created on 24.08.2021.

@author: ljmarjanovic
"""
import stt_lib as stt
import kontrole_lib as kon

# import calendar
import datetime
from datetime import date

import tkinter as tk
# from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar


# main for function call.
if __name__ == "__main__":
    # create main window
    root = tk.Tk()
    root.geometry('550x400')
    root.minsize(550, 400)
    root.title("Logistika STT Izvestaj")


    def _quit():
        root.quit()
        root.destroy()
        exit()


    def _msgBox():
        # messagebox.showinfo('Python message info box', 'O pitonu')
        # messagebox.showwarning('Python message info box', 'O pitonu')
        # messagebox.showerror('Python message info box', 'O pitonu')
        # messagebox.askyesno("Python message dual choice box", "Are you sure?")
        messagebox.showinfo('STT Aplikacija', 'STT izvestaj za logistiku 2021')

    def nadjiSLV():
        kon.findSLV(SLVFile, slv)


    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 3 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # meni definicija
    # menuBar = Menu(root)
    menuBar = tk.Menu(root)

    root.config(menu=menuBar)

    fileMenu = tk.Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=_quit)
    menuBar.add_cascade(label="File", menu=fileMenu)

    helpMenu = tk.Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="O programu", command=_msgBox)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    SLV = ""
    danas = date.today()
    poslednjidan = danas.strftime("%d.%m.%Y")

    prvi = datetime.datetime(danas.year, danas.month, 1)
    prvidan = prvi.strftime("%d.%m.%Y")

    SLVFile = tk.StringVar()
    cs = tk.StringVar()
    paid = tk.StringVar()
    InfoText = tk.StringVar()

    Mesec = tk.StringVar(root, value=str(danas.month))
    Godina = tk.StringVar(root, value=str(danas.year))

    OdDatuma = tk.StringVar(root, value=prvidan)
    DoDatuma = tk.StringVar(root, value=poslednjidan)
    cc = tk.StringVar(root, value="4")


    def generateSTT():
        d1 = kon.checkDate(OdDatuma.get())
        if d1 != 1:
            datum_od.focus_set()

        d2 = kon.checkDate(DoDatuma.get())
        if d2 != 1:
            datum_do.focus_set()

        f1 = kon.checkField(cs.get(), 1)
        f1 = kon.checkField(cc.get(), 2)
        f1 = kon.checkField(paid.get(), 3)
        f1 = kon.checkField(slv.get(), 4)

        if f1 == 1:
            cc.focus_set()
        elif f1 == 2:
            cs.focus_set()
        elif f1 == 3:
            paid.focus_set()
        elif f1 == 4:
            slv.focus_set()
        elif f1 == 0:
            slv_ok = stt.checkSLV(slv.get())
            if slv_ok == 1:
                messagebox.showwarning('Greska u SLV fajlu', 'Nije ispravan SLV fajl!')
                f1 = 4
                slv.focus_set()

        # if (d1 == 1) and (d2 == 1) and (c1 == 1) and (c2 == 1) and (p1 == 1) and (s1 == 1):
        # if (d1 == 1) and (d2 == 1) and (f1 == 1):
        if (d1 == 1) and (d2 == 1) and (f1 == 0):
            stt.generateExcel(DoDatuma.get(), slv.get(), cs.get(), cc.get(), paid.get(), textInfo, bar)
            textInfo.delete(0, tk.END)
            textInfo.insert(0, "Gotov Izvestaj")
            textInfo.update()
            messagebox.showinfo('STT', 'Gotov Izvestaj!')


    # odavde ide forma
    lblMesec = tk.Label(root, text="Mesec", width=10, font=("bold", 10), anchor="w")
    lblMesec.place(x=10, y=30)

    mesec = tk.Entry(root, textvar=Mesec)
    mesec.place(x=100, y=30)

    lblGodina = tk.Label(root, text="Godina", width=10, font=("bold", 10), anchor="w")
    lblGodina.place(x=280, y=30)

    godina = tk.Entry(root, textvar=Godina)
    godina.place(x=400, y=30)

    lblPeriod = tk.Label(root, text="Period Izvestaja", width=20, font=("bold", 10), fg='blue', anchor="w")
    lblPeriod.place(x=10, y=70)

    lblOdDatuma = tk.Label(root, text="Od datuma", width=10, font=("bold", 10), anchor="w")
    lblOdDatuma.place(x=10, y=110)

    datum_od = tk.Entry(root, textvar=OdDatuma)
    datum_od.place(x=100, y=110)

    lblDoDatuma = tk.Label(root, text="Do datuma", width=10, font=("bold", 10), anchor="w")
    lblDoDatuma.place(x=10, y=140)

    datum_do = tk.Entry(root, textvar=DoDatuma)
    datum_do.place(x=100, y=140)

    lblSLV = tk.Label(root, text="Prateci SLV", width=15, font=("bold", 10), anchor="w")
    lblSLV.place(x=10, y=180)

    slv = tk.Entry(root, textvar=SLVFile, width=50)
    slv.place(x=100, y=180)

#    def nadjiSLV():
#        kon.findSLV(SLVFile, slv)
    tk.Button(root, text='Pronadji', width=10, command=nadjiSLV).place(x=420, y=175)


    def nadjiSLV():
        kon.findSLV(SLVFile, slv)

    lblCS = tk.Label(root, text="SLV CS kol", width=20, font=("bold", 10), anchor="w")
    lblCS.place(x=10, y=260)

    cs = tk.Entry(root, textvar=cs)
    cs.place(x=100, y=260)

    lblPaid = tk.Label(root, text="SLV Paid kol", width=20, font=("bold", 10), anchor="w")
    lblPaid.place(x=280, y=260)

    paid = tk.Entry(root, textvar=paid)
    paid.place(x=400, y=260)

    lblInfo = tk.Label(root, text="Status obrade:", width=20, font=("bold", 10), anchor="w")
    lblInfo.place(x=280, y=290)

    textInfo = tk.Entry(root, textvar=InfoText, fg='blue')
    textInfo.place(x=400, y=290)

    # progress bar
    bar = Progressbar(root, length=250)
    bar['value'] = 0
    bar.place(x=280, y=320)

    lblCC = tk.Label(root, text="SLV CC kol", width=20, font=("bold", 10), anchor="w")
    lblCC.place(x=10, y=290)

    cc = tk.Entry(root, textvar=cc)
    cc.place(x=100, y=290)

    tk.Button(root, text='Generisi', width=20, bg='brown', fg='white', command=generateSTT).place(x=200, y=350)

    root.mainloop()

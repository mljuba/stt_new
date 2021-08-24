# import calendar
import datetime
# from datetime import date

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# from tkinter import ttk
# from tkinter.ttk import Progressbar
# from tkinter import Menu


def updateVrsta(up_vrsta, textinfo):
    textinfo.delete(0, tk.END)
    textinfo.insert(0, up_vrsta)
    textinfo.update()


def updateBar(broj, bar):
    bar['value'] = int(broj) * 5


def _check(self, index, size):
    entry = self.entries[index]
    next_index = index + 1
    next_entry = self.entries[next_index] if next_index < len(self.entries) else None
    data = entry.get()

    if len(data) > size or not data.isdigit():
        self._backspace(entry)
    if len(data) >= size and next_entry:
        next_entry.focus()


def left(s, amount=1, substring=""):
    if substring == "":
        return s[:amount]
    else:
        if len(substring) > amount:
            substring = substring[:amount]
        return substring + s[:-amount]


def right(s, amount=1, substring=""):
    if substring == "":
        return s[-amount:]
    else:
        if len(substring) > amount:
            substring = substring[:amount]
        return s[:-amount] + substring


def mid(s, offset, amount):
    return s[offset - 1:offset + amount - 1]


def checkDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d.%m.%Y')
        return 1
    except ValueError:
        messagebox.showwarning('Greska u datumu', 'Nije ispravan format datuma! \n Treba biti npr. 01.06.2020')
        return 0


def checkField(field_check, field_pos):
    if field_check != "":
        return 0
    else:
        if field_pos == 1:
            messagebox.showwarning('Greska u podacima', 'Nije unet CS broj kolone!')
            return 1
        elif field_pos == 2:
            messagebox.showwarning('Greska u podacima', 'Nije unet CC broj kolone!')
            return 2
        elif field_pos == 3:
            messagebox.showwarning('Greska u podacima', 'Nije unet Paid broj kolone!')
            return 3
        elif field_pos == 4:
            messagebox.showwarning('Greska u SLV fajlu', 'Nije pronadjen SLV fajl!')
            return 4


def working_days(start_dt, end_dt):
    num_days = (end_dt - start_dt).days + 1
    num_weeks = num_days // 7
    a = 0
    # condition 1
    if end_dt.strftime('%a') == 'Sat':
        if start_dt.strftime('%a') != 'Sun':
            a = 1
    # condition 2
    if start_dt.strftime('%a') == 'Sun':
        if end_dt.strftime('%a') != 'Sat':
            a = 1
    # condition 3
    if end_dt.strftime('%a') == 'Sun':
        if start_dt.strftime('%a') not in ('Mon', 'Sun'):
            a = 2
    # condition 4
    if start_dt.weekday() not in (0, 6):
        if (start_dt.weekday() - end_dt.weekday()) >= 2:
            a = 2
    working_days1 = num_days - (num_weeks * 2) - a

    return working_days1


def daysPassed(start_dt, end_dt):
    num_days = (end_dt - start_dt).days + 1
    num_weeks = num_days // 7
    a = 0
    # condition 1
    if end_dt.strftime('%a') == 'Sat':
        if start_dt.strftime('%a') != 'Sun':
            a = 1
    # condition 2
    if start_dt.strftime('%a') == 'Sun':
        if end_dt.strftime('%a') != 'Sat':
            a = 1
    # condition 3
    if end_dt.strftime('%a') == 'Sun':
        if start_dt.strftime('%a') not in ('Mon', 'Sun'):
            a = 2
    # condition 4
    if start_dt.weekday() not in (0, 6):
        if (start_dt.weekday() - end_dt.weekday()) >= 2:
            a = 2
    pass_working_days = num_days - (num_weeks * 2) - a

    return pass_working_days


def findSLV(slvfile, slv):
    SLVraw = filedialog.askopenfilename(initialdir="/", title="Pronadji SLV",
                                        filetype=(("xlsx", "*.xlsx"), ("All Files", "*.*")))
    slvfile.set(SLVraw)
    slv.delete(0, tk.END)
    slv.insert(0, SLVraw)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
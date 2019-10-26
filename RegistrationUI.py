from tkinter import *
import tkinter.messagebox

class RegistrationUI(parent=Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.religion_list = ["Christianity" , "Buddihsm" , "Islam" , "Sikh", "Hindu"]

    def initUI(self):
        self.parent.title("สุ่มเลขบัตรประชาชน - ลงทะเบียนเข้าสู่ระบบ")
        self.pack(fill=BOTH, expand=1)

        # New contact grid
        Label(self, text="Generated Citizen ID: ").grid(row=0, column=2, columnspan=2, sticky=W)
        Label(self, text="First Name:").grid(row=1, column=1, sticky=E)
        Label(self, text="Last Name:").grid(row=2, column=1, sticky=E)
        Label(self, text="Address").grid(row=3, column=1, sticky=E)

        self.entry1 = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)
        self.entry1.grid(row=1, column=2)
        self.entry2.grid(row=2, column=2)
        self.entry3.grid(row=3, column=2)

        religion_status_check = IntVar()
        self.religion_status_check = Checkbutton(self, variable=religion_status_check,
                                        command=self.require_religion,
                                        text="Specify Religion?")
        self.religion_status_check.grid(row=4, column=2, columnspan=2)

        Label(self, text="Birthday:").grid(row=5, column=1, sticky=E)
        Label(self, text="Religion:").grid(row=6, column=1, sticky=E)

        self.entry4 = Entry(self)
        self.entry5 = Entry(self)

        self.entry4.grid(row=5, column=2)
        self.entry5.grid(row=6, column=2)

        religion_list = Listbox(self, width=20, height=len(self.religion_list))
        religion_list.grid(row=0, column=1)
        for religion in self.religion_list:
            religion_list.insert(END, religion)

        religion_list.bind("<<ListboxSelect>>", self.onSelect)
        religion_list.place(x=20, y=210)


    def onSelect(self, val):
        sender = val.widget
        idk = sender.curselection()
        value = sender.get(idk)
        self.entry5.set(value)

    def require_religion(self):
        if self.religion_status_check.get() == 1:
            self.entry5.config(state='disabled')
        else:
            self.entry5.config(state='enabled')


def main():
    root = Tk()
    ex = RegistrationUI(root)
    root.geometry('600x700+200+100')
    root.mainloop()

if __name__ == '__main__':
    main()
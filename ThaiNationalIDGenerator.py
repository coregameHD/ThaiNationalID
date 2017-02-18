from tkinter import *
import random

class ThaiNationalID_Generator:
    def generate_number(self):
        random_num = random.randint(100000000000, 999999999999)
        temp = random_num
        sumall = 0

        for i in range(1,13):
            sumall += (i+1) * (random_num % 10)
            random_num = random_num // 10

        sumall = sumall % 11
        checksum = 11 - sumall
        result = (temp * 10) + checksum
        self.thai_id.set(result)

    def copy_button(self):
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(self.thai_id.get())
        clip.destroy()
        
    def __init__(self):
        window = Tk()
        window.title("สุ่มเลขบัตรประชาชน")

        # Menu Bar
        menubar = Menu(window)
        window.config(menu = menubar)

        filemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "Generate", command = self.generate_number)
        filemenu.add_command(label = "Copy to Clipboard", command = self.copy_button)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = window.quit)

        aboutmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "About", menu = aboutmenu)
        aboutmenu.add_command(label = "About Me")

        Label(window, text = "Thai National ID Generator").grid(row = 1,
                                                 column = 1, sticky = W)
        Label(window, text = "Your number is ").grid(row = 2,
                                                     column = 1, sticky = W)
        
        self.thai_id = StringVar()
        Entry(window, textvariable = self.thai_id,
              justify = RIGHT).grid(row = 2, column = 2, sticky = E)
        Button(window, text = "Generate",
               command = self.generate_number).grid(row = 4, column = 2, sticky = E)
        Button(window, text = "Copy to Clipboard",
               command = self.copy_button).grid(row = 4, column = 1, sticky = W)
        
        window.mainloop()  

ThaiNationalID_Generator()



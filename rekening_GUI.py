import tkinter as tk
from tkinter import ttk
from rekening_klasse import Rekening


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("300x150")
        self.configure(bg="#A8D0DB")
        self.spaarR1 = tk.StringVar()
        self.zichtR1 = tk.StringVar()
        self.spaarR2 = tk.StringVar()
        self.zichtR2 = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rekening1 = Rekening("R1",5000,8000)
        self.rekening2 = Rekening("R2",8000,18000)
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Spaarrekening 1:').grid(column=0, row=0, **padding)
        ttk.Label(self, text='Zichtrekening 1:').grid(column=0, row=1, **padding)
        ttk.Label(self, text='Spaarrekening 2:').grid(column=0, row=2, **padding)
        ttk.Label(self, text='zichtrekening 2:').grid(column=0, row=3, **padding)


        # Entry
        self.spaarR1.set(str(self.rekening1.spaarrekening))
        spaarr1_entry = ttk.Entry(self, textvariable=self.spaarR1)
        spaarr1_entry.grid(column=1, row=0, **padding)
        spaarr1_entry.focus()

        self.zichtR1.set(str(self.rekening1.zichtrekening))
        zichtr1 = ttk.Entry(self, textvariable=self.zichtR1)
        zichtr1.grid(column=1, row=1, **padding)

        self.spaarR2.set(str(self.rekening2.spaarrekening))
        spaarr2_entry = ttk.Entry(self, textvariable=self.spaarR2)
        spaarr2_entry.grid(column=1, row=2, **padding)

        self.zichtR2.set(str(self.rekening2.zichtrekening))
        zichtr2_entry = ttk.Entry(self, textvariable=self.zichtR2)
        zichtr2_entry.grid(column=1, row=3, **padding)


        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)

        submit_button.grid(column=1, row=4, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=5, columnspan=3, **padding)

    def submit(self):
        self.rekening1.spaarrekening = int(self.spaarR1.get())
        self.rekening2.spaarrekening = int(self.spaarR2.get())
        self.rekening1.zichtrekening = int(self.zichtR1.get())
        self.rekening2.zichtrekening = int(self.zichtR2.get())


        r3 = self.rekening1 + self.rekening2
        #print(r3)
        self.output_label.config(text=r3)


if __name__ == "__main__":
    app = App()
    app.mainloop()

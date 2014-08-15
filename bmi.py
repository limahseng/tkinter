# BMI Calculator

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class BMIApp(object):

  def __init__(self, master):
    
    # heading label
    self.heading_label = ttk.Label(master, text="BMI Calculator")
    self.heading_label.pack()

    # weight input
    self.weight_entry = ttk.Entry(master)
    self.weight_entry.pack()
    self.weight_entry.insert(0,"Weight in kg") 

    # height input
    self.height_entry = ttk.Entry(master)
    self.height_entry.pack()
    self.height_entry.insert(0,"Height in m")

    # submit button
    self.submit_button = ttk.Button(master, text="Compute!", command=self.calc_bmi)
    self.submit_button.pack()

  def calc_bmi(self):
    # compute and show bmi to 2 decimal places
    bmi = int(self.weight_entry.get()) / (float(self.height_entry.get()) * float(self.height_entry.get()))
    messagebox.showinfo(title="Your BMI", message="{0:.2f}".format(bmi))


def main():
  win = Tk()
  app = BMIApp(win)
  win.mainloop()

if __name__ == "__main__":
  main()

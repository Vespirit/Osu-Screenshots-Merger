import os
from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
  gui = Tk()
else:
  gui = Tk()
gui.title('Screenshot Folder Merger')
gui.resizable(False, False)
gui.geometry('400x200')
gui.grid_propagate(False)
for x in range(12):
  Grid.columnconfigure(gui, x, weight=1, uniform='row')
for y in range(6):
  Grid.rowconfigure(gui, y, weight=1, uniform='row')
for x in range(12):
  for y in range(6):
    Label(gui, width = 1, bg = '#FFFFFF').grid(row = y, column = x, sticky = N+S+E+W)
init = True
gui.Label1 = Label(gui, text = "Destination", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#FFFFFF')
gui.Label1.grid(row = 0, column = 1, columnspan = 7, rowspan = 1, sticky = N+S+E+W)
gui.Label2 = Label(gui, text = "New Folder", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#FFFFFF')
gui.Label2.grid(row = 2, column = 1, columnspan = 7, rowspan = 1, sticky = N+S+E+W)
gui.Label3 = Label(gui, text = "", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#FFFFFF')
gui.Label3.grid(row = 5, column = 4, columnspan = 8, rowspan = 1, sticky = N+S+E+W)
gui.Entry1 = Entry(gui, width = 1, bg = '#FFFFFF', justify = 'center')
gui.Entry1.grid(row = 1, column = 1, columnspan = 7, rowspan = 1, sticky = N+S+E+W)
gui.Entry1.insert(0, "")
gui.Entry2 = Entry(gui, width = 1, bg = '#FFFFFF', justify = 'center')
gui.Entry2.grid(row = 3, column = 1, columnspan = 7, rowspan = 1, sticky = N+S+E+W)
gui.Entry2.insert(0, "")
def runch_folder(argument):
  global init
  if not(__name__ == '__main__'):
    init = True
    from main import ch_folder
    gui.Label3.config(text="")
    folder = ch_folder()
    if argument == "Button1":
        gui.Entry1.delete(0, END)
        gui.Entry1.insert(0, folder)
    else:
        gui.Entry2.delete(0, END)
        gui.Entry2.insert(0, folder)
def runmerge(argument):
  global init
  if not(__name__ == '__main__'):
    init = True
    from main import merge
    merge(gui.Entry1.get(), gui.Entry2.get())
    gui.Label3.config(text="Merged successfully.")
gui.Button1 = Button(gui, text = "Browse", font = ('Arial', 14), width = 1, height = 1, fg = '#000000', command = lambda: runch_folder("Button1"), bg = '#00FFFF')
gui.Button1.grid(row = 1, column = 8, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
gui.Button2 = Button(gui, text = "Browse", font = ('Arial', 14), width = 1, height = 1, fg = '#000000', command = lambda: runch_folder("Button2"), bg = '#00FFFF')
gui.Button2.grid(row = 3, column = 8, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
gui.Button3 = Button(gui, text = "Merge", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', command = lambda: runmerge("Button3"), bg = '#00FFFF')
gui.Button3.grid(row = 5, column = 1, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
def initModules():
  from main import ch_folder
  from main import merge
gui.initModules = initModules
def hide():
  gui.withdraw()
def show():
  gui.deiconify()
def hideAllWidgets():
    gui.Label1.grid_remove()
    gui.Label2.grid_remove()
    gui.Label3.grid_remove()
    gui.Entry1.grid_remove()
    gui.Entry2.grid_remove()
    gui.Button1.grid_remove()
    gui.Button2.grid_remove()
    gui.Button3.grid_remove()
gui.hideAllWidgets = hideAllWidgets
def showAllWidgets():
    gui.Label1.grid()
    gui.Label2.grid()
    gui.Label3.grid()
    gui.Entry1.grid()
    gui.Entry2.grid()
    gui.Button1.grid()
    gui.Button2.grid()
    gui.Button3.grid()
gui.showAllWidgets = showAllWidgets
running = True
def isRunning():
    global running
    return running
def quit():
    global running
    running = False
    gui.hide()
gui.protocol("WM_DELETE_WINDOW", quit)
gui.isRunning = isRunning
def run():
  global init
  gui.update()
  gui.update_idletasks()
  if init:
    gui.Label1.config(wraplength = gui.Label1.winfo_width() + 2)
    gui.Label2.config(wraplength = gui.Label2.winfo_width() + 2)
    gui.Label3.config(wraplength = gui.Label3.winfo_width() + 2)
    gui.Button1.config(wraplength = gui.Button1.winfo_width() + 2)
    gui.Button2.config(wraplength = gui.Button2.winfo_width() + 2)
    gui.Button3.config(wraplength = gui.Button3.winfo_width() + 2)
    if (gui.Label1.cget("wraplength") > 3):
        init = False
gui.run = run
gui.hide = hide
gui.show = show

if __name__ == "__main__":
  while isRunning():
    gui.run()

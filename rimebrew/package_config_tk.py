from tkinter import *
import tkinter.ttk as ttk

# Preliminary code for a simple GUI
# Alternative style of the package config.

# TODO: add weight to resize arbitrary

root = Tk()
root.title("Rimebrew")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frameStyle=ttk.Style()
frameStyle.configure('i.TFrame',background='red')

mainFrame = ttk.Frame(root)
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

mainFrame.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(2, weight=1)

Installed_frame = ttk.Frame(mainFrame)
Installed_list = Listbox(Installed_frame)
Installed_text = ttk.Label(Installed_frame, text="Available Schemas")

Installed_frame.columnconfigure(0, weight=1)
Installed_frame.rowconfigure(1, weight=1)

Active_frame = ttk.Frame(mainFrame)
Active_list = Listbox(Active_frame)
Active_text = ttk.Label(Active_frame, text="Activated Schemas")
Active_frame.columnconfigure(0, weight=1)
Active_frame.rowconfigure(1, weight=1)

Middle_frame = ttk.Frame(mainFrame)

Installed_frame.grid(column=0, row=0, sticky=(N, W, E, S))
Middle_frame.grid(column=1, row=0)
Active_frame.grid(column=2, row=0, sticky=(N, W, E, S))

Installed_text.grid(column=0, row=0, sticky=(N, W))
Installed_list.grid(column=0, row=1, sticky=(N, W, E, S))

Active_text.grid(column=0, row=0, sticky=(N, W))
Active_list.grid(column=0, row=1, sticky=(N, W, E, S))

active_btn = ttk.Button(Middle_frame, text="→")
deactive_btn = ttk.Button(Middle_frame, text="←")

active_btn.grid(column=0, row=0, sticky=(S, W, E))
deactive_btn.grid(column=0, row=1, sticky=(S, W, E))

root.mainloop()

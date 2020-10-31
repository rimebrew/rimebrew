from  tkinter import *
import tkinter.ttk as ttk
# Preliminary code for a simple GUI

# TODO: add weight to resize arbitrary

root = Tk()
root.title("Rimebrew")

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)


mainFrame = ttk.Frame(root)
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))


# weight=0 means the first row or the grid wouldn't change at all.
mainFrame.rowconfigure(0,weight=0)
mainFrame.rowconfigure(1,weight=1)

mainFrame.columnconfigure(0,weight=1)


# toolbar area
toolbarFrame = ttk.Frame(mainFrame)
toolbarFrame.grid(column=0,row=0, sticky=(N, W, E, S))

toolbarFrame.columnconfigure(3,weight=1)

buttom_update = ttk.Button(toolbarFrame,text='update')
buttom_update.grid(column=0,row=0, sticky='nesw')

buttom_install= ttk.Button(toolbarFrame,text='install')
buttom_install.grid(column=1,row=0, sticky='nesw')

buttom_remove = ttk.Button(toolbarFrame,text='remove')
buttom_remove.grid(column=2,row=0, sticky='nesw')

search_box    = ttk.Entry(toolbarFrame)
search_box.grid(column=3,row=0, sticky='nesw')

search_box.insert('0',"Type here...")
buttom_search = ttk.Button(toolbarFrame,text='search')\
                 .grid(column=4,row=0, sticky='nesw')

#Display area
middleFrame = ttk.Labelframe(mainFrame,text="Schema List")
middleFrame.grid(column=0,row=1, sticky='nesw')
middleFrame.columnconfigure(0,weight=1)
middleFrame.rowconfigure(0,weight=1)


tree = ttk.Treeview(middleFrame)
tree.grid(column=0,row=0, sticky='nesw')

tree["columns"]=("one","two")
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("" , 0,    text="Line 1", values=("1A","1b"))

id2 = tree.insert("", 1, "dir2", text="Dir 2")
tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))

tree.insert("", 3, "dir3", text="Dir 3")
tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))

root.mainloop()


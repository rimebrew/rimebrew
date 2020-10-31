import tkinter as tk
import tkinter.ttk as ttk
# Preliminary code for a simple GUI

class rimebrewGUI:
    def __init__(self, master=None):
        # build ui
        self.frame_1 = ttk.Frame(master)
        self.button_5 = ttk.Button(self.frame_1)
        self.button_5.config(text='button_5')
        self.button_5.grid(sticky='w')
        self.button_6 = ttk.Button(self.frame_1)
        self.button_6.config(text='button_6')
        self.button_6.grid(column='1', row='0', sticky='w')
        self.button_7 = ttk.Button(self.frame_1)
        self.button_7.config(text='button_7')
        self.button_7.grid(column='2', row='0', sticky='w')
        self.entry_2 = ttk.Entry(self.frame_1)
        _text_ = '''entry_2'''
        self.entry_2.delete('0', 'end')
        self.entry_2.insert('0', _text_)
        self.entry_2.grid(column='3', row='0', sticky='w')
        self.button_8 = ttk.Button(self.frame_1)
        self.button_8.config(text='button_8')
        self.button_8.grid(column='4', row='0', sticky='w')
        self.panedwindow_1 = ttk.Panedwindow(self.frame_1, orient='horizontal')
        self.panedwindow_1.config(height='200', width='200')
        self.panedwindow_1.grid(column='0', columnspan='5', row='1')
        self.Infopan = ttk.Notebook(self.frame_1)
        self.Infopan.config(height='200', width='200')
        self.Infopan.grid(column='0', columnspan='5', row='2')
        self.frame_1.config(height='200', width='200')
        self.frame_1.grid()

        # Main widget
        self.mainwindow = self.frame_1


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = rimebrewGUI(root)
    app.run()


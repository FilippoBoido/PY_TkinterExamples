import tkinter as tk

class ListFrame(tk.Frame):
    def __init__(self, master, items=[]):
        super().__init__(master)
        self.list = tk.Listbox(self)
        self.scroll = tk.Scrollbar(self,
                                   orient=tk.VERTICAL,
                                   command=self.list.yview)
        self.list.config(yscrollcommand=self.scroll.set)
        self.list.insert(0,*items)
        self.list.pack(side=tk.LEFT,
                       expand=True,
                       fill=tk.BOTH)
        self.scroll.pack(side=tk.LEFT,
                         fill=tk.Y)
        
        
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        lf = ListFrame(self)
        lf.pack(expand=True,
                fill=tk.BOTH)
        self.mainloop()
        
        
if __name__ == "__main__":
    App()

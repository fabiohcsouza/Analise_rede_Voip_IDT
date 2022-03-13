import tkinter as tk

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Analise rede VoIP - Net2Phone')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    root.tk.call('wm', 
                'iconphoto', 
                root._w, 
                tk.PhotoImage(file='images/net2phone.png'))
    return root
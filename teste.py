import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
import core
########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Analise rede VoIP - Net2Phone")
        self.frame = tk.Frame(parent).pack()

        # Widget Label superior
        self.lb1 = ttk.Label(self.frame, text=('TROUBLESHOOT VOIP - github.com/fabiohcsouza/Analise_rede_VoIP'),
        background="#00008B",
        foreground="white",
        anchor=tk.CENTER,
        padding=5,
        width=132,
        )
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='images/net2phone.png'))

        self.lb1.pack(fill="x") #lb superior

    #-Widget-Label----------------------------------------------------------
        # Widget Notebook
        self.nb1 = ttk.Notebook(self.frame)
        self.nb1.pack(fill="both", expand=True, padx=10, pady=10)

        self.frame2 = ttk.Frame(self.nb1)
        self.frame2.pack(fill="both", expand=True)

        self.frame1 = ttk.LabelFrame(self.frame2, text="MTR", relief=SUNKEN)
        self.frame1.grid(row=0, column=0, padx=5, pady=5)

        self.nb1.add(self.frame2, text="Troubleshoot")

        # Widget lb portal
        self.lb2 = ttk.Label(self.frame1, text=('Select portal:'),
        width=20,
        )

        # Widgt CCB portais
        self.ccb1_var = tk.Variable
        self.ccb1 = ttk.Combobox(self.frame1, textvariable=self.ccb1_var, 
        values=core.portais, 
        width=17,
        )
        self.ccb1.bind("<<ComboboxSelected>>", self.op_check1)
        
        # Widget lb output portal
        self.lb3 = ttk.Label(self.frame1, text="- None",
        width=30,
        )

        # Widget lb gateway
        self.lb4 = ttk.Label(self.frame1, text="Enter IP gateway:",
        width=20,
        )

        # Widget input gateway
        self.entry1_var = StringVar
        self.entry1 = ttk.Entry(self.frame1, textvariable=self.entry1_var,
        width=20,
        )

        # Widget lb host
        self.lb5 = ttk.Label(self.frame1, text="Enter IP Host:",
        width=20,
        )

        # Widget input host
        self.entry2_var = StringVar
        self.entry2 = ttk.Entry(self.frame1, textvariable=self.entry2_var,
        width=20,
        justify=tk.LEFT
        )

        # Widget bt start
        self.handler = lambda: self.progress_bar(True)
        self.btn1 = ttk.Button(self.frame1, text="Start", 
        command=self.handler,
        )

        # Widget bt Parar
        self.handler1 = lambda: self.progress_bar(False) 
        self.btn2 = ttk.Button(self.frame1, text="Stop", 
        command=self.handler1,
        )

        self.pb = ttk.Progressbar(self.frame1,
        orient='horizontal',
        mode='indeterminate',
        length=200
        )
        

        self.lb2.grid(row=0, column=0, pady=5, padx=5) #lb input portal
        self.ccb1.grid(row=0, column=1, pady=5, padx=5) #CCB portais
        self.lb3.grid(row=0, column=2, pady=5, padx=5) #lb output portal

        self.lb4.grid(row=1, column=0, pady=5, padx=5) #lb gateway
        self.entry1.grid(row=1, column=1, pady=5, padx=5) #input gateway
        self.lb5.grid(row=2, column=0, pady=5, padx=5) #lb host
        self.entry2.grid(row=2, column=1, pady=5, padx=5) #input host

        self.btn1.grid(row=3, column=0) #bt Start
        self.btn2.grid(row=3, column=1) #bt Stop
        
        
    #-Widget-Label-2-------------------------------------------------------


    #-Barra-progresso------------------------------------------------------
    def progress_bar(self, status):

        self.pb.grid(row=3, column=2, pady=5, padx=5)

        while True:
            if status == True:
                self.btn1['command'] = self.pb.start
                break
            elif status == False:
                self.btn2['command'] = self.pb.stop
                break
            else:
                break
       

    #-Remover-janela-------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()
        
    #----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.geometry("400x300")
        otherFrame.title("otherFrame")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        btn = tk.Button(otherFrame, text="Close", command=handler)
        btn.pack()
        
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()
        
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        #self.root.deiconify()
        
        #----------------------------------------------------------------------
    def op_check1(self, event):
        """"""
        self.resp1 = self.ccb1.get()
        self.resp_portal = core.portal_entrada[self.resp1]
        self.lb3['text'] = "- " + self.resp_portal
#----------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()
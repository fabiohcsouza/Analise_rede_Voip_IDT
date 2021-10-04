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
        self.frame = tk.Frame(parent).grid()

        # Widget Label superior
        self.lb1 = ttk.Label(self.frame, text=('TROUBLESHOOT VOIP - github.com/fabiohcsouza/Analise_rede_VoIP'),
        background="#00008B",
        foreground="white",
        anchor=tk.CENTER,
        padding=5,
        width=132,
        ).grid()
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='images/net2phone.png'))


    #-Widget-Label----------------------------------------------------------
        # Widget Notebook
        self.nb1 = ttk.Notebook(self.frame, width=796, height=500)
        self.nb1.grid()

        self.frame1 = tk.Frame(self.nb1)
        self.frame1.grid()

        self.frame2 = tk.Frame(self.frame1)
        self.frame2.grid(row=0,column=0)

        self.frame3 = tk.Frame(self.frame1)
        self.frame3.grid(row=0,column=1)

        self.nb1.add(self.frame1, text="Troubleshoot")

        # Widget Label2
        self.lb2 = ttk.Label(self.frame2, text=('Selecione o portal:'),
        padding=5,
        )
        self.lb2.grid(row=0, column=0)

        # Widgt seleção portal
        self.ccb1_var = tk.Variable
        self.ccb1 = ttk.Combobox(self.frame2, textvariable=self.ccb1_var, 
        values=core.portais, 
        height=10,
        )
        self.ccb1.bind("<<ComboboxSelected>>", self.op_check1)
        self.ccb1.grid(row=0, column=1)
        
        # Widget Label3
        self.lb3 = ttk.Label(self.frame3, text="- None",
        padding=5,
        )
        self.lb3.grid(row=0, column=2)

        # Widget Label4
        self.lb4 = ttk.Label(self.frame2, text="Informe IP gateway:",
        padding=5,
        )
        self.lb4.grid(row=1, column=0)

        # Widget Entry 1
        self.entry1_var = StringVar
        self.entry1 = ttk.Entry(self.frame2, textvariable=self.entry1_var,
        )
        self.entry1.grid(row=1, column=1)

        # Widget Label5
        self.lb5 = ttk.Label(self.frame3, text="Informe IP Host:",
        padding=5,
        )
        self.lb5.grid(row=1, column=2)

        # Widget Entry 2
        self.entry2_var = StringVar
        self.entry2 = ttk.Entry(self.frame3, textvariable=self.entry2_var,
        )
        self.entry2.grid(row=1, column=3)

        # Widget botão
        handler = lambda: self.openFrame()
        btn1 = ttk.Button(self.frame2, text="Start", command=handler)
        btn1.grid(row=3, column=0)
    #-Widget-Label-2-------------------------------------------------------


    #-Seleção-portal-------------------------------------------------------
    def select_input(self):
        ccb1_var = tk.Variable
        ccb_1 = ttk.Combobox(self.frame1, textvariable=ccb1_var)
        ccb_1['values'] = core.portais
        ccb_1.bind("<<ComboboxSelected>>", )

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
        self.root.deiconify()
        
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
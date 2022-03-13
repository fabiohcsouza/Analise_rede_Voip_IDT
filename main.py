import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
import core
from tkinter.messagebox import showinfo

########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Analise rede VoIP - Net2Phone")
        self.frame = tk.Frame(parent, bg='#fff').pack()
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='images/net2phone.png'))

        # Widget Label superior
        self.lb1 = ttk.Label(self.frame, text=('TROUBLESHOOT VOIP - github.com/fabiohcsouza/Analise_rede_VoIP'),
        background="#00008B",
        foreground="white",
        anchor=tk.CENTER,
        padding=5,
        width=132,
        )
        self.lb1.pack(fill="x") #lb superior

    #-Widget-Label----------------------------------------------------------
        # Widget Notebook
        self.nb1 = ttk.Notebook(self.frame)
        self.nb1.pack(fill="both", expand=True, padx=10, pady=10)

        self.frame2 = ttk.Frame(self.nb1)
        self.frame2.pack(fill="both", expand=True)

        self.frame1 = ttk.LabelFrame(self.frame2, text="Data-Input", relief=SUNKEN)
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

        self.pb = ttk.Progressbar(self.frame1,
        orient='horizontal',
        mode='indeterminate',
        length=200
        )

        # Widget bt start
        self.handler = lambda: self.start_bar()
        self.btn1 = ttk.Button(self.frame1, text="Start", 
        command=self.handler
        )

        # Widget bt Parar
        self.handler1 = lambda: self.stop_bar()
        self.btn2 = ttk.Button(self.frame1, text="Stop", 
        command=self.handler1,
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
        self.pb.grid(row=3, column=2, pady=5, padx=5)
        
    #-Widget-Label-2-------------------------------------------------------
        self.frame3 = ttk.LabelFrame(self.frame2, text="Data-Output", relief=SUNKEN)
        self.frame3.grid(row=1, column=0, padx=5, pady=5)

        self.nb2 = ttk.Notebook(self.frame3)
        self.nb2.pack(fill="both", expand=True)

        self.frame4 = ttk.Frame(self.nb2)
        self.frame4.pack(fill="both", expand=True)

        self.nb2.add(self.frame4, text="MTR-Out_Portal")

        columns = ('#0', '#1', '#2', '#3', '#4','#5','#6','#7','#8','#9')

        self.tree = ttk.Treeview(self.frame4, columns=columns, show='headings')

        self.tree.column('#0', minwidth=0, width=60)
        self.tree.column('#1', minwidth=0, width=30)
        self.tree.column('#2', minwidth=0, width=110)
        self.tree.column('#3', minwidth=0, width=60)
        self.tree.column('#4', minwidth=0, width=60)
        self.tree.column('#5', minwidth=0, width=60)
        self.tree.column('#6', minwidth=0, width=60)
        self.tree.column('#7', minwidth=0, width=60)
        self.tree.column('#8', minwidth=0, width=60)
        self.tree.column('#9', minwidth=0, width=60)

        self.tree.heading('#0', text='Hora')
        self.tree.heading('#1', text='Nº')
        self.tree.heading('#2', text='Host')
        self.tree.heading('#3', text='Loss%')
        self.tree.heading('#4', text='Snt')
        self.tree.heading('#5', text='Recv')
        self.tree.heading('#6', text='Best')
        self.tree.heading('#7', text='Avrg')
        self.tree.heading('#8', text='Worsl')
        self.tree.heading('#9', text='Last')

        # adding data to the treeview
        for d in core.portal_out["mtr"]:
            self.tree.insert('', tk.END, values=d)

        self.tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self.frame4, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

                # bind the select event
        def item_selected(event):
                showinfo(title='Information',
                        message="Exelente")


        self.tree.bind('<<TreeviewSelect>>', item_selected)

    #-Barra-progresso------------------------------------------------------
    def progress_bar(self, status):

        if status == True:
            self.start_bar()
        elif status == False:
            self.stop_bar()

    def start_bar(self):
        self.btn1['command'] = self.pb.start
    
    def stop_bar(self):
        self.btn2['command'] = self.pb.stop
    

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
    def show_selected_size():
        showinfo(
            title='Result',
            message="Teste Ok"
        )
        
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
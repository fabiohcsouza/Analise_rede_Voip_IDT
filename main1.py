import tkinter as tk
from teste import make_root
from teste import Interface

def main():
    root = make_root()
    interface = Interface(root)
    interface.start()

if '__name__' == '__main__':
    main()
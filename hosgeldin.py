#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import ttk
import os, platform, distro
import webbrowser

def main():
    root = tk.Tk()
    root.geometry("700x475")
    root.iconphoto(False, tk.PhotoImage(file="images/pisilinux-welcome.png"))
    root.title("Pisi Linux'a Hoş Geldiniz")
    root.resizable(width=False, height=False)

    #header
    frm_header = tk.Frame(root, bg="gray20")
    frm_header.pack(side=TOP, fill=X)

    img_pisi_white = tk.PhotoImage(file="images/pisi-white2.png")
    lbl_pisi_white = tk.Label(frm_header, width=128, height=128, image=img_pisi_white, bg="gray20")
    lbl_pisi_white.pack(side=LEFT)

    img_pisi_text = tk.PhotoImage(file="images/pisi-text.png")
    lbl_pisi_text = tk.Label(frm_header, image=img_pisi_text, bg="gray20")
    lbl_pisi_text.pack(side=LEFT)

    lbl_distro = tk.Label(frm_header, text="\n"+distro.name()+" "+distro.version(), bg="gray20", fg="white", font=('System', 16, 'bold'))
    lbl_distro.pack()

    txt_kernel = platform.release()
    lbl_kernel = tk.Label(frm_header, text="Kernel : "+txt_kernel, bg="gray20", fg="white", font=('System', 16, 'bold'))
    lbl_kernel.pack()


    #container


    #footer


    root.mainloop()

if __name__ == '__main__':
    main()
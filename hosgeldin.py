#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import ttk
import os, platform, distro
import webbrowser

def callback(url):
    webbrowser.open_new(url)

def main():
    root = tk.Tk()
    root.geometry("700x475")
    root.iconphoto(False, tk.PhotoImage(file="images/pisilinux-welcome.png"))
    root.title("Pisi Linux'a Hoş Geldiniz")
    root.resizable(width=False, height=False)

    #header
    frm_header = tk.Frame(root, bg="gray20")
    frm_header.pack(side=TOP, fill=X)

    img_pisi_white = tk.PhotoImage(file="images/pisi-white-96.png")
    # lbl_pisi_white = tk.Label(frm_header, width=128, height=128, image=img_pisi_white, bg="gray20")
    lbl_pisi_white = tk.Label(frm_header, image=img_pisi_white, bg="gray20")
    lbl_pisi_white.pack(side=LEFT)

    img_pisi_text = tk.PhotoImage(file="images/pisi-text-80.png")
    lbl_pisi_text = tk.Label(frm_header, image=img_pisi_text, bg="gray20")
    lbl_pisi_text.pack(side=LEFT)

    lbl_distro = tk.Label(frm_header, text="\n"+distro.name()+" "+distro.version(), bg="gray20", fg="white", font=("System", 16, "bold"))
    lbl_distro.pack()

    txt_kernel = platform.release()
    lbl_kernel = tk.Label(frm_header, text="Kernel v"+txt_kernel, bg="gray20", fg="white", font=('System', 16, 'bold'))
    lbl_kernel.pack()


    #container
    txt_widget = tk.Text(root, width=100, height=7, font=("System", 10), wrap=WORD, bd=0, highlightthickness=0)
    txt = "\nPisi Linux'a Hoş Geldiniz!.. Topluluğumuza katıldığınız için teşekkür ederiz! \n\nPisi Linux geliştiricileri olarak Pisi Linux'u kullanmaktan zevk almanızı umuyoruz. Aşağıdaki bağlantılar Pisi Linux kullanmanıza kılavuzluk edecektir. Lütfen deneyimlerinizi, önerilerinizi ve karşılaştığınız hataları bize bildirmekten çekinmeyiniz."""
    txt_widget.tag_configure("tag", justify="center")
    txt_widget.insert("1.0", txt)
    txt_widget.tag_add("tag", "1.0", "end")
    txt_widget.pack(fill="both")

    #grid
    frm_link = tk.Frame(root, bg="white")
    frm_link.pack(fill="both")

    #1. kolon
    lbl_belgeler = tk.Label(frm_link, text="Belgeler", font=("System", 16, "bold"), bg="white")
    lbl_belgeler.grid(row=0, column=0, padx=50, pady=5)
    
    img_pisi_kilavuzu = tk.PhotoImage(file="images/guide-32.png")
    link_pisi_kilavuzu = tk.Label(frm_link, image=img_pisi_kilavuzu, text="Pisi Kılavuzu", compound="left", cursor="hand2", bg="white")
    link_pisi_kilavuzu.bind("<Button-1>", lambda e: callback("https://pisilinux.org/en/pisilinux-kurulumu/"))
    link_pisi_kilavuzu.grid(row=1, column=0, padx=50, pady=10)

    img_surum_notlari = tk.PhotoImage(file="images/info-24.png")
    link_surum_notlari = tk.Label(frm_link, image=img_surum_notlari, text="Sürüm Notları", compound="left", cursor="hand2", bg="white")
    link_surum_notlari.bind("<Button-1>", lambda e: callback("file:///usr/share/pisilinux-welcome/data/release-notes/release-notes-tr.html"))
    link_surum_notlari.grid(row=2, column=0, padx=50, pady=10)

    img_pisi_wiki = tk.PhotoImage(file="images/wiki-24.png")
    link_pisi_wiki = tk.Label(frm_link, image=img_pisi_wiki, text="Pisi Linux Wiki", compound="left", cursor="hand2", bg="white")
    link_pisi_wiki.bind("<Button-1>", lambda e: callback("https://pisilinux.org/wiki/"))
    link_pisi_wiki.grid(row=3, column=0, padx=50, pady=10)

    #2. kolon
    lbl_destek = tk.Label(frm_link, text="Destek", font=("System", 16, "bold"), bg="white")
    lbl_destek.grid(row=0, column=1, padx=50, pady=5)


    #3. kolon
    lbl_proje = tk.Label(frm_link, text="Proje", font=("System", 16, "bold"), bg="white")
    lbl_proje.grid(row=0, column=2, padx=50, pady=5)
    

    #footer



    root.mainloop()

if __name__ == '__main__':
    main()
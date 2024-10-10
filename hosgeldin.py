#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
import os, shutil, platform, distro, webbrowser
import gettext, locale, sys


gettext.bindtextdomain("messages", locale)
gettext.textdomain("messages")

user_locale = locale.getlocale()[0]
locale = sys.argv[1] if len(sys.argv) > 1 else user_locale
lang = gettext.translation("messages", localedir="locale", fallback=True, languages=[locale])
lang.install()
_ = lang.gettext

def callback(url):
    webbrowser.open_new(url)

def main():
    root = tk.Tk()
    root.geometry("700x475")
    root.iconphoto(False, tk.PhotoImage(file="images/pisi-hosgeldin.png"))
    root.title(_("Pisi Linux'a Hoş Geldiniz"))
    root.resizable(width=False, height=False)

    #header
    frm_header = tk.Frame(root, bg="gray20")
    frm_header.pack(side=TOP, fill="both")

    img_pisi_white = tk.PhotoImage(file="images/pisi-white-96.png")
    lbl_pisi_white = tk.Label(frm_header, image=img_pisi_white, bg="gray20")
    lbl_pisi_white.pack(side=LEFT)

    img_pisi_text = tk.PhotoImage(file="images/pisi-text-80.png")
    lbl_pisi_text = tk.Label(frm_header, image=img_pisi_text, bg="gray20")
    lbl_pisi_text.pack(side=LEFT)

    lbl_distro = tk.Label(frm_header, text="\n"+distro.name()+" "+distro.version(), bg="gray20", fg="white", font=("fixedsys", 16, "bold"))
    lbl_distro.pack()

    txt_kernel = platform.release()
    lbl_kernel = tk.Label(frm_header, text="Kernel v"+txt_kernel, bg="gray20", fg="white", font=("fixedsys", 16, "bold"))
    lbl_kernel.pack()


    #container
    txt_widget = tk.Text(root, padx=50, height=7, font=("Noto", 10), wrap=WORD, bd=0, highlightthickness=0)
    txt = _("\nPisi Linux'a Hoş Geldiniz!.. Topluluğumuza katıldığınız için teşekkür ederiz! \n\nPisi Linux geliştiricileri olarak Pisi Linux'u kullanmaktan zevk almanızı umuyoruz. Aşağıdaki bağlantılar Pisi Linux kullanmanıza kılavuzluk edecektir. Lütfen deneyimlerinizi, önerilerinizi ve karşılaştığınız hataları bize bildirmekten çekinmeyiniz.""")
    txt_widget.tag_configure("tag", justify="center")
    txt_widget.insert("1.0", txt)
    txt_widget.tag_add("tag", "1.0", "end")
    txt_widget.pack(fill="both")

    #grid
    frm_link = tk.Frame(root, pady=33, bg="white")
    frm_link.pack(fill="both")

    #1. kolon
    lbl_belgeler = tk.Label(frm_link, text=_("Belgeler"), font=("Noto", 12, "bold"), bg="white", width=10)
    lbl_belgeler.grid(row=0, column=0, padx=50)
    
    img_pisi_kilavuzu = tk.PhotoImage(file="images/guide-32.png")
    link_pisi_kilavuzu = tk.Label(frm_link, image=img_pisi_kilavuzu, text=_("Pisi Kılavuzu"), compound="left", cursor="hand2", bg="white")
    link_pisi_kilavuzu.bind("<Button-1>", lambda e: callback("https://pisilinux.org/en/pisilinux-kurulumu/"))
    link_pisi_kilavuzu.grid(row=1, column=0)

    img_surum_notlari = tk.PhotoImage(file="images/info-24.png")
    link_surum_notlari = tk.Label(frm_link, image=img_surum_notlari, text=_("Sürüm Notları"), compound="left", cursor="hand2", bg="white")
    link_surum_notlari.bind("<Button-1>", lambda e: callback("file:///usr/share/pisilinux-welcome/data/release-notes/release-notes-tr.html"))
    link_surum_notlari.grid(row=2, column=0)

    img_pisi_wiki = tk.PhotoImage(file="images/wiki-24.png")
    link_pisi_wiki = tk.Label(frm_link, image=img_pisi_wiki, text=_("Pisi Linux Wiki"), compound="left", cursor="hand2", bg="white")
    link_pisi_wiki.bind("<Button-1>", lambda e: callback("https://pisilinux.org/wiki/"))
    link_pisi_wiki.grid(row=3, column=0)

    #2. kolon
    lbl_destek = tk.Label(frm_link, text=_("Destek"), font=("Noto", 12, "bold"), bg="white", width=12)
    lbl_destek.grid(row=0, column=1, padx=50)

    img_forum = tk.PhotoImage(file="images/forum-36.png")
    link_forum = tk.Label(frm_link, image=img_forum, text=_("Pisi Forum Sayfası"), compound="left", cursor="hand2", bg="white")
    link_forum.bind("<Button-1>", lambda e: callback("https://pisilinux.org/forum"))
    link_forum.grid(row=1, column=1)

    img_pisi_telegram = tk.PhotoImage(file="images/chat-36.png")
    link_pisi_telegram = tk.Label(frm_link, image=img_pisi_telegram, text=_("PisiLinux Telegram"), compound="left", cursor="hand2", bg="white")
    link_pisi_telegram.bind("<Button-1>", lambda e: callback("https://t.me/joinchat/MAcpp0o6E4dAAoz090cDjA"))
    link_pisi_telegram.grid(row=2, column=1)

    img_pisi_hatalari = tk.PhotoImage(file="images/bug-36.png")
    link_pisi_hatalari = tk.Label(frm_link, image=img_pisi_hatalari, text=_("PisiLinux Hataları"), compound="left", cursor="hand2", bg="white")
    link_pisi_hatalari.bind("<Button-1>", lambda e: callback("https://github.com/pisilinux/main/issues/new"))
    link_pisi_hatalari.grid(row=3, column=1)

    #3. kolon
    lbl_proje = tk.Label(frm_link, text=_("Proje"), font=("Noto", 12, "bold"), bg="white", width=10)
    lbl_proje.grid(row=0, column=2, padx=50)

    img_kaptan = tk.PhotoImage(file="images/kaptan-36.png")
    link_kaptan = tk.Label(frm_link, image=img_kaptan, text=_("Kaptan'ı Başlat"), compound="left", cursor="hand2", bg="white")
    # link_kaptan.bind("<Button-1>", lambda e: callback(os.system("kaptan")))
    link_kaptan.bind("<Button-1>", lambda e: (os.system("kaptan")))
    link_kaptan.grid(row=1, column=2)

    img_join_us = tk.PhotoImage(file="images/join-us-36.png")
    link_join_us = tk.Label(frm_link, image=img_join_us, text=_("Bize Katılın"), compound="left", cursor="hand2", bg="white")
    link_join_us.bind("<Button-1>", lambda e: callback("https://pisilinux.org/contact/"))
    link_join_us.grid(row=2, column=2)

    img_home = tk.PhotoImage(file="images/home-36.png")
    link_home = tk.Label(frm_link, image=img_home, text=_("Pisi AnaSayfa"), compound="left", cursor="hand2", bg="white")
    link_home.bind("<Button-1>", lambda e: callback("https://pisilinux.org/"))
    link_home.grid(row=3, column=2)
    

    #footer
    frm_footer = tk.Frame(root, padx=5, pady=5, bg="gray20")
    frm_footer.pack(side=BOTTOM, fill="both")

    img_facebook = tk.PhotoImage(file="images/facebook-36.png")
    lbl_facebook = tk.Label(frm_footer, image=img_facebook, cursor="hand2", bg="gray20")
    lbl_facebook.bind("<Button-1>", lambda e: callback("https://www.facebook.com/Pisilinux/"))
    lbl_facebook.pack(side=LEFT)

    img_twitter = tk.PhotoImage(file="images/twitter-36.png")
    lbl_twitter = tk.Label(frm_footer, image=img_twitter, cursor="hand2", bg="gray20")
    lbl_twitter.bind("<Button-1>", lambda e: callback("https://x.com/pisi_linux"))
    lbl_twitter.pack(side=LEFT)

    img_instagram = tk.PhotoImage(file="images/instagram-36.png")
    lbl_instagram = tk.Label(frm_footer, image=img_instagram, cursor="hand2", bg="gray20")
    lbl_instagram.bind("<Button-1>", lambda e: callback("https://www.instagram.com/pisilinux_official/"))
    lbl_instagram.pack(side=LEFT)

    img_youtube = tk.PhotoImage(file="images/youtube-36.png")
    lbl_youtube = tk.Label(frm_footer, image=img_youtube, cursor="hand2", bg="gray20")
    lbl_youtube.bind("<Button-1>", lambda e: callback("https://www.youtube.com/channel/UCLGSGLpxVE-vxzBuebBj3tA"))
    lbl_youtube.pack(side=LEFT)

    img_github = tk.PhotoImage(file="images/github-36.png")
    lbl_github = tk.Label(frm_footer, image=img_github, cursor="hand2", bg="gray20")
    lbl_github.bind("<Button-1>", lambda e: callback("https://github.com/pisilinux"))
    lbl_github.pack(side=LEFT)

    # hosgeldin başlangıçta açılabilmesi için HOME/.config/autostart dizininin kontrolü
    autostart_path = os.path.join(os.environ["HOME"], ".config", "autostart")
    if not os.path.exists(autostart_path):
        os.makedirs(autostart_path)

    def on_button_toggle():
        if var.get() == 1:
            shutil.copy("pisi-hosgeldin.desktop",
                        os.path.join(os.environ["HOME"], ".config", "autostart"))
        else:
            os.remove(
                os.path.join(
                    os.environ["HOME"], ".config", "autostart", "pisi-hosgeldin.desktop"))
            
    file_path = os.path.join(os.environ["HOME"], ".config", "autostart", "pisi-hosgeldin.desktop")
    var = tk.IntVar()
    if os.path.isfile(file_path):
        var.set(1)
    else:
        var.set(0)

    chkbox_baslangic = tk.Checkbutton(frm_footer, text=_("Sistem açılışında göster"), variable=var, onvalue=1, offvalue=0, command=on_button_toggle, padx=10, bg="gray20", fg="white", activebackground="gray20", activeforeground="white", selectcolor="gray20", font=("Noto", 10), bd=0, highlightthickness=0)
    chkbox_baslangic.pack(side=RIGHT)            

    root.mainloop()

if __name__ == '__main__':
    main()

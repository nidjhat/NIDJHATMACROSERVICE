import customtkinter as ctk
import webbrowser
import keyboard

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("NIDJHATMACROSERVICE")
app.geometry("900x600")

aktif = False
dil = "TR"

texts = {
    "TR": {
        "title": "NIDJHATMACROSERVICE",
        "start": "PROGRAMI CALISTIR",
        "stop": "PROGRAMI DURDUR",
        "status_on": "DURUM: AKTIF",
        "status_off": "DURUM: PASIF",
        "contact": "ILETISIM",
        "macros": "MAKROLAR",
        "insert": "INSERT = AKTIF/PASIF"
    },
    "EN": {
        "title": "NIDJHATMACROSERVICE",
        "start": "START PROGRAM",
        "stop": "STOP PROGRAM",
        "status_on": "STATUS: ACTIVE",
        "status_off": "STATUS: OFF",
        "contact": "CONTACT",
        "macros": "MACROS",
        "insert": "INSERT = ENABLE/DISABLE"
    },
    "RU": {
        "title": "NIDJHATMACROSERVICE",
        "start": "ЗАПУСТИТЬ ПРОГРАММУ",
        "stop": "ОСТАНОВИТЬ ПРОГРАММУ",
        "status_on": "СТАТУС: АКТИВЕН",
        "status_off": "СТАТУС: ВЫКЛ",
        "contact": "КОНТАКТЫ",
        "macros": "МАКРОСЫ",
        "insert": "INSERT = ВКЛ/ВЫКЛ"
    }
}

def dili_degistir(secim):
    global dil
    dil = secim
    yenile()

def yenile():
    title_label.configure(text=texts[dil]["title"])
    start_btn.configure(text=texts[dil]["start"])
    stop_btn.configure(text=texts[dil]["stop"])
    contact_label.configure(text=texts[dil]["contact"])
    macro_label.configure(text=texts[dil]["macros"])
    insert_label.configure(text=texts[dil]["insert"])

    if aktif:
        status_label.configure(text=texts[dil]["status_on"], text_color="green")
    else:
        status_label.configure(text=texts[dil]["status_off"], text_color="red")

def baslat():
    global aktif
    aktif = True
    yenile()

def durdur():
    global aktif
    aktif = False
    yenile()

def insert_toggle():
    global aktif
    aktif = not aktif
    yenile()

keyboard.add_hotkey("insert", insert_toggle)

title_label = ctk.CTkLabel(
    app,
    text="NIDJHATMACROSERVICE",
    font=("Arial", 34, "bold")
)
title_label.pack(pady=20)

lang_frame = ctk.CTkFrame(app)
lang_frame.pack(pady=10)

tr_btn = ctk.CTkButton(
    lang_frame,
    text="TURKCE",
    width=100,
    command=lambda: dili_degistir("TR")
)
tr_btn.grid(row=0, column=0, padx=5)

en_btn = ctk.CTkButton(
    lang_frame,
    text="ENGLISH",
    width=100,
    command=lambda: dili_degistir("EN")
)
en_btn.grid(row=0, column=1, padx=5)

ru_btn = ctk.CTkButton(
    lang_frame,
    text="РУССКИЙ",
    width=100,
    command=lambda: dili_degistir("RU")
)
ru_btn.grid(row=0, column=2, padx=5)

status_label = ctk.CTkLabel(
    app,
    text="DURUM: PASIF",
    font=("Arial", 22, "bold"),
    text_color="red"
)
status_label.pack(pady=10)

insert_label = ctk.CTkLabel(
    app,
    text="INSERT = AKTIF/PASIF",
    font=("Arial", 16)
)
insert_label.pack(pady=5)

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=20)

start_btn = ctk.CTkButton(
    btn_frame,
    text="PROGRAMI CALISTIR",
    width=220,
    height=45,
    command=baslat
)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = ctk.CTkButton(
    btn_frame,
    text="PROGRAMI DURDUR",
    width=220,
    height=45,
    fg_color="red",
    hover_color="#990000",
    command=durdur
)
stop_btn.grid(row=0, column=1, padx=10)

macro_label = ctk.CTkLabel(
    app,
    text="MAKROLAR",
    font=("Arial", 24, "bold")
)
macro_label.pack(pady=15)

macro_frame = ctk.CTkFrame(app)
macro_frame.pack(pady=10)
from tkinter import filedialog


macro_list = []

macro_box = ctk.CTkTextbox(app, width=500, height=180)
macro_box.pack(pady=10)
import_button = ctk.CTkButton(
    app,
    text="IMPORT MACRO",
    width=220,
    height=40,
    command=lambda: print("Yakinda")
)

import_button.pack(pady=15)

def import_macro():

    file = filedialog.askopenfilename(
        filetypes=[
            ("Macro Files", "*.amc *.mgn *.txt"),
            ("All Files", "*.*")
        ]
    )

    if file:
        macro_list.append(file)

        macro_box.delete("1.0", "end")

        for macro in macro_list:
            macro_box.insert("end", macro + "\n")

import_button = ctk.CTkButton(
    app,
    text="IMPORT MACRO",
    width=220,
    height=40,
    command=lambda: print("Makro import sistemi yakında")
)

import_button.pack(pady=15)

ctk.CTkButton(macro_frame, text="AMC").grid(row=0, column=0, padx=10, pady=10)
ctk.CTkButton(macro_frame, text="MGN").grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(macro_frame, text="AWM").grid(row=0, column=2, padx=10, pady=10)
ctk.CTkButton(macro_frame, text="AK47").grid(row=0, column=3, padx=10, pady=10)

contact_label = ctk.CTkLabel(
    app,
    text="ILETISIM",
    font=("Arial", 24, "bold")
)
contact_label.pack(pady=15)

social_frame = ctk.CTkFrame(app)
social_frame.pack(pady=10)

ctk.CTkButton(
    social_frame,
    text="WhatsApp",
    width=150,
    command=lambda: webbrowser.open("https://wa.me/994773892509")
).grid(row=0, column=0, padx=10, pady=10)

ctk.CTkButton(
    social_frame,
    text="TikTok",
    width=150,
    command=lambda: webbrowser.open("https://www.tiktok.com/@PHIRIYEFF99")
).grid(row=0, column=1, padx=10, pady=10)

ctk.CTkButton(
    social_frame,
    text="Instagram",
    width=150,
    command=lambda: webbrowser.open("https://www.instagram.com/nid.jhat")
).grid(row=0, column=2, padx=10, pady=10)

ctk.CTkButton(
    social_frame,
    text="YouTube",
    width=150,
    command=lambda: webbrowser.open("https://www.youtube.com/@nidjhat")
).grid(row=0, column=3, padx=10, pady=10)

yenile()

app.mainloop()

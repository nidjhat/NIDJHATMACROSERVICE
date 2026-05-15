import customtkinter as ctk
import webbrowser
import keyboard
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("NIDJHATMACROSERVICE")
app.geometry("900x600")

aktif = False
dil = "TR"
macro_list = []

texts = {
    "TR": {
        "title": "NIDJHATMACROSERVICE",
        "start": "PROGRAMI CALISTIR",
        "stop": "PROGRAMI DURDUR",
        "status_on": "DURUM: AKTIF",
        "status_off": "DURUM: PASIF",
        "macros": "MAKROLAR",
        "insert": "INSERT = AKTIF/PASIF",
        "import": "IMPORT MACRO"
    },
    "EN": {
        "title": "NIDJHATMACROSERVICE",
        "start": "START PROGRAM",
        "stop": "STOP PROGRAM",
        "status_on": "STATUS: ACTIVE",
        "status_off": "STATUS: PASSIVE",
        "macros": "MACROS",
        "insert": "INSERT = ACTIVE/PASSIVE",
        "import": "IMPORT MACRO"
    },
    "RU": {
        "title": "NIDJHATMACROSERVICE",
        "start": "ЗАПУСТИТЬ",
        "stop": "ОСТАНОВИТЬ",
        "status_on": "СТАТУС: АКТИВЕН",
        "status_off": "СТАТУС: ПАССИВЕН",
        "macros": "МАКРОСЫ",
        "insert": "INSERT = ВКЛ/ВЫКЛ",
        "import": "ИМПОРТ МАКРО"
    }
}

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

def dili_degistir(yeni_dil):
    global dil
    dil = yeni_dil

    title_label.configure(text=texts[dil]["title"])
    start_btn.configure(text=texts[dil]["start"])
    stop_btn.configure(text=texts[dil]["stop"])
    macro_title.configure(text=texts[dil]["macros"])
    insert_label.configure(text=texts[dil]["insert"])
    import_button.configure(text=texts[dil]["import"])

    if aktif:
        status_label.configure(text=texts[dil]["status_on"])
    else:
        status_label.configure(text=texts[dil]["status_off"])

def baslat():
    global aktif
    aktif = True
    status_label.configure(
        text=texts[dil]["status_on"],
        text_color="lime"
    )

def durdur():
    global aktif
    aktif = False
    status_label.configure(
        text=texts[dil]["status_off"],
        text_color="red"
    )

def insert_toggle():
    global aktif

    aktif = not aktif

    if aktif:
        status_label.configure(
            text=texts[dil]["status_on"],
            text_color="lime"
        )
    else:
        status_label.configure(
            text=texts[dil]["status_off"],
            text_color="red"
        )

keyboard.add_hotkey("insert", insert_toggle)

app.after(100, insert_toggle)

title_label = ctk.CTkLabel(
    app,
    text=texts[dil]["title"],
    font=("Arial", 36, "bold")
)
title_label.pack(pady=25)

lang_frame = ctk.CTkFrame(app, fg_color="transparent")
lang_frame.pack(pady=5)

tr_btn = ctk.CTkButton(
    lang_frame,
    text="TURKCE",
    width=90,
    command=lambda: dili_degistir("TR")
)
tr_btn.pack(side="left", padx=5)

en_btn = ctk.CTkButton(
    lang_frame,
    text="ENGLISH",
    width=90,
    command=lambda: dili_degistir("EN")
)
en_btn.pack(side="left", padx=5)

ru_btn = ctk.CTkButton(
    lang_frame,
    text="РУССКИЙ",
    width=90,
    command=lambda: dili_degistir("RU")
)
ru_btn.pack(side="left", padx=5)

status_label = ctk.CTkLabel(
    app,
    text=texts[dil]["status_off"],
    text_color="red",
    font=("Arial", 28, "bold")
)
status_label.pack(pady=15)

insert_label = ctk.CTkLabel(
    app,
    text=texts[dil]["insert"],
    font=("Arial", 20)
)
insert_label.pack(pady=5)

btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=20)

start_btn = ctk.CTkButton(
    btn_frame,
    text=texts[dil]["start"],
    width=220,
    height=45,
    command=baslat
)
start_btn.pack(side="left", padx=10)

stop_btn = ctk.CTkButton(
    btn_frame,
    text=texts[dil]["stop"],
    width=220,
    height=45,
    fg_color="red",
    hover_color="darkred",
    command=durdur
)
stop_btn.pack(side="left", padx=10)

macro_title = ctk.CTkLabel(
    app,
    text=texts[dil]["macros"],
    font=("Arial", 30, "bold")
)
macro_title.pack(pady=15)

macro_frame = ctk.CTkFrame(app)
macro_frame.pack(pady=10)

for text in ["AMC", "MGN", "AWM", "AK47"]:
    btn = ctk.CTkButton(
        macro_frame,
        text=text,
        width=120
    )
    btn.pack(side="left", padx=8, pady=8)

import_button = ctk.CTkButton(
    app,
    text=texts[dil]["import"],
    width=220,
    height=40,
    command=import_macro
)
import_button.pack(pady=15)

macro_box = ctk.CTkTextbox(
    app,
    width=500,
    height=120
)
macro_box.pack(pady=10)

app.mainloop()

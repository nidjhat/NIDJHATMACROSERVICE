import customtkinter as ctk
from tkinter import filedialog
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1100x650")
app.title("NIDJHATMACROSERVICE")

# ===== SOL MENU =====

left_frame = ctk.CTkFrame(app, width=220, corner_radius=0)
left_frame.pack(side="left", fill="y")

title = ctk.CTkLabel(
    left_frame,
    text="NIDJHAT\nMACRO\nSERVICE",
    font=("Arial", 28, "bold")
)
title.pack(pady=30)

play_btn = ctk.CTkButton(
    left_frame,
    text="▶ PLAY"
)
play_btn.pack(pady=10, padx=20)

stop_btn = ctk.CTkButton(
    left_frame,
    text="■ STOP",
    fg_color="red",
    hover_color="#990000"
)
stop_btn.pack(pady=10, padx=20)

# ===== IMPORT =====

macro_list = []

macro_listbox = ctk.CTkTextbox(
    app,
    width=650,
    height=500
)
macro_listbox.pack(pady=30, padx=30)

def import_macro():

    file = filedialog.askopenfilename(
        filetypes=[
            ("Macro Files", "*.amc *.mgn *.txt"),
            ("All Files", "*.*")
        ]
    )

    if file:

        name = os.path.basename(file)

        macro_list.append(name)

        macro_listbox.delete("1.0", "end")

        for macro in macro_list:
            macro_listbox.insert("end", f"{macro}\n")

import_btn = ctk.CTkButton(
    left_frame,
    text="＋ IMPORT MACRO",
    command=import_macro
)
import_btn.pack(pady=20, padx=20)

# ===== DIL =====

lang_menu = ctk.CTkOptionMenu(
    left_frame,
    values=["Turkce", "English", "Russian"]
)
lang_menu.pack(pady=20)

# ===== PROFILLER =====

profile_title = ctk.CTkLabel(
    left_frame,
    text="PROFILES",
    font=("Arial", 20, "bold")
)
profile_title.pack(pady=20)

aug_btn = ctk.CTkButton(
    left_frame,
    text="AUG"
)
aug_btn.pack(pady=5, padx=20)

sniper_btn = ctk.CTkButton(
    left_frame,
    text="SNIPER"
)
sniper_btn.pack(pady=5, padx=20)

drob_btn = ctk.CTkButton(
    left_frame,
    text="DROB"
)
drob_btn.pack(pady=5, padx=20)

# ===== CONTACT =====

contact_label = ctk.CTkLabel(
    left_frame,
    text="CONTACT",
    font=("Arial", 18, "bold")
)
contact_label.pack(pady=15)

wpp = ctk.CTkLabel(
    left_frame,
    text="WhatsApp: +994773892509"
)
wpp.pack()

tt = ctk.CTkLabel(
    left_frame,
    text="TikTok: @PHIRIYEFF99"
)
tt.pack()

ig = ctk.CTkLabel(
    left_frame,
    text="Instagram: @nid.jhat"
)
ig.pack()

yt = ctk.CTkLabel(
    left_frame,
    text="YouTube: @nidjhat"
)
yt.pack()

app.mainloop()

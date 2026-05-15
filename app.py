import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("1550x900")
app.title("NIDJHATMACROSERVICE")
app.configure(fg_color="#050505")

# ================= LEFT PANEL =================

left = ctk.CTkFrame(app, width=330, fg_color="#090909", corner_radius=15)
left.pack(side="left", fill="y", padx=10, pady=10)

logo = ctk.CTkLabel(
    left,
    text="NIDJHATMACROSERVICE",
    text_color="#ff1a1a",
    font=("Arial Black", 28)
)
logo.pack(pady=20)

subtitle = ctk.CTkLabel(
    left,
    text="MACRO ENGINE",
    text_color="gray",
    font=("Arial", 18)
)
subtitle.pack()

search = ctk.CTkEntry(
    left,
    placeholder_text="Makro ara...",
    width=270,
    height=40,
    fg_color="#111111",
    border_color="#ff1a1a"
)
search.pack(pady=20)

macros = [
    "AK47 RECOIL",
    "M4A1 RECOIL",
    "AUG RECOIL",
    "KRISS RECOIL",
    "RAPID FIRE",
    "SNIPER BREATH",
    "JUMP SHOT",
]

for m in macros:
    row = ctk.CTkFrame(left, fg_color="#101010", corner_radius=10)
    row.pack(fill="x", padx=15, pady=5)

    lbl = ctk.CTkLabel(
        row,
        text=m,
        font=("Arial", 18),
        text_color="white"
    )
    lbl.pack(side="left", padx=10, pady=10)

    sw = ctk.CTkSwitch(
        row,
        text="",
        progress_color="#ff1a1a",
        button_color="white"
    )
    sw.pack(side="right", padx=10)

profiles_title = ctk.CTkLabel(
    left,
    text="PROFILLER",
    text_color="#ff1a1a",
    font=("Arial Black", 22)
)
profiles_title.pack(pady=(25,10))

profile_box = ctk.CTkTextbox(
    left,
    width=270,
    height=180,
    fg_color="#0f0f0f",
    border_color="#ff1a1a",
    border_width=1
)
profile_box.pack(pady=10)

profile_box.insert("0.0", """
Point Blank
CS2
Valorant
PUBG
Genel
""")

# ================= CENTER =================

center = ctk.CTkFrame(app, fg_color="#070707", corner_radius=15)
center.pack(side="left", fill="both", expand=True, padx=5, pady=10)

# TOP MENU

topmenu = ctk.CTkFrame(center, fg_color="transparent")
topmenu.pack(fill="x", pady=10)

tabs = ["MACRO", "RAPID FIRE", "AYARLAR", "PROFILLER", "ARACLAR"]

for t in tabs:
    btn = ctk.CTkButton(
        topmenu,
        text=t,
        width=180,
        height=60,
        fg_color="#101010",
        hover_color="#ff1a1a",
        border_color="#ff1a1a",
        border_width=1,
        font=("Arial Black", 18)
    )
    btn.pack(side="left", padx=5)

# TITLE

title = ctk.CTkLabel(
    center,
    text="AK47 RECOIL",
    text_color="#ff1a1a",
    font=("Arial Black", 32)
)
title.pack(anchor="w", padx=20, pady=15)

# BUTTONS

buttons = ctk.CTkFrame(center, fg_color="transparent")
buttons.pack(anchor="w", padx=20)

play = ctk.CTkButton(
    buttons,
    text="▶ PLAY",
    width=180,
    height=60,
    fg_color="#ff1a1a",
    hover_color="#cc0000",
    font=("Arial Black", 20)
)
play.pack(side="left", padx=10)

stop = ctk.CTkButton(
    buttons,
    text="■ STOP",
    width=180,
    height=60,
    fg_color="#151515",
    hover_color="#333333",
    font=("Arial Black", 20)
)
stop.pack(side="left", padx=10)

rec = ctk.CTkButton(
    buttons,
    text="● REC",
    width=180,
    height=60,
    fg_color="#990000",
    hover_color="#cc0000",
    font=("Arial Black", 20)
)
rec.pack(side="left", padx=10)

# TABLE AREA

table = ctk.CTkTextbox(
    center,
    fg_color="#090909",
    border_color="#ff1a1a",
    border_width=1,
    font=("Consolas", 17)
)
table.pack(fill="both", expand=True, padx=20, pady=20)

table.insert("0.0", """
#   ACTION             DETAIL          DELAY

1   Mouse Move         X:0  Y:-5      15ms
2   Wait               ---            15ms
3   Mouse Move         X:0  Y:-6      15ms
4   Wait               ---            15ms
5   Mouse Move         X:0  Y:-7      15ms
6   Wait               ---            15ms
7   Mouse Move         X:0  Y:-8      15ms
""")

# ================= RIGHT PANEL =================

right = ctk.CTkFrame(app, width=320, fg_color="#090909", corner_radius=15)
right.pack(side="right", fill="y", padx=10, pady=10)

lang = ctk.CTkComboBox(
    right,
    values=["Türkçe", "English", "Русский"],
    width=220,
    height=45,
    fg_color="#111111",
    border_color="#ff1a1a",
    button_color="#ff1a1a"
)
lang.pack(pady=25)

settings_title = ctk.CTkLabel(
    right,
    text="MAKRO AYARLARI",
    text_color="#ff1a1a",
    font=("Arial Black", 24)
)
settings_title.pack(pady=10)

loop = ctk.CTkCheckBox(
    right,
    text="Surekli Tekrar",
    text_color="white",
    checkbox_width=25,
    checkbox_height=25
)
loop.pack(anchor="w", padx=30, pady=15)

slider = ctk.CTkSlider(
    right,
    from_=1,
    to=100,
    width=220,
    progress_color="#ff1a1a",
    button_color="white"
)
slider.pack(pady=20)

activate = ctk.CTkButton(
    right,
    text="AKTIF ET",
    width=220,
    height=55,
    fg_color="#ff1a1a",
    hover_color="#cc0000",
    font=("Arial Black", 18)
)
activate.pack(pady=10)

disable = ctk.CTkButton(
    right,
    text="PASIF ET",
    width=220,
    height=55,
    fg_color="#151515",
    hover_color="#333333",
    font=("Arial Black", 18)
)
disable.pack()

# CONTACTS

contact_title = ctk.CTkLabel(
    right,
    text="ILETISIM",
    text_color="#ff1a1a",
    font=("Arial Black", 24)
)
contact_title.pack(pady=(40,10))

contacts = [
    "WHATSAPP",
    "YOUTUBE",
    "TELEGRAM",
    "DISCORD",
    "WEBSITE"
]

for c in contacts:
    b = ctk.CTkButton(
        right,
        text=c,
        width=220,
        height=55,
        fg_color="#101010",
        hover_color="#ff1a1a",
        border_color="#ff1a1a",
        border_width=1,
        font=("Arial Black", 16)
    )
    b.pack(pady=8)

footer = ctk.CTkLabel(
    app,
    text="NIDJHATMACROSERVICE v1.0.0",
    text_color="#00ff66",
    font=("Arial", 16)
)
footer.place(x=20, y=870)

app.mainloop()

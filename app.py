import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("1500x900")
app.title("NIDJHATMACROSERVICE")

# ================= MAIN =================

main = ctk.CTkFrame(app, fg_color="#050505")
main.pack(fill="both", expand=True)

# ================= LEFT SIDEBAR =================

left = ctk.CTkFrame(main, width=320, fg_color="#0b0b0b", corner_radius=0)
left.pack(side="left", fill="y")

logo = ctk.CTkLabel(
    left,
    text="NIDJHAT\nMACRO\nSERVICE",
    text_color="#ff1a1a",
    font=("Arial Black", 34)
)
logo.pack(pady=30)

search = ctk.CTkEntry(
    left,
    placeholder_text="Makro ara...",
    width=260,
    height=40
)
search.pack(pady=10)

macro_list = [
    "AK47 RECOIL",
    "M4A1 RECOIL",
    "AUG RECOIL",
    "KRISS RECOIL",
    "RAPID FIRE",
    "SNIPER BREATH",
]

for macro in macro_list:
    item = ctk.CTkFrame(left, fg_color="#111111")
    item.pack(fill="x", padx=20, pady=5)

    lbl = ctk.CTkLabel(
        item,
        text=macro,
        text_color="white",
        font=("Arial", 18)
    )
    lbl.pack(side="left", padx=10, pady=10)

    sw = ctk.CTkSwitch(item, text="")
    sw.pack(side="right", padx=10)

# ================= CENTER =================

center = ctk.CTkFrame(main, fg_color="#070707")
center.pack(side="left", fill="both", expand=True, padx=10, pady=10)

title = ctk.CTkLabel(
    center,
    text="AK47 RECOIL",
    text_color="#ff1a1a",
    font=("Arial Black", 28)
)
title.pack(anchor="w", padx=20, pady=20)

btn_frame = ctk.CTkFrame(center, fg_color="transparent")
btn_frame.pack(anchor="w", padx=20)

play_btn = ctk.CTkButton(
    btn_frame,
    text="▶ PLAY",
    width=180,
    height=50,
    fg_color="#ff1a1a",
    hover_color="#cc0000",
    font=("Arial Black", 18)
)
play_btn.pack(side="left", padx=10)

stop_btn = ctk.CTkButton(
    btn_frame,
    text="■ STOP",
    width=180,
    height=50,
    fg_color="#1a1a1a",
    hover_color="#333333",
    font=("Arial Black", 18)
)
stop_btn.pack(side="left", padx=10)

rec_btn = ctk.CTkButton(
    btn_frame,
    text="● REC",
    width=180,
    height=50,
    fg_color="#990000",
    hover_color="#cc0000",
    font=("Arial Black", 18)
)
rec_btn.pack(side="left", padx=10)

textbox = ctk.CTkTextbox(
    center,
    fg_color="#0d0d0d",
    border_color="#ff1a1a",
    border_width=1,
    font=("Consolas", 16)
)
textbox.pack(fill="both", expand=True, padx=20, pady=20)

sample = """
#   ACTION              DETAIL          DELAY

1   Mouse Move          X:0 Y:-5       15ms
2   Wait                ---            15ms
3   Mouse Move          X:0 Y:-6       15ms
4   Wait                ---            15ms
5   Mouse Move          X:0 Y:-7       15ms
"""

textbox.insert("0.0", sample)

# ================= RIGHT PANEL =================

right = ctk.CTkFrame(main, width=320, fg_color="#0b0b0b")
right.pack(side="right", fill="y")

lang = ctk.CTkComboBox(
    right,
    values=["Turkce", "English", "Русский"],
    width=220,
    height=40
)
lang.pack(pady=30)

settings_title = ctk.CTkLabel(
    right,
    text="MAKRO AYARLARI",
    text_color="#ff1a1a",
    font=("Arial Black", 24)
)
settings_title.pack(pady=10)

loop_check = ctk.CTkCheckBox(
    right,
    text="Surekli Tekrar",
    text_color="white"
)
loop_check.pack(anchor="w", padx=30, pady=10)

delay = ctk.CTkSlider(
    right,
    from_=1,
    to=100,
    width=220,
    progress_color="#ff1a1a"
)
delay.pack(pady=20)

activate_btn = ctk.CTkButton(
    right,
    text="AKTIF ET",
    width=220,
    height=50,
    fg_color="#ff1a1a",
    hover_color="#cc0000",
    font=("Arial Black", 18)
)
activate_btn.pack(pady=20)

disable_btn = ctk.CTkButton(
    right,
    text="PASIF ET",
    width=220,
    height=50,
    fg_color="#1a1a1a",
    hover_color="#333333",
    font=("Arial Black", 18)
)
disable_btn.pack()

# ================= FOOTER =================

footer = ctk.CTkLabel(
    app,
    text="NIDJHATMACROSERVICE v1.0.0",
    text_color="#00ff66",
    font=("Arial", 16)
)
footer.place(x=20, y=865)

app.mainloop()

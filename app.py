import customtkinter as ctk

print("PROGRAM BASLADI")

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x500")
app.title("NIDJHATMACROSERVICE")

label = ctk.CTkLabel(
    app,
    text="NIDJHATMACROSERVICE",
    font=("Arial", 30, "bold")
)
label.pack(pady=40)

button = ctk.CTkButton(
    app,
    text="PROGRAM CALISIYOR"
)
button.pack(pady=20)

app.mainloop()

input("ENTER BAS")

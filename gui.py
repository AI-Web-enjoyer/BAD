def main():
    import tkinter as tk
    from UniqueLetter import get_unique_letter
    import customtkinter as ctk

    def button_func():
        text = main_textbox.get(1.0, "end-1c")
        var.set(get_unique_letter(text))

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    window = ctk.CTk()
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.title("Uniqueness")
    window.geometry("500x400")

    main_label = ctk.CTkLabel(master=window,
                              text="Type any text to get first unique symbol",
                              font=('Arial', 18))
    main_label.grid(pady=25, row=0, column=0)

    var = tk.StringVar(window, "Your answer will be here")

    main_textbox = tk.Text(window, highlightthickness=0, width=1, height=5, padx=10, pady=10)
    main_textbox.grid(row=1, column=0, sticky="nsew", padx=100)

    ctk_textbox_scrollbar = ctk.CTkScrollbar(window, command=main_textbox.yview)
    ctk_textbox_scrollbar.grid(row=1, column=1, sticky="ns")
    main_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

    answer_label = ctk.CTkLabel(master=window,  textvariable=var, font=("Arial", 20))
    answer_label.grid()

    main_button = ctk.CTkButton(master=window, text="Find unique symbol", font=("Arial", 16), command=button_func)
    main_button.grid(pady=20)

    window.mainloop()

#Code von ChatGPT https://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622
import tkinter as tk
from tkinter import messagebox, filedialog

# Sprachdefinition mit Anzeige-Label + Flagge
languages = {
    "de": {
        "flag": "🇩🇪 Deutsch",
        "code": "de",
        "title": "TextEditor Alpha 0.3",
        "about_title": "Über",
        "about_message": "TextEditor\nAlpha 0.3\n(c) 2025 Jan Löwen\nhttps://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622",
        "file_menu": "Datei",
        "open_item": "Öffnen...",
        "save_item": "Speichern unter...",
        "exit_item": "Beenden",
        "help_menu": "Hilfe",
        "about_item": "Über"
    },
    "en": {
        "flag": "🇬🇧 English",
        "code": "en",
        "title": "TextEditor Alpha 0.3",
        "about_title": "About",
        "about_message": "TextEditor\nAlpha 0.3\n(c) 2025 Jan Loewen\nhttps://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622",
        "file_menu": "File",
        "open_item": "Open...",
        "save_item": "Save As...",
        "exit_item": "Exit",
        "help_menu": "Help",
        "about_item": "About"
    }
}

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.lang = "de"

        # === Modernes Layout ===
        root.title("Einfacher Texteditor")
        root.configure(bg="#f0f0f0")
        self.header = tk.Frame(root, bg="#ddd")
        self.header.pack(side=tk.TOP, fill=tk.X)

        self.lang_var = tk.StringVar(value=languages[self.lang]["flag"])
        self.lang_menu = tk.OptionMenu(self.header, self.lang_var,
                                       *[languages[k]["flag"] for k in languages],
                                       command=self.set_language_by_flag)
        self.lang_menu.configure(bg="#fff", relief=tk.RAISED)
        self.lang_menu.pack(side=tk.RIGHT, padx=10, pady=8)

        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)

        # === Textfeld ===
        self.text = tk.Text(root, font=("Segoe UI", 12), wrap=tk.WORD, bg="white", fg="black")
        self.text.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))

        self.update_language()

    def set_language_by_flag(self, selected_flag_label):
        for code, data in languages.items():
            if data["flag"] == selected_flag_label:
                self.lang = code
                break
        self.update_language()

    def update_language(self):
        t = languages[self.lang]
        self.root.title(t["title"])
        self.lang_var.set(t["flag"])

        # Menü neu erstellen
        self.menubar.delete(0, tk.END)

        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label=t["open_item"], command=self.open_file)
        file_menu.add_command(label=t["save_item"], command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label=t["exit_item"], command=self.root.quit)
        self.menubar.add_cascade(label=t["file_menu"], menu=file_menu)

        help_menu = tk.Menu(self.menubar, tearoff=0)
        help_menu.add_command(label=t["about_item"], command=self.show_about)
        self.menubar.add_cascade(label=t["help_menu"], menu=help_menu)

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Textdateien", "*.txt")])
        if filepath:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, content)

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Textdateien", "*.txt")])
        if filepath:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END).strip())

    def show_about(self):
        t = languages[self.lang]
        messagebox.showinfo(t["about_title"], t["about_message"])


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = TextEditor(root)
    root.mainloop()

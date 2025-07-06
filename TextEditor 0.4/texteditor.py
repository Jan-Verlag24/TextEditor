#Code von ChatGPT https://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622
import tkinter as tk
from tkinter import messagebox, filedialog, font
from reportlab.pdfgen import canvas

# Sprachdefinition
languages = {
    "de": {
        "flag": "🇩🇪 Deutsch",
        "code": "de",
        "title": "TextEditor Alpha 0.4",
        "about_title": "Über",
        "about_message": "TextEditor\nAlpha 0.4\n(c) 2025 Jan Löwen\nhttps://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622",
        "file_menu": "Datei",
        "open_item": "Öffnen...",
        "save_item": "Speichern unter...",
        "export_pdf": "Exportieren als PDF",
        "export_rtf": "Exportieren als RTF",
        "exit_item": "Beenden",
        "help_menu": "Hilfe",
        "about_item": "Über"
    },
    "en": {
        "flag": "🇬🇧 English",
        "code": "en",
        "title": "TextEditor Alpha 0.4",
        "about_title": "About",
        "about_message": "TextEditor\nAlpha 0.4\n(c) 2025 Jan Loewen\nhttps://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622",
        "file_menu": "File",
        "open_item": "Open...",
        "save_item": "Save As...",
        "export_pdf": "Export as PDF",
        "export_rtf": "Export as RTF",
        "exit_item": "Exit",
        "help_menu": "Help",
        "about_item": "About"
    }
}

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.lang = "de"
        self.current_font = "Arial"
        self.current_size = 12

        # === Layout: Header mit Sprache & Format ===
        self.header = tk.Frame(root, bg="#eee")
        self.header.pack(side=tk.TOP, fill=tk.X)

        # Sprache
        self.lang_var = tk.StringVar(value=languages[self.lang]["flag"])
        self.lang_menu = tk.OptionMenu(self.header, self.lang_var,
                                       *[languages[k]["flag"] for k in languages],
                                       command=self.set_language_by_flag)
        self.lang_menu.pack(side=tk.RIGHT, padx=5, pady=5)

        # Schriftart-Auswahl
        fonts = sorted(font.families())
        self.font_var = tk.StringVar(value=self.current_font)
        self.font_menu = tk.OptionMenu(self.header, self.font_var, *fonts, command=self.change_font)
        self.font_menu.pack(side=tk.LEFT, padx=5, pady=5)

        # Schriftgröße
        self.size_var = tk.IntVar(value=self.current_size)
        self.size_spin = tk.Spinbox(self.header, from_=8, to=72, width=4, textvariable=self.size_var, command=self.change_font)
        self.size_spin.pack(side=tk.LEFT, padx=5)

        # Formatbuttons
        self.bold_btn = tk.Button(self.header, text="B", command=self.toggle_bold, font=("Arial", 10, "bold"))
        self.bold_btn.pack(side=tk.LEFT, padx=2)
        self.italic_btn = tk.Button(self.header, text="I", command=self.toggle_italic, font=("Arial", 10, "italic"))
        self.italic_btn.pack(side=tk.LEFT, padx=2)
        self.underline_btn = tk.Button(self.header, text="U", command=self.toggle_underline, font=("Arial", 10, "underline"))
        self.underline_btn.pack(side=tk.LEFT, padx=2)

        # === Menü ===
        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)

        # === Textfeld ===
        self.text = tk.Text(root, wrap=tk.WORD)
        self.text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Schriftformat initial setzen
        self.set_font()

        self.update_language()

    def set_language_by_flag(self, flag):
        for code, data in languages.items():
            if data["flag"] == flag:
                self.lang = code
                break
        self.update_language()

    def update_language(self):
        t = languages[self.lang]
        self.root.title(t["title"])
        self.lang_var.set(t["flag"])

        # Menü
        self.menubar.delete(0, tk.END)

        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label=t["open_item"], command=self.open_file)
        file_menu.add_command(label=t["save_item"], command=self.save_file)
        file_menu.add_command(label=t["export_pdf"], command=self.export_pdf)
        file_menu.add_command(label=t["export_rtf"], command=self.export_rtf)
        file_menu.add_separator()
        file_menu.add_command(label=t["exit_item"], command=self.root.quit)
        self.menubar.add_cascade(label=t["file_menu"], menu=file_menu)

        help_menu = tk.Menu(self.menubar, tearoff=0)
        help_menu.add_command(label=t["about_item"], command=self.show_about)
        self.menubar.add_cascade(label=t["help_menu"], menu=help_menu)

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filepath:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, content)

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])
        if filepath:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END).strip())

    def export_pdf(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")])
        if filepath:
            c = canvas.Canvas(filepath)
            textobject = c.beginText(40, 800)
            textobject.setFont(self.current_font, self.current_size)
            content = self.text.get("1.0", tk.END).splitlines()
            for line in content:
                textobject.textLine(line)
            c.drawText(textobject)
            c.save()
            messagebox.showinfo("Export", "PDF erfolgreich gespeichert.")

    def export_rtf(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".rtf",
                                                 filetypes=[("RTF files", "*.rtf")])
        if filepath:
            content = self.text.get("1.0", tk.END).strip()
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(r"{\rtf1\ansi\n" + content.replace("\n", r"\line ") + r"}")
            messagebox.showinfo("Export", "RTF erfolgreich gespeichert.")

    def show_about(self):
        t = languages[self.lang]
        messagebox.showinfo(t["about_title"], t["about_message"])

    def change_font(self, *_):
        self.set_font()

    def set_font(self):
        self.current_font = self.font_var.get()
        self.current_size = self.size_var.get()
        font_config = (self.current_font, self.current_size)
        self.text.configure(font=font_config)

    def toggle_bold(self):
        current_tags = self.text.tag_names("sel.first")
        if "bold" in current_tags:
            self.text.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text.tag_add("bold", "sel.first", "sel.last")
            self.text.tag_configure("bold", font=(self.current_font, self.current_size, "bold"))

    def toggle_italic(self):
        current_tags = self.text.tag_names("sel.first")
        if "italic" in current_tags:
            self.text.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.text.tag_add("italic", "sel.first", "sel.last")
            self.text.tag_configure("italic", font=(self.current_font, self.current_size, "italic"))

    def toggle_underline(self):
        current_tags = self.text.tag_names("sel.first")
        if "underline" in current_tags:
            self.text.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.text.tag_add("underline", "sel.first", "sel.last")
            self.text.tag_configure("underline", font=(self.current_font, self.current_size, "underline"))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x600")
    app = TextEditor(root)
    root.mainloop()

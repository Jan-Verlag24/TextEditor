#Code von ChatGPT https://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622
# import tkinter as tk
# from tkinter import messagebox, filedialog, font
# from reportlab.pdfgen import canvas

        # changelog = (
        #     "📝 Update-Log\n"
        #     "\n"
        #     "Version 1.0.0 – Juli 2025\n"
        #     "- Neuer moderner Texteditor\n"
        #     "- Mehrsprachigkeit (🇩🇪/🇬🇧)\n"
        #     "- Export als PDF & RTF\n"
        #     "- Schriftart, Größe, Format (B/I/U)\n"
        #     "- Farbwahl für Text\n"
        #     "- Farbpalette dauerhaft sichtbar\n"
        #     "- Update-Log\n"
        #     "- Sicher: Keine Viren enthalten\n"
        # )

import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, ttk, scrolledtext
from tkinter.font import Font
from fpdf import FPDF
import os

class TextEditor:
    def __init__(self, root):
        self.root = root

        self.dark_mode = False

        self.language = "de"
        self.translations = {
            "de": {
                "app_title": "TextEditor Alpha 0.5",
                "file_menu": "Datei",
                "open_item": "Öffnen",
                "save_item": "Speichern",
                "export_rtf_html": "Exportieren als RTF/HTML/PDF",
                "exit_item": "Beenden",
                "help_menu": "Hilfe",
                "about_item": "Über",
                "changelog_item": "Änderungen",
                "about_text": "TextEditor\nAlpha 0.5\n(c) 2025 Jan Löwen\nhttps://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622\n\nHallo und willkommen in diesem Editor. Dies ist ein Test-Text, um zu zeigen, was in diesem Editor möglich ist!\nAktuelle Features:\n1. Verschiedene Fonts\n2. Schriftgöße\n3. Formatierungen (Fett, Kursiv und Unterstrichen)\n4. Sprachen (Deutsch & Englisch)\n5. Dateien öffnen (TXT)\n6. Speichern (TXT)\n7. Exportieren (RTF & PDF)\n\nGeplante Features:\n1. Schriftfarbe\n2. Weitere Sprachen (Französisch, Niederländisch und mehr)\n3. Uhrzeit und Datum einfügen\n4. weitere Funktionen, wie in Microsoft Editor ;)\n5. Speichern mit dem Befehl (STRG + S)\n6. Öffnen mit dem Befehl (STRG + O)\n7. Uhrzeit und Datum mit Befehl (F5) einfügen\n8. Mehrere Tabs\n9. Und weitere Tolle Funktionen\n\nDieses Programm enthält keine Viren.",
                "changelog_title": "Update-Log",
                "changelog": "📝 Update-Log\n\nVersion 0.5 – Juli 2025\n- PDF-Export\n- Dark Mode\n- Sprachunterstützung: 🇫🇷 Französisch, 🇳🇱 Niederländisch\n- Hilfe-Menü\n"
            },
            "en": {
                "app_title": "TextEditor Alpha 0.5",
                "file_menu": "File",
                "open_item": "Open",
                "save_item": "Save",
                "export_rtf_html": "Export as RTF/HTML/PDF",
                "exit_item": "Exit",
                "help_menu": "Help",
                "about_item": "About",
                "changelog_item": "Changelog",
                "about_text": "TextEditor\nAlpha 0.5\n(c) 2025 Jan Loewen\nhttps://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622\n\nHello and welcome to this editor. This is an exmaple-text for showing, what is possible with this editor!\nFeatures Added:\n1. Different Fonts\n2. Font Size\n3. Text Formatting (Bold, Italic and Underscore)\n4. Languages (German & English)\n5. Open File (TXT)\n6. Save as (TXT)\n7. Export (RTF & PDF)\n\nPlanned Features:\n1. Font Color\n2. More Languages (French, Dutch and more)\n3. Adding Time and Date\n4. More Functions, like in Microsoft Editor ;)\n5. Save with CONTROL + S\n6. Open with CONTROL + O\n7. Adding Time and Date with (F5)\n8. Multiple Tabs\n9. And many more functions to be added\n\nThis program contains no viruses.",
                "changelog_title": "Changelog",
                "changelog": "📝 Changelog\n\nVersion 0.5 – July 2025\n- PDF export\n- Dark mode\n- Language support: 🇫🇷 French, 🇳🇱 Dutch\n- Help menu\n"
            },
            "fr": {
                "app_title": "TextÉditeur Alpha 0.5",
                "file_menu": "Fichier",
                "open_item": "Ouvrir",
                "save_item": "Enregistrer",
                "export_rtf_html": "Exporter en RTF/HTML/PDF",
                "exit_item": "Quitter",
                "help_menu": "Aide",
                "about_item": "À propos",
                "changelog_item": "Journal",
                "about_text": "TextÉditeur\nVersion 0.5\n(c) 2025 Jan Loewen\n\nCe programme ne contient aucun virus.",
                "changelog_title": "Journal des modifications",
                "changelog": "📝 Journal des modifications\n\nVersion 0.5 – Juillet 2025\n- Exportation PDF\n- Mode sombre\n- Prise en charge des langues : 🇫🇷 Français, 🇳🇱 Néerlandais\n- Menu d'aide\n"
            },
            "nl": {
                "app_title": "Teksteditor Alpha 0.5",
                "file_menu": "Bestand",
                "open_item": "Openen",
                "save_item": "Opslaan",
                "export_rtf_html": "Exporteren als RTF/HTML/PDF",
                "exit_item": "Afsluiten",
                "help_menu": "Hulp",
                "about_item": "Over",
                "changelog_item": "Wijzigingen",
                "about_text": "Teksteditor\nVersie 0.5\n(c) 2025 Jan Loewen\n\nDit programma bevat geen virussen.",
                "changelog_title": "Wijzigingslogboek",
                "changelog": "📝 Wijzigingslogboek\n\nVersie 0.5 – Juli 2025\n- PDF-export\n- Donkere modus\n- Ondersteuning voor talen: 🇫🇷 Frans, 🇳🇱 Nederlands\n- Help-menu\n"
            }
        }

        self.root.title(self.translations[self.language]["app_title"])

        self.text = tk.Text(root, wrap="word", undo=True)
        self.text.pack(expand=1, fill="both")

        self.header = tk.Frame(root)
        self.header.pack(fill="x")

        self.bold_btn = tk.Button(self.header, text="B", command=self.make_bold)
        self.bold_btn.pack(side="left")

        self.italic_btn = tk.Button(self.header, text="I", command=self.make_italic)
        self.italic_btn.pack(side="left")

        self.underline_btn = tk.Button(self.header, text="U", command=self.make_underline)
        self.underline_btn.pack(side="left")

        self.color_btn = tk.Button(self.header, text="🖍️", command=self.choose_color)
        self.color_btn.pack(side="left", padx=2)

        self.font_family = ttk.Combobox(self.header, values=["Arial", "Courier", "Times New Roman"])
        self.font_family.set("Arial")
        self.font_family.pack(side="left")
        self.font_family.bind("<<ComboboxSelected>>", self.change_font)

        self.font_size = ttk.Combobox(self.header, values=[str(s) for s in range(8, 32)])
        self.font_size.set("12")
        self.font_size.pack(side="left")
        self.font_size.bind("<<ComboboxSelected>>", self.change_font)

        self.language_btn = tk.Menubutton(self.header, text="🌐 Sprache")
        self.language_menu = tk.Menu(self.language_btn, tearoff=0)
        self.language_menu.add_command(label="🇩🇪 Deutsch", command=lambda: self.set_language("de"))
        self.language_menu.add_command(label="🇬🇧 English", command=lambda: self.set_language("en"))
        self.language_menu.add_command(label="🇫🇷 Français", command=lambda: self.set_language("fr"))
        self.language_menu.add_command(label="🇳🇱 Nederlands", command=lambda: self.set_language("nl"))
        self.language_btn.config(menu=self.language_menu)
        self.language_btn.pack(side="left", padx=6)

        self.darkmode_btn = tk.Button(self.header, text="🌙", command=self.toggle_dark_mode)
        self.darkmode_btn.pack(side="left")

        self.create_color_palette()

        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)

        self.update_language()

        self.statusbar = tk.Label(root, text="Sicher: Keine Viren enthalten ✔", bg="#ddd", anchor="w")
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_language(self, lang):
        self.language = lang
        self.update_language()

    def update_language(self):
        t = self.translations[self.language]
        self.root.title(t["app_title"])
        self.menubar.delete(0, "end")

        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label=t["open_item"], command=self.open_file)
        file_menu.add_command(label=t["save_item"], command=self.save_file)
        file_menu.add_command(label=t["export_rtf_html"], command=self.export_rtf_html)
        file_menu.add_separator()
        file_menu.add_command(label=t["exit_item"], command=self.root.quit)
        self.menubar.add_cascade(label=t["file_menu"], menu=file_menu)

        help_menu = tk.Menu(self.menubar, tearoff=0)
        help_menu.add_command(label=t["about_item"], command=self.show_about)
        help_menu.add_command(label=t["changelog_item"], command=self.show_changelog_window)
        self.menubar.add_cascade(label=t["help_menu"], menu=help_menu)

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path, "r", encoding="utf-8") as f:
                self.text.delete("1.0", "end")
                self.text.insert("1.0", f.read())

    def save_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", "end-1c"))

    def export_rtf_html(self):
        filetypes = [("Rich Text Format", "*.rtf"), ("HTML-Datei", "*.html"), ("PDF-Datei", "*.pdf")]
        file_path = filedialog.asksaveasfilename(defaultextension=".rtf", filetypes=filetypes)
        if not file_path:
            return

        content = self.text.get("1.0", "end-1c")

        if file_path.endswith(".rtf"):
            rtf = r"{\\rtf1\\ansi\n" + content.replace("\n", r"\\par\n") + r"}"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(rtf)

        elif file_path.endswith(".html"):
            html = "<html><body><p>" + content.replace("\n", "<br>") + "</p></body></html>"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html)

        elif file_path.endswith(".pdf"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Helvetica", size=12)
            for line in content.splitlines():
                pdf.cell(200, 10, txt=line, ln=True)
            pdf.output(file_path)
            pdf.add_font('Arial', '', 'arial.ttf', uni=True)
            pdf.set_font('Arial', size=12)


    def show_about(self):
        t = self.translations[self.language]
        messagebox.showinfo(t["about_item"], t["about_text"])

    def show_changelog_window(self):
        t = self.translations[self.language]
        log_window = tk.Toplevel(self.root)
        log_window.title(t["changelog_title"])
        log_window.geometry("400x300")

        text = scrolledtext.ScrolledText(log_window, wrap=tk.WORD, font=("Arial", 10))
        text.pack(expand=True, fill="both")

        text.insert("1.0", t["changelog"])
        text.config(state=tk.DISABLED)

    def make_bold(self):
        self.toggle_tag("bold", Font(weight="bold"))

    def make_italic(self):
        self.toggle_tag("italic", Font(slant="italic"))

    def make_underline(self):
        self.toggle_tag("underline", Font(underline=1))

    def toggle_tag(self, tag, font):
        current_tags = self.text.tag_names("sel.first")
        if tag in current_tags:
            self.text.tag_remove(tag, "sel.first", "sel.last")
        else:
            self.text.tag_add(tag, "sel.first", "sel.last")
            self.text.tag_configure(tag, font=font)

    def change_font(self, event=None):
        family = self.font_family.get()
        size = int(self.font_size.get())
        self.text.configure(font=(family, size))

    def choose_color(self):
        color = colorchooser.askcolor(title="Farbe wählen")[1]
        if color:
            self.text.tag_add("color", "sel.first", "sel.last")
            self.text.tag_configure("color", foreground=color)

    def create_color_palette(self):
        colors = ["black", "red", "green", "blue", "orange", "purple", "brown", "gray"]
        palette = tk.Frame(self.header)
        for color in colors:
            btn = tk.Button(palette, bg=color, width=2, command=lambda c=color: self.apply_color(c))
            btn.pack(side=tk.LEFT, padx=1)
        palette.pack(side=tk.LEFT, padx=4)

    def apply_color(self, color):
        try:
            self.text.tag_add("color", "sel.first", "sel.last")
            self.text.tag_configure("color", foreground=color)
        except tk.TclError:
            pass

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        bg = "#1e1e1e" if self.dark_mode else "white"
        fg = "#dcdcdc" if self.dark_mode else "black"
        self.text.config(bg=bg, fg=fg, insertbackground=fg)
        self.statusbar.config(bg="#444" if self.dark_mode else "#ddd", fg=fg)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

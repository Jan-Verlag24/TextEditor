#Code von ChatGPT https://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import messagebox

def open_file():
    filepath = askopenfilename()
    if filepath:
        with open(filepath, "r", encoding="utf-8") as f:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, f.read())

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt",
                                  filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text_editor.get(1.0, tk.END))

def show_about():
    messagebox.showinfo("Über", "TextEditor\nAlpha 0.1\n(c) 2025 Jan Löwen\nhttps://chatgpt.com/c/686a7729-8748-8012-b9f6-b9474125a622")

root = tk.Tk()
root.title("TextEditor Alpha 0.1")

# Textfeld
text_editor = tk.Text(root, wrap="word")
text_editor.pack(expand=1, fill="both")

# Menüleiste
menu = tk.Menu(root)
root.config(menu=menu)

# Datei-Menü
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Datei", menu=file_menu)
file_menu.add_command(label="Öffnen", command=open_file)
file_menu.add_command(label="Speichern", command=save_file)

# Hilfe-Menü mit "Über"
help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Hilfe", menu=help_menu)
help_menu.add_command(label="Über", command=show_about)

root.mainloop()

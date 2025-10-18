import os
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import Toplevel
from tkinter import Canvas
from tkinter import StringVar, BooleanVar
from tkinter import scrolledtext
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import font as tkfont
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import Toplevel
from tkinter import Canvas
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import Toplevel
from tkinter import Canvas
from tkinter import StringVar, BooleanVar
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext

from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext

from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext

from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext

import webbrowser
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox

# Eldessouky Labels - استخدامات الأدوية

TEMPLATES_FILE = "templates.json"

def load_templates():
    if os.path.exists(TEMPLATES_FILE):
        with open(TEMPLATES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [
        {"name": "3 مرات قبل الأكل", "text": "خذ الدواء 3 مرات قبل الأكل"},
        {"name": "مرتين بعد الأكل", "text": "خذ الدواء مرتين بعد الأكل"},
        {"name": "مرة واحدة يوميًا", "text": "خذ الدواء مرة واحدة يوميًا"},
    ]

def save_templates(templates):
    with open(TEMPLATES_FILE, "w", encoding="utf-8") as f:
        json.dump(templates, f, ensure_ascii=False, indent=2)

class LabelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eldessouky Labels - طباعة استخدامات")
        self.geometry("500x400")
        self.configure(bg="#e6f0ff")

        self.templates = load_templates()

        tk.Label(self, text="📋 قائمة الاستخدامات", bg="#e6f0ff", font=("Tahoma", 14, "bold")).pack(pady=10)

        self.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, font=("Tahoma", 12), width=40, height=10)
        self.listbox.pack(pady=10)
        self.refresh_list()

        frame_btn = tk.Frame(self, bg="#e6f0ff")
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="🖨️ معاينة و طباعة", font=("Tahoma", 10, "bold"), bg="#0078d7", fg="white",
                  command=self.preview_print).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="➕ إضافة", font=("Tahoma", 10, "bold"), bg="#0078d7", fg="white",
                  command=self.add_template).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="✏️ تعديل", font=("Tahoma", 10, "bold"), bg="#0078d7", fg="white",
                  command=self.edit_template).grid(row=0, column=2, padx=5)
        tk.Button(frame_btn, text="❌ حذف", font=("Tahoma", 10, "bold"), bg="#0078d7", fg="white",
                  command=self.delete_template).grid(row=0, column=3, padx=5)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for t in self.templates:
            self.listbox.insert(tk.END, t["name"])

    def add_template(self):
        name = simpledialog.askstring("اسم الاستخدام", "اكتب اسم الاستخدام:")
        if name:
            text = simpledialog.askstring("النص الكامل", "اكتب نص الاستخدام:")
            if text:
                self.templates.append({"name": name, "text": text})
                save_templates(self.templates)
                self.refresh_list()

    def edit_template(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر استخدام لتعديله.")
            return
        idx = sel[0]
        old = self.templates[idx]
        name = simpledialog.askstring("تعديل الاسم", "اكتب الاسم الجديد:", initialvalue=old["name"])
        text = simpledialog.askstring("تعديل النص", "اكتب النص الجديد:", initialvalue=old["text"])
        if name and text:
            self.templates[idx] = {"name": name, "text": text}
            save_templates(self.templates)
            self.refresh_list()

    def delete_template(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر استخدام لحذفه.")
            return
        for i in reversed(sel):
            del self.templates[i]
        save_templates(self.templates)
        self.refresh_list()

    def preview_print(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر استخدام واحد على الأقل للمعاينة.")
            return

        preview = tk.Toplevel(self)
        preview.title("معاينة الطباعة")
        preview.geometry("400x300")
        preview.configure(bg="white")

        text = "\n\n".join([self.templates[i]["text"] for i in sel])
        tk.Label(preview, text=text, font=("Tahoma", 12), bg="white", justify="right", wraplength=350).pack(padx=10, pady=10)

        tk.Button(preview, text="طباعة", bg="#0078d7", fg="white", font=("Tahoma", 10, "bold"),
                  command=lambda: self.print_labels(text)).pack(pady=10)

    def print_labels(self, text):
        file_name = "print_preview.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(text)
        os.startfile(file_name, "print")

if __name__ == "__main__":
    app = LabelApp()
    app.mainloop()

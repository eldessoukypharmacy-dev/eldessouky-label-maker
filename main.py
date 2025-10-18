import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import json
import tempfile
import os

# ==================== إعداد التطبيق ====================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🩺 برنامج طباعة لاصقات الدواء - صيدلية الدسوقي")
app.geometry("750x600")

# ==================== تحميل القوالب ====================
TEMPLATE_FILE = "templates.json"

def load_templates():
    if not os.path.exists(TEMPLATE_FILE):
        return []
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_templates(templates):
    with open(TEMPLATE_FILE, "w", encoding="utf-8") as f:
        json.dump(templates, f, ensure_ascii=False, indent=2)

templates = load_templates()
filtered_templates = templates.copy()  # للبحث

# ==================== الإطارات الأساسية ====================
frame = ctk.CTkFrame(app, corner_radius=10)
frame.pack(padx=20, pady=20, fill="both", expand=True)

title_label = ctk.CTkLabel(frame, text="📋 قوالب الطباعة", font=("Tahoma", 22, "bold"))
title_label.pack(pady=10)

# ==================== مربع البحث ====================
search_var = tk.StringVar()

def filter_templates(*args):
    query = search_var.get().strip().lower()
    global filtered_templates
    if query == "":
        filtered_templates = templates.copy()
    else:
        filtered_templates = [t for t in templates if query in t["name"].lower() or query in t["text"].lower()]
    refresh_checkboxes()

search_entry = ctk.CTkEntry(frame, placeholder_text="🔍 ابحث عن قالب...", textvariable=search_var, width=400, height=35, font=("Tahoma", 14))
search_entry.pack(pady=(0, 10))
search_var.trace_add("write", filter_templates)

# ==================== قائمة القوالب ====================
template_vars = []
checkbox_frame = ctk.CTkScrollableFrame(frame, label_text="اختيار القوالب للطباعة", width=600, height=250)
checkbox_frame.pack(pady=10, padx=20, fill="both", expand=True)

def refresh_checkboxes():
    for widget in checkbox_frame.winfo_children():
        widget.destroy()
    template_vars.clear()
    for tpl in filtered_templates:
        var = tk.BooleanVar()
        cb = ctk.CTkCheckBox(checkbox_frame, text=tpl["name"], variable=var, font=("Tahoma", 16))
        cb.pack(anchor="w", padx=20, pady=5)
        template_vars.append((var, tpl))

refresh_checkboxes()

# ==================== إدارة القوالب ====================
def add_template():
    name = simpledialog.askstring("إضافة قالب", "📝 اكتب اسم القالب:")
    if not name:
        return
    text = simpledialog.askstring("إضافة القالب", "✏️ اكتب نص القالب:")
    if not text:
        return
    templates.append({"name": name, "text": text})
    save_templates(templates)
    filter_templates()

def edit_template():
    names = [tpl["name"] for tpl in templates]
    if not names:
        messagebox.showinfo("تنبيه", "⚠️ لا توجد قوالب لتعديلها.")
        return
    name = simpledialog.askstring("تعديل قالب", "اكتب اسم القالب المراد تعديله:")
    if name not in names:
        messagebox.showerror("خطأ", "❌ القالب غير موجود.")
        return
    tpl = next(t for t in templates if t["name"] == name)
    new_text = simpledialog.askstring("تعديل نص القالب", f"النص الحالي:\n\n{tpl['text']}\n\n🖊️ اكتب النص الجديد:")
    if not new_text:
        return
    tpl["text"] = new_text
    save_templates(templates)
    filter_templates()

def delete_template():
    names = [tpl["name"] for tpl in templates]
    if not names:
        messagebox.showinfo("تنبيه", "⚠️ لا توجد قوالب لحذفها.")
        return
    name = simpledialog.askstring("حذف قالب", "🗑️ اكتب اسم القالب المراد حذفه:")
    if name not in names:
        messagebox.showerror("خطأ", "❌ القالب غير موجود.")
        return
    templates[:] = [t for t in templates if t["name"] != name]
    save_templates(templates)
    filter_templates()

# ==================== المعاينة ====================
def preview_labels():
    selected = [tpl["text"] for var, tpl in template_vars if var.get()]
    if not selected:
        messagebox.showwarning("تنبيه", "⚠️ من فضلك اختر قالب واحد على الأقل.")
        return

    preview_window = ctk.CTkToplevel(app)
    preview_window.title("👁️‍🗨️ معاينة قبل الطباعة")
    preview_window.geometry("450x400")

    txt = "\n\n".join(selected)
    text_widget = ctk.CTkTextbox(preview_window, wrap="word", font=("Tahoma", 16))
    text_widget.insert("1.0", txt)
    text_widget.configure(state="disabled")
    text_widget.pack(padx=20, pady=20, fill="both", expand=True)

# ==================== الطباعة ====================
def print_labels():
    selected = [tpl["text"] for var, tpl in template_vars if var.get()]
    if not selected:
        messagebox.showwarning("تنبيه", "⚠️ اختر قالب واحد على الأقل للطباعة.")
        return

    txt = "\n\n".join(selected)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    temp_file.write(txt.encode("utf-8"))
    temp_file.close()
    os.startfile(temp_file.name, "print")

# ==================== الأزرار ====================
btns_frame = ctk.CTkFrame(frame)
btns_frame.pack(pady=10)

ctk.CTkButton(btns_frame, text="➕ إضافة قالب", command=add_template, width=150).grid(row=0, column=0, padx=10, pady=5)
ctk.CTkButton(btns_frame, text="✏️ تعديل قالب", command=edit_template, width=150).grid(row=0, column=1, padx=10, pady=5)
ctk.CTkButton(btns_frame, text="🗑️ حذف قالب", command=delete_template, width=150).grid(row=0, column=2, padx=10, pady=5)

ctk.CTkButton(frame, text="👁️‍🗨️ معاينة قبل الطباعة", command=preview_labels, width=250, height=40).pack(pady=10)
ctk.CTkButton(frame, text="🖨️ طباعة المحدد", command=print_labels, width=250, height=40).pack(pady=5)

app.mainloop()

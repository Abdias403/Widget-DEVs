import tkinter as tk
from tkinter import filedialog
import os
import importlib.util

ruta_skins = os.path.join(os.getcwd(), "skins")

def open_skins_options():
    skins_options = tk.Toplevel(root)
    skins_options.title("Opciones de Skins")
    skins_options.geometry("300x200")

    label = tk.Label(skins_options, text="Selecciona una opción de skin:")
    label.pack()

    button_clock = tk.Button(skins_options, text="Reloj", command=lambda: execute_skin("reloj.py"))
    button_clock.pack()

    button_widget = tk.Button(skins_options, text="Widget", command=lambda: execute_skin("widget.py"))
    button_widget.pack()

    button_calendar = tk.Button(skins_options, text="Calendario", command=lambda: execute_skin("calendario.py"))
    button_calendar.pack()

    label_filename = tk.Label(skins_options, text="")
    label_filename.pack()

    execute_button = tk.Button(skins_options, text="Ejecutar Skin", command=lambda: execute_selected_skin(label_filename))
    execute_button.pack()

    upload_button = tk.Button(skins_options, text="Cargar Skin", command=lambda: upload_skin(label_filename))
    upload_button.pack()

    update_skins_list(skins_options)

def execute_selected_skin(label):
    filename = label["text"]
    if filename:
        os.system(f"python {filename}")

def update_skins_list(window):
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") not in ["Reloj", "Widget", "Calendario"]:
            widget.destroy()

    archivos_skins = obtener_archivos_py()
    for archivo in archivos_skins:
        skin_button = tk.Button(window, text=archivo, command=lambda a=archivo: execute_skin(a))
        skin_button.pack()

def obtener_archivos_py():
    archivos_py = []
    for archivo in os.listdir(ruta_skins):
        if archivo.endswith('.py'):
            archivos_py.append(archivo)
    return archivos_py

def cargar_skin(nombre_archivo):
    ruta_archivo = os.path.join(ruta_skins, nombre_archivo)
    spec = importlib.util.spec_from_file_location(nombre_archivo[:-3], ruta_archivo)
    skin = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(skin)
    return skin

def execute_skin(filename):
    execute_selected_skin({"text": os.path.join(ruta_skins, filename)})

def upload_skin(label):
    file_path = filedialog.askopenfilename(filetypes=(("Python files", "*.py"), ("All files", "*.*")))
    if file_path:
        label.config(text=file_path)
        destination = os.path.join(ruta_skins, os.path.basename(file_path))
        if os.path.exists(destination):
            os.remove(destination)
        os.replace(file_path, destination)

# Crear la carpeta de skins si no existe
if not os.path.exists(ruta_skins):
    os.makedirs(ruta_skins)

# Crear la ventana principal
root = tk.Tk()
root.title("Menu")

# Crear barra de menú
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Crear menú "Opciones"
options_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=options_menu)

# Agregar opciones al menú
options_menu.add_command(label="Skins", command=open_skins_options)
options_menu.add_command(label="Configuración")
options_menu.add_command(label="Editar")

# Bucle principal de la interfaz gráfica
root.mainloop()

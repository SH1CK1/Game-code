import tkinter as tk

root = tk.Tk()
width_px = root.winfo_screenwidth()
height_px = root.winfo_screenheight()
root.destroy()

print(f"Ширина экрана: {width_px} пикселей")
print(f"Высота экрана: {height_px} пикселей")

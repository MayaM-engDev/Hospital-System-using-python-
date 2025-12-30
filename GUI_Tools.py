from tkinter import *
from tkinter import ttk


def create_scrollable_tab(notebook,title):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=title)

    canvas = Canvas(tab)
    scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)

    scrollable_frame = Frame(canvas,bg= "#D3D3D3")

    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set,bg="#D3D3D3")
    canvas.bind_all("<MouseWheel>",lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scrollable_frame

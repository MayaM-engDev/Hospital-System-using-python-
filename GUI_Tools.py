from tkinter import *
from tkinter import ttk


# def create_scrollable_tab(notebook,title):
#     tab = ttk.Frame(notebook)
#     notebook.add(tab, text=title)

#     canvas = Canvas(tab)
#     scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)

#     scrollable_frame = Frame(canvas,bg= "#D3D3D3")

#     scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

#     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#     canvas.configure(yscrollcommand=scrollbar.set,bg="#D3D3D3")
#     canvas.bind_all("<MouseWheel>",lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))
    
#     canvas.pack(side="left", fill="both", expand=True)

#     scrollbar.pack(side="right", fill="y")

#     return scrollable_frame


def create_scrollable_tab(notebook, title):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=title)

    # Create canvas and scrollbar
    canvas = Canvas(tab, bg="#D3D3D3", highlightthickness=0)
    scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)

    # This frame will hold your doctor_list_frame
    scrollable_frame = Frame(canvas, bg="#D3D3D3")

    # This is the secret to centering: 
    # We create the window and use "anchor='n'" (top-center) 
    # and we will update the width dynamically
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="n")

    def configure_scroll_region(e):
        canvas.configure(scrollregion=canvas.bbox("all"))
        # This part forces the inner frame to at least be as wide as the canvas
        # so that "center" alignment works
        if scrollable_frame.winfo_reqwidth() < canvas.winfo_width():
            canvas.itemconfigure(canvas_window, width=canvas.winfo_width())

    scrollable_frame.bind("<Configure>", configure_scroll_region)
    
    # Update anchor point whenever canvas resized to keep things centered
    canvas.bind("<Configure>", lambda e: canvas.itemconfigure(canvas_window, width=e.width))

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))
    
    canvas.pack(side="left", fill="both", expand=True)

    # --- 1. CENTER THE FRAME WITHIN THE TAB ---
    # This gives the tab a "flexible" grid. 
    # Weight=1 tells the grid to expand and fill all empty space around the frame.
    scrollable_frame.columnconfigure(0, weight=1)
    scrollable_frame.rowconfigure(0, weight=1)

    scrollbar.pack(side="right", fill="y")

    return scrollable_frame

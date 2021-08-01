from offline_screen import *
from client import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


root = tk.Tk()
root.title("Chain Reaction")
root.geometry("800x800")
root.resizable(0, 0)
font = {"font": ("Arial", 10, "bold"), "background": "#EE018B"}

img = ImageTk.PhotoImage(Image.open("mainMenu.jpg"))

button_style = ttk.Style()
button_style.theme_use("clam")

for style in ["W.TButton", "W.TCheckbutton", "W.TLabel", "W.TEntry"]:
    # if style == 'W.TLabel':
    #     font = {'font': ('Arial', 10, 'bold')}
    button_style.configure(style, **font)

button_style.map("W.TButton", background=[("active", "#00FABC")])

sound_option = tk.IntVar(value=0)


def image_frame():
    main_image_frame = ttk.Label(root, image=img)
    main_image_frame.place(x=0, y=0, relwidth=1, relheight=1)


def home_page():
    widget_destroy(root)
    image_frame()
    button_frame = ttk.Frame(root, relief="raised", borderwidth=2)
    button_frame.place(x=353.7, y=512)
    offline_button = ttk.Button(
        button_frame, text="Offline", style="W.TButton", command=offline_page
    )
    offline_button.grid(column=0, row=0, sticky=tk.W)
    local_button = ttk.Button(
        button_frame, text="Local", style="W.TButton", command=local_page
    )
    local_button.grid(column=0, row=1, sticky=tk.W)
    settings_button = ttk.Button(
        button_frame, text="Settings", style="W.TButton", command=settings_page
    )
    settings_button.grid(column=0, row=2, sticky=tk.W)

    root.mainloop()


def local_page():
    widget_destroy(root)
    image_frame()
    button_frame = ttk.Frame(root, relief="raised", borderwidth=2)
    button_frame.place(x=353.7, y=512)
    host_button = ttk.Button(
        button_frame, text="Host", style="W.TButton", command=lambda: join_page(True)
    )
    host_button.grid(column=0, row=0, sticky=tk.W)

    join_button = ttk.Button(
        button_frame, text="Join", style="W.TButton", command=lambda: join_page(False)
    )
    join_button.grid(column=0, row=1, sticky=tk.W)
    back_button = ttk.Button(
        button_frame, text="Back", style="W.TButton", command=home_page
    )
    back_button.grid(column=0, row=2, sticky=tk.W)
    root.mainloop()


def settings_page():
    widget_destroy(root)
    image_frame()
    button_frame = ttk.Frame(root, relief="raised", borderwidth=2)
    button_frame.place(x=353.7, y=512)
    sound_button = ttk.Checkbutton(
        button_frame, text="Sound", style="W.TCheckbutton", variable=sound_option
    )
    sound_button.grid(column=0, row=0, sticky=tk.W)
    back_button = ttk.Button(
        button_frame, text="Back", style="W.TButton", command=home_page
    )
    back_button.grid(column=0, row=1, sticky=tk.W)
    root.mainloop()


def offline_page():
    widget_destroy(root)
    mainScreen(root, home_page, image_frame, button_style, sound_option.get())


def join_page(isHost):
    call_join(
        root,
        local_page,
        widget_destroy,
        image_frame,
        button_style,
        home_page,
        isHost,
        sound_option.get(),
    )


if __name__ == "__main__":
    home_page()

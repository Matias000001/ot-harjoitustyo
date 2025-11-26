# src/gui_main.py
from tkinter import Tk
from ui import UI


def main():
    window = Tk()
    window.title("CipherVault")
    window.geometry("800x550")
    window.minsize(800, 550)
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()

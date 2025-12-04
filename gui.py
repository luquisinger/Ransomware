#!/usr/bin/env python3
# gui.py
import tkinter as tk
from tkinter import simpledialog

def pedir_senha():
    root = tk.Tk()
    root.withdraw()  # esconde janela principal

    senha = simpledialog.askstring(
        "Descriptografia",
        "Digite a chave:",
        show='*'
    )

    root.destroy()
    return senha

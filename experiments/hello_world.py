# hello_world.py
# GUI popup. Requires access to Display:0 (if running in a CLI)

import PySimpleGUI as sg

sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

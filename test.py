import tkinter as tk
window = tk.Tk()

window.geometry("300x400")

frame = tk.Frame(window, width=300, height=400, background="salmon")
frame.pack()
window.title("Test GitHub")

canvas = tk.Canvas(frame, width= 200, height=300, background="pink")
canvas.pack()


window.mainloop()
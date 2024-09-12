import tkinter as tk
import threading
import simple_mode
import automated_mode

def start_simple_mode():
    threading.Thread(target=simple_mode.run_simple_mode, daemon=True).start()

def start_automated_mode():
    threading.Thread(target=automated_mode.run_automated_mode, daemon=True).start()

def quit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Trading Bot")

simple_button = tk.Button(root, text="Simple Mode", command=start_simple_mode)
simple_button.pack(pady=10)

automated_button = tk.Button(root, text="Automated Mode", command=start_automated_mode)
automated_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(pady=10)

root.mainloop()
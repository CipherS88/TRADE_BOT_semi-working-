import tkinter as tk
import numpy as np
import cv2
import mss

def analyze_screen():
    with mss.mss() as sct:
        # capture
        monitor = sct.monitors[1]
        img = sct.grab(monitor)
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        #analysis here
        return "buy" if np.random.rand() > 0.5 else "sell"

def run_simple_mode():
    def update_status():
        action = analyze_screen()
        status_label.config(text=f"Recommended Action: {action}")
        root.after(1000, update_status)  # Refresh every second

    global root
    root = tk.Tk()
    root.title("Simple Mode")

    status_label = tk.Label(root, text="", font=("Helvetica", 14))
    status_label.pack(pady=10)

    update_status()  # loop
    root.mainloop()

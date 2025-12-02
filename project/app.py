import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import pandas as pd
import matplotlib.pyplot as plt
import os
import focus_tracker  # Import main tracker logic

running = False
thread = None
LOG_FILE = "focus_log.csv"


def tracking_worker():
    """Executes the tracking loop without opening terminal."""
    global running
    try:
        focus_tracker.start_tracking_loop()
    except Exception as e:
        messagebox.showerror("Error", f"Tracking crashed:\n{e}")
    finally:
        running = False


def start_tracking():
    global running, thread

    if running:
        messagebox.showinfo("Already Running", "Tracking is already running.")
        return

    running = True
    thread = threading.Thread(target=tracking_worker, daemon=True)
    thread.start()
    messagebox.showinfo("Started", "Focus tracking started.")


def stop_tracking():
    global running

    if not running:
        messagebox.showinfo("Not Running", "Tracking is not active.")
        return

    running = False
    focus_tracker.stop()
    messagebox.showinfo("Stopped", "Focus tracking stopped.")

def show_progress():
    if not os.path.exists(LOG_FILE):
        messagebox.showwarning("No Data", "No focus log found yet.")
        return

    try:
        df = pd.read_csv(LOG_FILE)

        if df.empty:
            messagebox.showinfo("No Data", "Log exists but has no entries.")
            return

        plt.figure(figsize=(8, 5))
        plt.plot(df['Date'], df['Focus_Percent(%)'], marker='o', linewidth=2)
        plt.xlabel("Session Date")
        plt.ylabel("Focus (%)")
        plt.title("📈 Focus Tracking Progress")
        plt.ylim(0, 100)
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Unable to read log file:\n{e}")

# ---------------- GUI -----------------

root = tk.Tk()
root.title("Focus Tracker Dashboard")
root.geometry("400x450")
root.config(bg="#2C2F33")

# Profile image
try:
    img = Image.open("profile.jpg").resize((120, 120))
    profile_img = ImageTk.PhotoImage(img)
    tk.Label(root, image=profile_img, bg="#2C2F33").pack(pady=20)
except:
    tk.Label(root, text="(No Profile Image)", bg="#2C2F33", fg="white").pack(pady=20)


tk.Button(root, text="Start Focus Tracking", command=start_tracking, width=25, height=2, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Show Progress Report", command=show_progress, width=25, height=2, bg="#2196F3", fg="white").pack(pady=10)
tk.Button(root, text="Stop", command=stop_tracking, width=25, height=2, bg="#FF5252", fg="white").pack(pady=10)

root.mainloop()

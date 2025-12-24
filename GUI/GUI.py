import tkinter as tk

def clicked():
    label.config(text="Button clicked")

root = tk.Tk()
root.title("My App")
root.geometry("300x200")

label = tk.Label(root, text="Hello")
label.pack(pady=10)

# Load image correctly
img = tk.PhotoImage(file=r"C:\Users\lavhr\OneDrive\מסמכים\GitHub\Lahav-Samples\images\Untitled.png")

# Keep reference AND attach to widget
img_label = tk.Label(root, image=img)
img_label.pack()
logo = img
root.iconphoto(True,logo)
button = tk.Button(root, text="Click me", command=clicked)
button.pack(pady=10)

root.mainloop()

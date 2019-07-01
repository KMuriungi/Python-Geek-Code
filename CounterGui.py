import Tkinter as tk

counter =0

def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()

root = tk.Tk()
root.title("Counter")
label= tk.Label(root, fg = "green").pack()
counter_label(label)
stopButton = tk.Button(root,text = "STOP",fg = "red",width = 40,command = root.destroy).pack()

root.mainloop()

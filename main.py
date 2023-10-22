from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("My app")
root.iconbitmap("./favicon.ico")

my_img1 = ImageTk.PhotoImage(Image.open("./minos.png"))
my_img3 = ImageTk.PhotoImage(Image.open("./cat.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("./ultrakill.jpg"))

image_list = [my_img1, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(n):
    global my_label
    global forw
    global prev

    my_label.configure(image=image_list[n - 1])
    forw.configure(command=lambda: forward(n + 1))
    prev.configure(command=lambda: previous(n - 1), state="normal")

    if n == 3:
        forw.configure(state="disabled")


def previous(n):
    global my_label
    global forw
    global prev

    my_label.configure(image=image_list[n - 1])
    forw.configure(command=lambda: forward(n + 1))
    prev.configure(command=lambda: previous(n - 1))

    if n == 1:
        prev.configure(state="disabled")


prev = Button(root, text="<<", command=previous, state="disabled")
quit_btn = Button(root, text="Exit program", command=root.quit)
forw = Button(root, text=">>", command=lambda: forward(2))

prev.grid(row=1, column=0)
quit_btn.grid(row=1, column=1)
forw.grid(row=1, column=2)

root.mainloop()

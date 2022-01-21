from tkinter import *


window = Tk()
window.geometry("400x400")

labels = []
images = []
canvas = []

for i in range(5):
    a = PhotoImage(file="Icons\\01d@2x.png", name=f"img_{i}")
    images.append(a)

print(images)

for i in range(5):
    a = Canvas(width=100, height=100, name=f"canvas_{i}")
    a.create_image(50, 50, image=images[i])
    canvas.append(a)

print(canvas)

for i in range(5):
    canvas[i].pack()

for i in range(6,12):
    print(i)


# for i in range(48):
#     a = Label(text=f"salam {i}", name=f"label_{i}")
#     labels.append(a)
#
# print(labels)
# for i in range(len(labels)):
#     labels[i].pack()
window.mainloop()
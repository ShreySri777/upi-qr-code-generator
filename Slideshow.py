from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

#List of images for slideshow
image_paths = [
    r"C:\Users\santo\OneDrive\Pictures\Screenshots\Screenshot 2026-06-13 130140.png",
    r"C:\Users\santo\OneDrive\Pictures\Screenshots\Screenshot 2026-06-13 130155.png",
    r"C:\Users\santo\OneDrive\Pictures\Screenshots\Screenshot 2026-06-13 130207.png",
    r"C:\Users\santo\OneDrive\Pictures\Screenshots\Screenshot 2026-06-13 130216.png",
    r"C:\Users\santo\OneDrive\Pictures\Screenshots\Screenshot 2026-06-13 130226.png"
]

#Resize the image to 1080x1080
image_size = (1080,1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image = photo_image)
        label.update()
        time.sleep(2)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()
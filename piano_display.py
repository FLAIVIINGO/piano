from tkinter import *

from PIL import Image, ImageTk

WINDOW_HEIGHT = 773
WINDOW_WIDTH = 1400

class PianoDisplay:

  def __init__(self) -> None:
    self.window = Tk()
    self.window.title("Jazz Piano Trainer")
    self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    self.frame = Frame(self.window)
    self.frame.pack(side=RIGHT)

    self.canvas = Canvas(
      self.frame, bg="white", width=WINDOW_WIDTH, height=WINDOW_HEIGHT
    )

    self.canvas.pack()

    self.window.update()
    print("Canvas Width:", self.canvas.winfo_width())
    print("Canvas Height:", self.canvas.winfo_height())

    original_image = Image.open("images/keys.png")

    aspect_ratio = original_image.height / original_image.width
    new_height = int(WINDOW_WIDTH * aspect_ratio)
    resized_image = original_image.resize((WINDOW_WIDTH, new_height), Image.LANCZOS)

    self.keys_img = ImageTk.PhotoImage(resized_image)

    # Set y-coordinate to be window height minus half of image height
    y_coordinate = WINDOW_HEIGHT - new_height / 2

    # self.keys_img = ImageTk.PhotoImage(Image.open("images/keys.png"))
  
    self.canvas.create_image(0, y_coordinate, image=self.keys_img, anchor="w")
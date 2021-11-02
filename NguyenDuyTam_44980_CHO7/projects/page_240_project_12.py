"""
Author:Nguyễn Duy Tâm
Date: 26/11/2000
Problem:

Solution:
    ....
"""
import os
import os.path

import tkinter

tk = tkinter

##########################################################################
# Module Exceptions

_root = None


class ImageView(tk.Canvas):
    def __init__(self, image,
                 title="New Image",
                 autoflush=False):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master,
                           width=image.getWidth(),
                           height=image.getHeight())
        self.master.title(title)
        self.pack()
        master.resizable(0, 0)
        self.image = image
        self.height = image.getHeight()
        self.width = image.getWidth()
        self.autoflush = autoflush
        self.closed = False

    def close(self):
        """Close the window"""
        self.closed = True
        self.master.destroy()
        self.image.canvas = None
        _root.quit()

    def isClosed(self):
        return self.closed

    def getHeight(self):
        """Return the height of the window"""
        return self.height

    def getWidth(self):
        """Return the width of the window"""
        return self.width


class Image:

    def __init__(self, *args):
        self.canvas = None
        if len(args) == 1:
            name = args[0]
            if type(name) != str:
                raise Exception('Must be a file name')
            if name[-4:].upper() != '.GIF':
                raise Exception('File must be a GIF')
            if not os.path.exists(args[0]):
                raise Exception('File not in current directory')
            self.image = tk.PhotoImage(file=args[0], master=_root)
            self.filename = args[0]
            self.width = self.image.width()
            self.height = self.image.height()
        else:  # arguments are width and height
            self.width, self.height = args
            self.image = tk.PhotoImage(master=_root,
                                       width=self.width,
                                       height=self.height)
            self.filename = ""

    def getWidth(self):
        """Returns the width of the image in pixels"""
        return self.width

    def getHeight(self):
        """Returns the height of the image in pixels"""
        return self.height

    def getPixel(self, x, y):
        """Returns a tuple (r,g,b) with the RGB color values for pixel (x,y)
        r,g,b are in range(256)

        """
        value = self.image.get(x, y)
        print("value:", value)
        if type(value) == int:
            return (value, value, value)
        else:
            return value

    def setPixel(self, x, y, color):
        """Sets pixel (x,y) to the color given by RGB values r, g, and b.
        r,g,b should be in range(256)

        """
        self.image.put("{#%02x%02x%02x}" % color, (x, y))

    def draw(self):
        """Creates and opens a window on an image.
        The user must close the window to return control to
        the caller."""
        if not self.canvas:
            self.canvas = ImageView(self,
                                    self.filename)
        self.canvas.create_image(self.width / 2,
                                 self.height / 2,
                                 image=self.image)
        _root.mainloop()

    def save(self, filename=""):
        """Saves the image to filename.  If no file name
        is provided, uses the image's file name if there
        is one; otherwise, simply returns.
        If the .gif extension is not present, it is added.
        """
        if filename == "":
            return
        else:
            self.filename = filename
        path, name = os.path.split(filename)
        ext = name.split(".")[-1]
        if ext != "gif":
            filename += ".gif"
            self.filename = filename
        self.image.write(self.filename, format="gif")

    def clone(self):
        new = Image(self.width, self.height)
        new.image = self.image.copy()
        return new

    def __str__(self):
        rep = ""
        if self.filename:
            rep += ("File name: " + self.filename + "\n")
        rep += ("Width:  " + str(self.width) + \
                "\nHeight: " + str(self.height))
        return rep


_root = tk.Tk()
_root.withdraw()
"""
solution: Defines a transform function that represents a general
pattern for traversing an image and modifying its pixels.

Tests this function by using it to define grayscale and
black and white functions.

"""
from images import Image


def transform(image, function):
    """Traverses the image and resets each pixel with the result
    of applying the function to it."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            image.setPixel(x, y, function(image.getPixel(x, y)))


def grayscale(image):
    """Converts an image to grayscale using the
    psychologically accurate transformations."""

    def change(triple):
        """Converts a pixel to grayscale."""
        (r, g, b) = triple
        r = int(r * 0.299)
        g = int(g * 0.587)
        b = int(b * 0.114)
        lum = r + g + b
        return (lum, lum, lum)

    transform(image, change)


def blackAndWhite(image):
    """Converts an image to black and white."""

    def change(triple):
        """Converts a pixel to black and white."""
        (r, g, b) = triple
        average = (r + g + b) // 3
        if average < 128:
            return (0, 0, 0)
        else:
            return (255, 255, 255)

    transform(image, change)


if __name__ == '__main__':
    filename = input("Enter the image file name: ")
    image = Image(filename)
    grayscale(image)
    # blackAndWhite(image)
    image.draw()

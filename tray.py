from gui import App

from PIL import Image
from pystray import Icon, MenuItem, Menu




def start():
    App().mainloop()


def exit(icon):
    icon.stop()


def reformat_image():
    image = Image.open('src/img/logo.png')

    return image


def main_tray():
    Icon('test', reformat_image(),
         menu=Menu(
             MenuItem('Start', start),
             MenuItem('Exit', exit)
         )
         ).run()


if __name__ == '__main__':
    main_tray()

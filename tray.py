import keyboard
from PIL import Image
from pystray import Icon, MenuItem, Menu

from gui import App


def reformat_image():
    image = Image.open('src/img/logo.png')
    return image


def main_tray():
    icon = Icon('test', reformat_image(),
                menu=Menu(
                    MenuItem('Start', lambda: App().mainloop()),
                    MenuItem('Exit', lambda: icon.stop())
                )
                )
    keyboard.add_hotkey('ctrl+space', callback=lambda: App().mainloop())

    icon.run()


if __name__ == '__main__':
    main_tray()

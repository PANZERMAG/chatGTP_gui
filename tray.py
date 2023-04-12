import pystray
from PIL import Image

def on_exit():
    # Функция, которая будет вызываться при выходе из программы
    print("Программа завершена")

def on_click(icon):
    # Функция, которая будет вызываться при клике на иконку
    print("Клик на иконку")

# Создание иконки
image = Image.open("src/img/")
menu = pystray.Menu(pystray.MenuItem("Выход", on_exit))
icon = pystray.Icon("example", image, "Пример", menu)

# Добавление обработчика клика на иконку
icon.run(on_click)

# Запуск бесконечного цикла, чтобы программа не завершилась
while True:
    pass

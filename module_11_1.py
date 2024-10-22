import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFilter


class Requests:

    url = 'https://mail.ru'  # Указываем URL, на который будем отправлять GET-запрос

    response = requests.get(url)  # запрос по указанному URL

    if response.status_code == 200:  # Проверяем ответ

        data = response.url  # Если 200, получаем данные из ответа
        print(f'Статус ответа: OK [код 200]')

    else:
        print('Ошибка при выполнении запроса')  # Когда ошибка

class Pillow:
    im = Image.open('foto.jpg')
    resized_im = im.resize((800, 600))  # изменение размера
    resized_im.save('resized_image.jpg')

    draw = ImageDraw.Draw(im) # Вставка текста в изображение
    message = f"Привет!" # Текст
    draw.text((10, 20), message, fill=ImageColor.colormap['red']) # Сдвиг по оси х, у, цвет текста


    blurred_image = im.filter(ImageFilter.BLUR)  # применить эффекты
    blurred_image.save('blurred_image.jpg')


    im.save('converted_image.jpg')  # конвертация в формат JPEG
    im.save('converted_image.gif')  # конвертация в формат GIF

class Matplotlib:
    x = [7, 6, 5, 4, 3, 2, 1]
    y = [10, 20, 15, 25, 30, 40, 50]

    plt.plot(x, y)         # Построение линейного графика
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title('Пример линейного графика')
    plt.show()

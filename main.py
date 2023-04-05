from PIL import Image

# открываем изображение
img = Image.open("image.jpg")

# считываем значения цветов пикселей
pixels = img.load()
color_sum = 0
count = 0

# вычисляем сумму значений цветов и количество пикселей
for i in range(img.width):
    for j in range(img.height):
        color_sum += sum(pixels[i, j])
        count += 1

# вычисляем среднее значение цветов
avg_color = color_sum // count

print(f"Среднее значение цветов: {avg_color}")

import cv2
import numpy as np
import matplotlib.pyplot as plt
# отображение графиков в ноутбуке

cat_image  = cv2.imread('img/cat.jpg')
cat_image = cv2.cvtColor(cat_image, cv2.COLOR_BGR2RGB)  # преобразуем цвет для plt

# значения цвета можно посмотреть в gimp или paint
pix = 256
low_red = (0.37 * pix, 0.11 * pix, 0.0 * pix)
high_red = (0.60 * pix, 0.6 * pix, 0.4 * pix)

cat_area = cv2.inRange(cat_image, low_red, high_red)

# посмотрим на результат
fig, m_axs = plt.subplots(1, 2, figsize = (12, 9))
ax1, ax2 = m_axs

ax1.set_title('Исходная картинка', fontsize=15)
ax1.imshow(cat_image, cmap='gray')
ax1.axis('off')


ax2.set_title('Только кот', fontsize=15)
ax2.imshow(cat_area, cmap='gray')
ax2.axis('off')
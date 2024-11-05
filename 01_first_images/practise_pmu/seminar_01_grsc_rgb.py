import cv2
import numpy as np
import matplotlib.pyplot as plt
# отображение графиков в ноутбуке

# считаем изображение
image = cv2.imread('01_first_images/img/RGB_cube.png') 

# посмотрим, какой тип объекта 
print(type(image), image.dtype)

# размерность
print(image.shape)

# преобразуем RGB в BGR для корректного отображения
# это необходимо из-за особенностей matplotlib
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

'''Отобразим объект''' # Раскомментировать нижние строки
# plt.imshow(image)
# plt.axis('off') # Можно включать/отключать координаты
# # plt.show()

# создадим grayscale изображение с помощью openCV
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray_image_0 = np.mean(image, axis=2)

fig, axs = plt.subplots(1, 3, figsize = (12, 8))
ax1, ax2, ax3 = axs

ax1.set_title('RGB изображение', fontsize=15)
ax1.imshow(image)

ax2.set_title('Grayscale изображение', fontsize=15)
ax2.imshow(gray_image, cmap='gray')

ax3.set_title('Grayscale"изображение', fontsize=15)
ax3.imshow(gray_image_0, cmap='gray')
# plt.show()


axs = [ax.axis('off') for ax in axs.flatten()]


''' ИГРАЕМСЯ С КАНАЛАМИ ИЗОБРАЖЕНИЙ'''

# R scale
r = image[:, :, 0].copy()
r[(r >= 40) & (r <= 250)] = 0

# G scale
g = image[:, :, 1].copy()
g[(g >= 150) & (g <= 250)] = 0

# B scale
b = image[:, :, 2].copy()
b[(b >= 250) & (b <= 255)] = 0

## посмотрим на результат
fig, axs = plt.subplots(1, 4, figsize = (20, 9))
ax1, ax2, ax3, ax4 = axs

ax1.set_title('R канал', fontsize=15)
ax1.imshow(r, cmap='gray')
ax2.set_title('G канал', fontsize=15)
ax2.imshow(g, cmap='gray')
ax3.set_title('B канал', fontsize=15)
ax3.imshow(b, cmap='gray')
ax4.set_title('RGB', fontsize=15)
ax4.imshow(image)

axs = [ax.axis('off') for ax in axs.flatten()]

# plt.show()

# ПОЛУЧИЛИ ТАКИЕ РЕЗУЛЬТАТАТЫ, ТАК КАК ТАК НАСТРОЕНЫ ДИАПАЗОНЫ ЗНАЧЕНИЙ (X, X ,X) ОТ 0 ДО 255




""" ИЗМЕНИМ КОНФИГУРАЦИЮ"""

tr_val = 155  # пороговое значение

# R scale
r = image[:, :, 0].copy()
r[r < tr_val] = 0

# G scale
g = image[:, :, 1].copy()
g[g < tr_val] = 0

# B scale
b = image[:, :, 2].copy()
b[b < tr_val] = 0

# посмотрим на результат
fig, axs = plt.subplots(1, 4, figsize = (20, 9))
ax1, ax2, ax3, ax4 = axs

ax1.set_title('R канал', fontsize=15)
ax1.imshow(r, cmap='gray')
ax2.set_title('G канал', fontsize=15)
ax2.imshow(g, cmap='gray')
ax3.set_title('B канал', fontsize=15)
ax3.imshow(b, cmap='gray')
ax4.set_title('RGB', fontsize=15)
ax4.imshow(image)

axs = [ax.axis('off') for ax in axs.flatten()]

plt.show()

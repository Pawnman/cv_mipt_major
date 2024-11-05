import cv2
import numpy as np
import matplotlib.pyplot as plt
# отображение графиков в ноутбуке

cat_image  = cv2.imread('01_first_images/img/testcat.jpg')
cat_image = cv2.cvtColor(cat_image, cv2.COLOR_BGR2RGB)  # преобразуем цвет для plt

# значения цвета можно посмотреть в gimp или paint
pix = 256
low_red = (0.37 * pix, 0.11 * pix, 0.0 * pix)
high_red = (0.63 * pix, 0.6 * pix, 0.43 * pix)

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
# plt.show() # Кот в ЧБ

print(cat_area.shape, cat_image.shape)

only_cat = np.zeros_like(cat_image)

for i in range(3):
    only_cat[..., i] = cat_image[..., i] * cat_area

print(cat_area.shape)

only_cat = cat_image * cat_area[:,:, np.newaxis]

print(only_cat.shape)

only_cat = cv2.cvtColor(only_cat, cv2.COLOR_BGR2RGB)

plt.imshow(only_cat)
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt
# отображение графиков в ноутбуке

cat_image  = cv2.imread('01_first_images/img/testcat.jpg')
cat_image = cv2.cvtColor(cat_image, cv2.COLOR_BGR2RGB)  # преобразуем цвет для plt

# plt.imshow(cat_image) # Раскомментировать для вывода изображения


# меняем цветовое пространство
cat_image_hsv = cv2.cvtColor(cat_image, cv2.COLOR_RGB2HSV)

# осталось только подобрать нужные цвета 
# воспользуйтесь функциями, которые реализовали выше
hsv_low = (0.00 * 360, 90, 30)
hsv_high = (0.057 * 360, 255, 255)

cat_area = cv2.inRange(cat_image_hsv, hsv_low, hsv_high)

## посмотрим на результат
fig, m_axs = plt.subplots(1, 2, figsize = (12, 9))
ax1, ax2 = m_axs

ax1.set_title('Исходная картинка', fontsize=15)
ax1.imshow(cat_image)
ax2.set_title('Только кот', fontsize=15)
ax2.imshow(cat_area, cmap='gray')

# plt.show() # Раскомментировать для вывода изображения

print(cat_area.shape)

x, y = np.argwhere(cat_area == 255).T
only_cat = np.zeros_like(cat_image)
only_cat[x, y] = cat_image[x, y]

plt.imshow(only_cat)
plt.show()

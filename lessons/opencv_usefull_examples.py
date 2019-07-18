# добавим необходимый пакет с opencv
import cv2

# ------------------------OPEN IMAGE FILE---------------------------

path_to_picture = './pictures/matrix-sunglasses-768x320.jpg'
# загружаем изображение и отображаем его
image = cv2.imread(path_to_picture)  # открываем и читаем файл с жесткого диска.

# Команда cv2.imread возвращает NumPy массив,
# который содержит представление данных из изображения.

print(image)
print(image.size)

cv2.imshow("Original image", image)  # Отображение файла встроенными средствами OpenCV.
cv2.waitKey(0)

# метод для отображения cv2.imshow() принимает в себя два аргумента,
# первый это название окна, в котором будет отрисовано изображение,
# второй –  имя переменной, которая хранит данное изображение.
# Однако выполнение только данной команды отрисует изображение и
# сразу же закроет программу. Для того, чтобы мы смогли увидеть
# и работать с изображением, добавим команду cv2.waitKey(0).
# Данная команда останавливает выполнение скрипта до нажатия клавиши на клавиатуре.
# Параметр 0 означает что нажатие любой клавиши будет засчитано.

print(image.shape)
# Когда вы выполним код, мы можем увидеть,
# что на терминал выведется (342, 768, 3).
# Это означает изображение содержит
# 320 строк, 768 столбцов и 3 канала цвета.


# --------------------CHANGE SIZES OF IMAGE---------------------------------

# Нам надо сохранить соотношение сторон
# чтобы изображение не исказилось при уменьшении
# для этого считаем коэф. уменьшения стороны
final_wide = 200#задаем итоговую ширину изображения, равную 200px
r = float(final_wide) / image.shape[1]
dim = (final_wide, int(image.shape[0] * r))#кортеж с новыми размерами

# уменьшаем изображение до подготовленных размеров

#Первый параметр – исходное изображение,
#второй – кортеж с требуемым разрешением для нового изображения,
#третий – алгоритм, который будет использоваться для масштабирования.
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resize image", resized)
cv2.waitKey(0)



# --------------------CUT THE PART OF IMAGE---------------------------------

# вырежем участок изображения используя срезы
# мы же используем NumPy
# crop - обрезать.
cropped = image[50:150, 150:300]
cv2.imshow("Cropped image", cropped)
cv2.waitKey(0)

# стиль NumPy: мы просто используем срезы.
# В такой нотации мы вырезаем изображение с 30 по 130 пиксель по высоте
# и со 150 по 300 пиксель по ширине.



# --------------------ROTATION OF IMAGE---------------------------------

# получим размеры изображения для поворота
# и вычислим центр изображения
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# повернем изображение на 180 градусов
M = cv2.getRotationMatrix2D(center, 180, 1.0)#матрица для преобразования
#Первый аргумент - это кортеж с точкой, относительно которой будет
#                  осуществлен поворот изображения и изменение размера.
#Второй аргумент – угол поворота, в градусах.
#Третий аргумент – коэффициент увеличения, который может быть и меньше 1.
#
# Метод возвращает матрицу поворота, которая может использоваться в необходимых случаях.






rotated = cv2.warpAffine(image, M, (w, h))
#(исходное изображение, матрица преобразования, в данном случае матрицу поворота,
#и кортеж с размерами выходного изображения).
#
# Данный метод возвращает преобразованную картинку.


#Показываем полученное изображение.
cv2.imshow("Rotated image", rotated)
cv2.waitKey(0)


# --------------------REFLECTION OF IMAGE---------------------------------

#отразим изображение по горизонтали
flip_image = cv2.flip(image,1)
#метод cv2.flip принимает два параметра –
#исходное изображение и ось для отражения.
#В качестве осей может быть следующие числа:
#0 – по вертикали,
#1 – по горизонтали,
#(-1) – по вертикали и по горизонтали.


cv2.imshow("Flip image", flip_image)
cv2.waitKey(0)


# --------------------SAVING OF IMAGE---------------------------------
path_to_picture = './pictures/flip.png'
# запишем изображение на диск в формате png
cv2.imwrite(path_to_picture, flip_image)

#команда cv2.imwrite принимает два аргумента,
#первый – путь файла, который будет создан,
#второй – изображение.
#
#Все операции по преобразованию формата OpenCV заботливо взял на себя.
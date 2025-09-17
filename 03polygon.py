import cv2
import numpy as np

img_file = "./img/girl.jpg"
img = cv2.imread(img_file)

# 네모박스
cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), 5)
cv2.rectangle(img, (300, 300), (100, 100), (0, 255, 0), 10)
# -두께에 -1을 넣으면 안에 색이 채워짐
cv2.rectangle(img, (450, 200), (200, 450), (0, 0, 255), -1)

cv2.imshow("IMG", img)
cv2.waitKey()
cv2.destroyAllWindows()

img = np.full((500, 500, 3), 255, dtype=np.uint8)

cv2.circle(img, (150, 150), 100, (255, 0, 0))

#radius 크기가 줄어듬
cv2.circle(img, (300, 150), 70, (0, 255, 0), 5)
# -1 하면 채워짐
cv2.circle(img, (450, 200), 50, (0, 0, 255), -1)

cv2.imshow("IMG", img)
cv2.waitKey()
cv2.destroyAllWindows()

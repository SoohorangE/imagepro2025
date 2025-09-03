import cv2

# 이미지 파일 읽기

img_file = "./img/restaurant1.jpg"
img = cv2.imread(img_file)

if img is not None:
  cv2.imshow("restaurant1", img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
  print("No image file.")


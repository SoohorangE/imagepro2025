import cv2

# 이미지 파일 읽기

img_file = "./img/girl.jpg"
img = cv2.imread(img_file)

if img is not None:
  cv2.imshow("IMG", img)
  cv2.waitKey()
  cv2.destroyAllWindows()
else:
  print("No image file.")

# 2025.9.17 pillow를 사용한 이미지 보기
# 단순하게 이미지를 보여주는 경우는 PIL 사용 추천
from PIL import Image
Image.open("./img/boy_face.jpg").show()

# 흑백으로 읽기
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
if img is not None:
  cv2.imshow("IMG", img)
  cv2.waitKey()
  cv2.destroyAllWindows()

# 동영상 읽기
video_file = "./img/big_buck.avi"
cap = cv2.VideoCapture(video_file)
if cap.isOpened():
  while True:
    ret, frame = cap.read()
    if ret:
      cv2.imshow("IMG", frame)
      cv2.waitKey(60)
    else:
      break
else:
  print("No video file.")

cap.release()
cv2.destroyAllWindows()


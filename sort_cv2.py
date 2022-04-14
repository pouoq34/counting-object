#train을 위해 영상을 이미지로 분할!
import cv2
vidcap = cv2.VideoCapture('/factory/video1.mp4')
success, image = vidcap.read()
count = 1
success = True

while success:
    success, image = vidcap.read()
    cv2.imwrite("/image/%d.jpg" % count, image)
    print("saved image %d.jpg" % count)

    if cv2.waitKey(10)==27:
        break
    count +=1


#직선 그리기 전, 이미지에서 좌표값 뽑기 (https://dk-kang.tistory.com/30)

import cv2
def onMouse(event, x, y, flags, param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        print('왼쪽 마우스 클릭 했을 때 좌표 : ', x, y)
    elif event == cv2.EVENT_LBUTTONUP :
        print('왼쪽 마우스 클릭 땠을 때 좌표 : ', x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        print('현재 이동하는 좌표 : ', x, y)
        if flags & cv2.EVENT_FLAG_LBUTTON :
            cv2.circle(img, (x,y), 5, (0,0,255), -1)
            cv2.imshow('image', img)

img = cv2.imread('/factory/image/363.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', onMouse)
cv2.waitKey()


#직선 그리기
import cv2
import sys

cap = cv2.VideoCapture('/factory/video1.mp4')
red_color = (0,0,255)
white_color = (255,255.,255)

if not cap.isOpened():
    print("Video open Failed")
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.line(frame, (720, 595), (587, 525), red_color, 3)
    frame = cv2.line(frame, (841, 471), (728, 423), red_color, 3)

    frame = cv2.line(frame, (880, 430), (781, 397), red_color, 3)
    frame = cv2.line(frame, (939, 356), (864, 326), red_color, 3)

    frame = cv2.line(frame, (975, 320), (903, 300), red_color, 3)
    frame = cv2.line(frame, (1013, 274), (950, 255), red_color, 3)

    frame = cv2.line(frame, (1037, 251), (985, 239), red_color, 3)
    frame = cv2.line(frame, (1063, 222), (1014, 207), red_color, 3)

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) == 27:
        break
cap.release()
cv2.destroyAllWindows()



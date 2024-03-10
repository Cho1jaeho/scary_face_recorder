import sys
import cv2 as cv


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)
button = 0

fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = int(1 / fps * 1000)

out = cv.VideoWriter('data/output.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True: 
    valid, img = cap.read()

    if not valid:
        break

    inversed = ~img

    if button == 1:     # button = 1이면 녹화
        cv.circle(inversed, (30, 30), radius = 20, color = (0, 0, 255), thickness = -1)
        out.write(inversed)

    cv.imshow('frame', img)
    cv.imshow('inversed', inversed)
    

    if cv.waitKey(delay) == 27:
        break
    if cv.waitKey(delay) == ord(' '):
        button = (button + 1) % 2       # space 누를 때마다 button = 0, 1 반복

cap.release()
out.release()
cv.destroyAllWindows()
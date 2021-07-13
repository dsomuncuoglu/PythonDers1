import cv2
import numpy as np

camera=cv2.VideoCapture(0)

width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Genislik=",width," Yukseklik=",height)

fourcc=cv2.VideoWriter_fourcc(*'MP4V')
writer=cv2.VideoWriter("kayit.mp4",fourcc,20,(width,height))

while True:
    ret,frame=camera.read()
    writer.write(frame)
    cv2.imshow("Video Kayit",frame)
    if cv2.waitKey(24) & 0xFF==ord('q'):
        break

camera.release()
writer.release()
cv2.destroyAllWindows()






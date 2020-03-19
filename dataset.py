import numpy as np
import cv2

vc = cv2.VideoCapture(0)
rval,frame = vc.read()


image_x = 330
image_y = 100
image_w = 250
image_h = 200

pic_no = 0
total_pic = 500

path = './DATA/1/'

flag_capruting = False

while True:
    if frame is not None:
        frame = cv2.flip(frame,1)

        cv2.rectangle(frame, (image_x, image_y), (image_x + image_w, image_y + image_h), (255,0,0),2)


        signal = frame[image_y:image_y + image_h, image_x:image_x + image_w]
        signal = cv2.cvtColor(signal,cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(signal,(11,11), 0)
        blur = cv2.medianBlur(blur,15)

        thresh = cv2.threshold(blur, 210,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        thresh = cv2.bitwise_not(thresh)

        cv2.imshow("Thresh", thresh)

        #cv2.imshow("Blur", blur)
        #cv2.imshow("Signal", signal)
        cv2.imshow("Image", frame)

        if flag_capruting:
            pic_no +=1
            save_img = cv2.resize(thresh, (50,50))
            save_img = np.array(save_img)
            cv2.imwrite(path + "/" + str(pic_no) + ".jpg", save_img)


    rval,frame = vc.read()
    keypress = cv2.waitKey(1)

    if pic_no == total_pic:
         flag_capruting = False
         break

    if keypress == ord('q'):
        break
    elif keypress == ord('c'):
        flag_capruting = True


vc.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
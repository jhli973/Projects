
import numpy as np
import cv2
import os

def get_image_from_video(video, out_put_path, freq):
    cap = cv2.VideoCapture(video)
    count = 1
    print(cap.isOpened())
    while cap.isOpened():
        ret, image = cap.read()

        if ret:
            # save image of every freq images
            if (count % freq) == 1:
                # trim some edge to make it a square
                image = image[0:480, 60:540]
                # resize the image at 250 x 250
                image = cv2.resize(image,(250, 250), interpolation=cv2.INTER_AREA)
                cv2.imwrite(os.path.join(out_put_path, "%d.jpg") % (count/freq), image)  # save frame as JPEG file
                print(count)
            count += 1

        else:
            break
        if cv2.waitKey(10) == 27:  # exit if Escape is hit
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Total {} images were captured".format(count / freq))

## run the program
video_name = 'Capture9.wmv'  #Capture_1.avi'
out_put_path = r"C:\Users\Jianhua\Desktop\images\capture9\\"
get_image_from_video(video_name,out_put_path, 2)
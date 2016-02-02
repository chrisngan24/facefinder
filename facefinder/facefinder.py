"""
Adopted from fideloper.com/facial-detection
by nkmst
"""

import cv2

IMAGE_OFFSET = 0.

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("./model/haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

    if len(rects) == 0:
        return [], img
    rects[:,2:] += rects[:,:2]
    return rects, img

def crop(rects, img, output_file_base):
    #Lazy logic: assume the biggest face is the current user
    max_size = 0
    max_coords = [0,0,0,0]
    x1, y1, x2, y2 = [0,0,0,0] 
    i = 0
    for x1, y1, x2, y2 in rects:
        #cv2.rectangle(img, (x1,y1), (x2, y2), (127,255,0), 2)
        cropped_img = img[y1: (y1 + (1+IMAGE_OFFSET)*(y2-y1)), x1:(x1 + (1+IMAGE_OFFSET)*(x2-x1))]
        output_file = '%s-%s.jpg' % (output_file_base, i)
        print 'writing to', output_file
        i+=1
        cv2.imwrite(output_file, cropped_img)

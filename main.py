# main.py
import cv2

def img_resize(image, w, h):
    return cv2.resize(image, (w, h))

def img_crop(image, startY, endY, startX, endX):
    return image[startY:endY, startX:endX]

def img_rotate(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, M, (w, h))

def img_flip(image, mode):
    return cv2.flip(image, mode)

def img_bright(image, beta):
    return cv2.convertScaleAbs(image, alpha=1.0, beta=beta)

def img_contrast(image, alpha):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def img_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def img_hsv(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def img_save(image, filename):
    cv2.imwrite(filename, image)
    return True

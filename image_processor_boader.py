import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"train\smoking_images\1953.jpg")

print(f'original img rows cols {img.shape}')
cv2.imshow('src', img)

# 保持纵横比例变成正方形
if img.shape[1] > img.shape[0]:
    top = 0
    left = 0
    bottom = img.shape[1] - img.shape[0]
    right = 0
if img.shape[0] > img.shape[1]:
    top = 0
    left = 0
    bottom = 0
    right = img.shape[0] - img.shape[1]  

# 填充按纵横比例，左上角为原图，右下角填充
img1 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT,value=[255,255,255])
img2 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_DEFAULT)
img3 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_ISOLATED)

# # 填充按纵横比例，左上角为原图，右下角填充（轴对称）
# img4 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT)
# img5 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT101)
# img6 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT_101)


img7 = cv2.copyMakeBorder(img, top, bottom, left, right,cv2.BORDER_WRAP)

# 填充按纵横比例，左上角为原图，右下角填充
img8  = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REPLICATE)
print(img1.shape)
cv2.imshow('BORDER_CONSTANT', img1)
cv2.imshow('BORDER_DEFAULT', img2)
cv2.imshow('BORDER_ISOLATED', img3)
# cv2.imshow('BORDER_REFLECT', img4)
# cv2.imshow('BORDER_REFLECT101', img5)
# cv2.imshow('BORDER_REFLECT_101', img6)
cv2.imshow('BORDER_WRAP', img7)
cv2.imshow('BORDER_REPLICATE', img8)

# 把图像处理成统一的尺寸
img_resize = cv2.resize(img2, (250, 250), interpolation=cv2.INTER_AREA)
print(img_resize.shape)
cv2.imshow('img_resize', img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()

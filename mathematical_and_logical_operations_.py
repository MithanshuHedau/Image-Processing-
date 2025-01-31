
# Addition
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
img1=cv2.imread('/content/add1.jpg',1)
img2=cv2.imread('/content/add2.jpg',1)
img11=cv2.resize(img1,(200,200))
print('IMAGE1')

cv2_imshow(img11)
img22=cv2.resize(img2,(200,200))
print('IMAGE2')

cv2_imshow(img22)
sum=cv2.add(img22,img11)
print('Addition of two images')
cv2_imshow(sum)
Sum1=cv2.imwrite('/content/drive/MyDrive/DIP Images/sum.jpg',sum)

# Substraction
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
img1=cv2.imread('/content/sub1.jpg',1)
img2=cv2.imread('/content/sub2.jpg',1)
image1=cv2.resize(img1,(200,200))
print('IMAGE1')

cv2_imshow(img11)
image2=cv2.resize(img2,(200,200))
print('IMAGE2')

cv2_imshow(img2)
Sub=cv2.subtract(image2,image1)
print('Substraction of two images')
cv2_imshow(Sub)
Sum1=cv2.imwrite('/content/drive/MyDrive/DIP Images/Sub.jpg',Sub)

# Getting again img2 back by subtarcting with the resultant image
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

img1 = cv2.imread('/content/add1.jpg', 1)
img2 = cv2.imread('/content/add2.jpg', 1)

img11 = cv2.resize(img1, (200, 200))
print('IMAGE1')
cv2_imshow(img11)

img22 = cv2.resize(img2, (200, 200))
print('IMAGE2')
cv2_imshow(img22)

sum_img = cv2.add(img22, img11)
print('Addition of two images')
cv2_imshow(sum_img)

result_subtraction = cv2.subtract(sum_img, img11)
print('Subtraction of images')
cv2_imshow(result_subtraction)

Subtracted_result = cv2.imwrite('/content/drive/MyDrive/DIP Images/subtracted_result.jpg', result_subtraction)

# Multiply
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
img1 = cv2.imread('/content/cameraman.jpg', 1)
print('Originsl Image')
cv2_imshow(img1)
result1=cv2.multiply(img1,2)
print('Multiply by 2')
cv2_imshow(result1)
result2=cv2.multiply(img1,3)
print('Multiply by 3')
cv2_imshow(result2)

# Divide
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
img1 = cv2.imread('/content/cameraman.jpg', 1)
print('Originsl Image')
cv2_imshow(img1)
result1=cv2.divide(img1,2)
print('Divide by 2')
cv2_imshow(result1)
result2=cv2.divide(img1,3)
print('Divide by 3')
cv2_imshow(result2)

#And Operation
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

img1 = cv2.imread('/content/Logical1.jpg', 1)
img2 = cv2.imread('/content/logical2.jpg', 1)

img11 = cv2.resize(img1, (180, 180))
print('ORIGINAL IMAGE ')
cv2_imshow(img1)

img22 = cv2.resize(img2, (180,180))
print('mask image ')
cv2_imshow(img2)

ANDING=cv2.bitwise_and(img11, img22)
print('AND OPERATION')
cv2_imshow(ANDING)

#OR Operation
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

img1 = cv2.imread('/content/Logical1.jpg', 1)
img2 = cv2.imread('/content/logical2.jpg', 1)

img11 = cv2.resize(img1, (180, 180))
print('ORIGINAL IMAGE ')
cv2_imshow(img1)

img22 = cv2.resize(img2, (180,180))
print('mask image ')
cv2_imshow(img2)

OR=cv2.bitwise_or(img11, img22)
print('OR OPERATION')
cv2_imshow(OR)

#XOR Operation
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

img1 = cv2.imread('/content/Logical1.jpg', 1)
img2 = cv2.imread('/content/logical2.jpg', 1)

img11 = cv2.resize(img1, (180, 180))
print('ORIGINAL IMAGE ')
cv2_imshow(img1)

img22 = cv2.resize(img2, (180,180))
print('mask image ')
cv2_imshow(img2)

XOR=cv2.bitwise_xor(img11, img22)
print('XOR OPERATION')
cv2_imshow(XOR)

#NOT Operation
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

img1 = cv2.imread('/content/NOT operation.jpg', 1)

print('ORIGINAL IMAGE ')
cv2_imshow(img1)

NOT=cv2.bitwise_not(img1)
print('NOT OPERATION')
cv2_imshow(NOT)

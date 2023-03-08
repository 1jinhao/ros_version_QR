import qrcode
import cv2
import numpy as np
str= ["四川省", "安徽省", "湖南省", "广东省", "浙江省", "江苏省", "福建省", "河南省","失效邮件"]



url="失效邮件"
img = qrcode.make(url, border=6)
img.save('QR_9.jpg')
#


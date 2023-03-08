import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont
img=cv2.imread('./my_chat.png')
font=ImageFont.truetype('./msyhbd.ttc',40)
WechatQRmodel = cv2.wechat_qrcode_WeChatQRCode('detect.prototxt', 'detect.caffemodel', 'sr.prototxt', 'sr.caffemodel')

codeinfo, pts = WechatQRmodel.detectAndDecode(img)
pts=np.int32(pts)
str= ["四川省", "安徽省", "湖南省", "广东省", "浙江省", "江苏省", "福建省", "河南省","失效邮件"]

# cv2.drawContours(img, pts, 1, [0, 0, 255], 2)
for i in range(len(codeinfo)):
    cv2.drawContours(img, pts, i, [0, 0, 255], 2)
    # print(i)
    # print(pts[i])
    for j in range(len(str)):
        if codeinfo[i].find(str[j])!=-1:
            print("第%d个:%s"%(i+1,str[j]))
            img_pil = Image.fromarray(img)
            draw = ImageDraw.Draw(img_pil)
            draw.text(pts[i][0], str[j], font=font, fill=(0, 0, 255))
            img = np.array(img_pil)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(pts)
# print(pts.shape)
# print(codeinfo[0].find('福建省'))
# print(codeinfo[0].find(str[-1]))
print(codeinfo)
# print(type(codeinfo))
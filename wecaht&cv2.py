import cv2
import numpy as np
from PIL import Image,ImageFont,ImageDraw

# import qrcode
#
# url='hello'
# img = qrcode.make(url, border=6)
# img.save('macbookPro.jpg')

# 使用opencv进行二维码识别
img = cv2.imread('./QR_QQ.jpg')
# QRmodel = cv2.QRCodeDetector()
# # start = time.time()
# codeinfo, pts, outs = QRmodel.detectAndDecode(img)
# # end = time.time()
# # print('time usage: ', end - start
#
# print(codeinfo, pts)
# cv2.drawContours(img, [np.int32(pts[0])], -1, (0, 0, 255), 2)
# cv2.imshow('QR', img)
# # cv2.imshow('straight_QR', outs)
# cv2.waitKey(0)
# print(outs.shape)
# cv2.destroyAllWindows()

# 使用wechat进行二维码识别
str= ["四川省", "安徽省", "湖南省", "广东省", "浙江省", "江苏省", "福建省", "河南省","失效邮件"]

font=ImageFont.truetype('./msyhbd.ttc',15)
cap = cv2.VideoCapture(0)
WechatQRmodel = cv2.wechat_qrcode_WeChatQRCode('detect.prototxt', 'detect.caffemodel', 'sr.prototxt', 'sr.caffemodel')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    codeinfo, pts = WechatQRmodel.detectAndDecode(img)

    pts = np.int32(pts)


    for i in range(pts.shape[0]):
        cv2.drawContours(frame, pts, i, [0, 0, 255], 2)

        for j in range(len(str)):
            if codeinfo[i].find(str[j]) != -1:
                frame_pil = Image.fromarray(frame)
                draw = ImageDraw.Draw(frame_pil)
                draw.text(pts[i][0], str[j], font=font, fill=(0, 0, 255))
                frame = np.array(frame_pil)
                # print("第%d个:%s"%(i+1,str[j]))
        # cv2.putText(frame, codeinfo[i], pts[i][0], cv2.FONT_HERSHEY_SIMPLEX, 1, [0, 0, 255], 2)
    # cv2.drawContours(frame, [np.int32(pts)], -1, (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()

# start = time.time()

# end = time.time()
print(codeinfo, pts)
# print('time usage: ', end - start)

# cv2.imshow('QR', img)
# cv2.waitKey(0)

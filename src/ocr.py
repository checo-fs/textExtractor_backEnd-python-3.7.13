import convertOCROutput
# import os
# import cv2
# from pdf2image import convert_from_path
# from paddleocr import PPStructure,draw_structure_result,save_structure_res,PaddleOCR, draw_ocr

# import layoutparser as lp

# #  Convert PDF to image
# images = convert_from_path('./doc/test3.pdf')

# for i in range(len(images)):
#     images[i].save('pages/page'+str(i)+'.jpg', 'JPEG')


# # Layout detection
# image = cv2.imread("pages/page0.jpg")
# image = image[..., ::-1]

# # load model
# model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config",
#                                 threshold=0.5,
#                                 label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"},
#                                 enforce_cpu=True,
#                                 enable_mkldnn=False)
# # detect
# layout = model.detect(image)

# for l in layout:
#     if l.type == 'Table':
#         x_1 = int(l.block.x_1)
#         y_1 = int(l.block.y_1)
#         x_2 = int(l.block.x_2)
#         y_2 = int(l.block.y_2)

#         break

# im = cv2.imread('pages/page1.jpg')

# cv2.imwrite('ext_im.jpg', im[y_1:y_2,x_1:x_2])


# OCR --->
# ocr = PaddleOCR(lang='en')
# image_path = 'pages/page0.jpg'
# image_cv = cv2.imread(image_path)
# image_height = image_cv.shape[0]
# image_width = image_cv.shape[1]
# output = ocr.ocr(image_path)
# print(output)
# <---


# for i in output:
#     print(output[0][0])

# for out in output:
#     print(out)
# boxes = [line[0] for line in output]
# texts = [line[1][0] for line in output]
# probabilities = [line[1][1][1] for line in output]



# for box in boxes:
#     print(box)


# texts = [line[1][0] for line in output]
# probabilities = [line[1][1] for line in output]

# image_boxes = image_cv.copy()

# for box in boxes:
#     cv2.rectangle(image_boxes, (int(box[0][0]),int(box[0][1])),(int(box[2][0]),int(box[2][1])),(0,0,255),1)

# cv2.imwrite('detections.jpg', image_boxes)






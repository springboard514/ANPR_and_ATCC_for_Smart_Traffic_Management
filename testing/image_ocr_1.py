import matplotlib.pyplot as plt

import image_ocr

# image-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = image_ocr.pipeline.Pipeline()

# Image path
img= ["D:\infosys_intern\STMS\data\ss3.png"]

pred = pipeline.recognize(img)
for predictions in pred:
    print(predictions)


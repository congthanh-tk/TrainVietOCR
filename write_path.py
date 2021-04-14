import os
from glob import glob

f = open("data.txt", "a")

impaths = glob('/home/thanh/Desktop/ToolTrainVietOCR/img/*')
impaths = sorted(impaths)
for impath in impaths:
    image_name = os.path.basename(impath)
    f.write(f"img/{image_name}\n")

f.close()

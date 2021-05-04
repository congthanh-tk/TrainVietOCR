import os
from glob import glob
import numpy as np
from PIL import Image
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg

config = Cfg.load_config_from_name('vgg_seq2seq')
config['weights'] = 'https://github.com/pbcquoc/vietocr/releases/download/v0.3.2/vgg-seq2seq.pth'
config['cnn']['pretrained']=False
# config['device'] = 'cuda:0'
config['device'] = 'cpu'
config['predictor']['beamsearch']=False

detector = Predictor(config)

f = open("train_data.txt", "a")

impaths = glob('/home/thanh/Documents/TrainVietOCR/img/*')
impaths = sorted(impaths)
for impath in impaths:
    image = Image.open(impath)
    image_name = os.path.basename(impath)
    # print(impath)

    s = detector.predict(image)
    # print(s)
    f.write(f"img/{image_name}\t{s}\n")

f.close()

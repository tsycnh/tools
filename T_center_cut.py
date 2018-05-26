# 该文件用来在图像中心进行裁切，输出为指定长宽比大小的图像
import os
import cv2
import numpy as np
import shutil
import utils

# 1. 载入文件夹目录下的所有bmp文件名 Done
# 2. 逐张文件处理
class CenterCut:
    # prison: 在prison内部进行roi提取，即生成的roi范围不能超出prison，格式: [x1,x2,y1,y2]
    def __init__(self, target_dir):
        parent_dir,tail = utils.get_parent_dir(target_dir)
        self.out_dir = parent_dir+'/'+tail+'_centercut/'
        utils.create_new_empty_dir(self.out_dir)
        self.load_images(target_dir)
        self.start_crop()

    def load_images(self, images_dir):
        r = os.listdir(images_dir)
        image_list = []
        for item in r:
            if item.split('.')[-1] == 'bmp':
                image_list.append(images_dir + '/' + item)
        # print(r)
        # print(image_list)
        self.image_list = image_list

    def generate_center_roi(self, width, height):

        if width >= height:
            x_left = int((width - height) / 2)
            x_right = x_left + height - 1
            y_top = 0
            y_bottom = height - 1
            rects = [x_left,y_top,height,height]
        else:
            x_left = 0
            x_right = width - 1
            y_top = int((height - width) / 2)
            y_bottom = y_top + width - 1
            rects = [x_left,y_top,width,width]
        return rects

    # 切割单张图、单个roi
    # 输入参数为原图、切割区域的左上角x,y坐标，切割区域的宽、高
    def crop_roi(self, img, x, y, width, height):
        x1 = x
        x2 = x1 + width
        y1 = y
        y2 = y1 + height
        return img[y1:y2, x1:x2]  # y1:y2,x1:x2

    def crop_rois(self, img, rects):
        rois = []
        for rect in rects:
            roi = self.crop_roi(img, rect[0], rect[1], rect[2], rect[3])
            rois.append(roi)

    def start_crop(self):
        if os.path.exists(self.out_dir):
            shutil.rmtree(self.out_dir)
        os.mkdir(self.out_dir)

        for i, image_path in enumerate(self.image_list):
            img = cv2.imread(image_path)
            height, width, channels = img.shape
            rects = self.generate_center_roi(width, height)
            roi_img = self.crop_roi(img, rects[0], rects[1], rects[2], rects[3])
            cv2.imwrite(self.out_dir + '/' + str(i) + '.jpg', roi_img)
            print('已保存', self.out_dir + '/' + str(i) + '.jpg')


if __name__ == '__main__':
    lc = CenterCut(target_dir='/Users/shidanlifuhetian/All/Tdevelop/cyclegan/datasets/KHB_ImgSets/train/水滴_sifted_w128_h128')

# 该文件用来在图像上随机裁切一些小图像
import os
import cv2
import numpy as np
import shutil
# 1. 载入文件夹目录下的所有bmp文件名 Done
# 2. 逐张文件处理
class LetsCrop:
    #prison: 在prison内部进行roi提取，即生成的roi范围不能超出prison，格式: [x1,x2,y1,y2]
    def __init__(self,prison,in_dir,out_dir,width,height,num):
        self.prison = prison
        self.out_dir = out_dir
        self.load_images(in_dir)
        self.rois = self.generate_rois(num, width, height)
        self.start_crop()
    def load_images(self,images_dir):
        r = os.listdir(images_dir)
        image_list = []
        for item in r:
            if item.split('.')[-1] == 'bmp':
                image_list.append(images_dir + '/' + item)
        # print(r)
        # print(image_list)
        self.image_list = image_list
    def generate_rois(self,num,width,height):

        x_left = self.prison[0]
        x_right = self.prison[1] - width
        y_top = self.prison[2]
        y_bottom = self.prison[3] - height
        rects = []
        for i in range(num):
            x = np.random.randint(x_left,x_right)
            y = np.random.randint(y_top,y_bottom)
            rect = [int(x),int(y),width,height]
            rects.append(rect)
        return rects

    # 切割单张图、单个roi
    # 输入参数为原图、切割区域的左上角x,y坐标，切割区域的宽、高
    def crop_roi(self,img,x,y,width,height):
        x1 = x
        x2 = x1 + width
        y1 = y
        y2 = y1 + height
        return img[y1:y2, x1:x2]  # y1:y2,x1:x2

    def crop_rois(self,img,rects):
        rois = []
        for rect in rects:
            roi = self.crop_roi(img,rect[0],rect[1],rect[2],rect[3])
            rois.append(roi)

    def start_crop(self):
        images_count = len(self.image_list)
        # all_roi_imgs = []
        if os.path.exists(self.out_dir):
            shutil.rmtree(self.out_dir)
        os.mkdir(self.out_dir)
        for i,roi in enumerate(self.rois):
            index = np.random.randint(0,images_count)
            img = cv2.imread(self.image_list[index])
            roi_img = self.crop_roi(img,roi[0],roi[1],roi[2],roi[3])
            cv2.imwrite(self.out_dir+'/'+str(i)+'.jpg',roi_img)
            print('已保存',self.out_dir+'/'+str(i)+'.jpg')


if __name__ =='__main__':
    lc = LetsCrop(prison=[536,2016,30,478],
                  in_dir='/Volumes/美美美美美美美美美美美酱 2/畕的东西/opencvimages/钢板样本/北海带钢完整样本/2号线1号相机bmp',
                  out_dir='./test',
                  width=400,
                  height=400,
                  num=2000)

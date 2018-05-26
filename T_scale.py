import cv2
import utils
import os
class Scale():
    def __init__(self,images_dir,scale=0,width=0,height=0,img_ext='bmp'):
        self.images_dir = images_dir
        self.scale = scale
        self.width = width
        self.height = height
        self.img_ext = img_ext
        parent_dir,tail = utils.get_parent_dir(images_dir)
        self.out_dir = os.path.join(parent_dir,tail+'_scale_'+str(scale)+'/')
        utils.create_new_empty_dir(self.out_dir)
        self.start_scale()
    def start_scale(self):
        self.images_list = utils.get_dir_filelist_by_extension(self.images_dir,self.img_ext)
        for i,f in enumerate(self.images_list):
            img = cv2.imread(f)
            height, width, channels = img.shape
            if self.scale != 0:
                new_img = cv2.resize(img,dsize=(0,0),fx=self.scale,fy=self.scale)
            if self.width !=0 and self.height==0:#按照宽度成比例缩放
                new_height = int((height/width)*self.width)
                new_img = cv2.resize(img,dsize=(self.width,new_height))
            if self.height !=0 and self.width == 0:
                new_width = int((width/height)*self.height)
                new_img = cv2.resize(img,dsize=(new_width,self.width))
            if self.height!=0 and self.width!=0:
                new_img = cv2.resize(img,dsize=(self.width,self.height))
            dst_name = self.out_dir+f.split('/')[-1]
            dst_name = dst_name.replace('.'+self.img_ext,'.jpg')
            cv2.imwrite(dst_name,new_img)
            print('已保存',dst_name)

if __name__ == '__main__':
    s = Scale(images_dir='/Users/shidanlifuhetian/All/Tdevelop/cyclegan/datasets/KHB_ImgSets/train/水滴_sifted_w128_h128_centercut',width=128,img_ext='jpg')
# 依据一定条件筛选图片
import utils
import os
import cv2
class Sift():
    def __init__(self,images_dir,ratio_limit=(0.5,2),min_width=128,min_height=128,img_ext='bmp'):
        self.images_dir = images_dir
        self.ratio_limit = ratio_limit   # 宽高比 ratio = w/h
        self.min_width = min_width
        self.min_height = min_height
        self.img_ext = img_ext
        parent_dir,tail = utils.get_parent_dir(images_dir)
        self.out_dir = os.path.join(parent_dir,tail+'_sifted_w'+str(self.min_width)+'_h'+str(self.min_height)+'/')
        utils.create_new_empty_dir(self.out_dir)
        self.start_sift()
    def start_sift(self):
        self.images_list = utils.get_dir_filelist_by_extension(self.images_dir,self.img_ext)
        for i,f in enumerate(self.images_list):
            img = cv2.imread(f)
            height, width, channels = img.shape
            ratio = width/height
            if height >= self.min_height \
                    and width >= self.min_width \
                    and ratio >= self.ratio_limit[0] \
                    and ratio <= self.ratio_limit[1]:
                dst_name = self.out_dir+f.split('/')[-1]
                # dst_name = dst_name.replace('.'+self.img_ext,'.jpg')
                cv2.imwrite(dst_name,img)
                print('已保存',dst_name)

if __name__ == '__main__':
    s = Sift(images_dir='/Users/shidanlifuhetian/All/Tdevelop/cyclegan/datasets/KHB_ImgSets/train/水滴')
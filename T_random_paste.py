# 随机粘贴工具
# TODO : 粘贴前景图的同时生成当前图的标记（Pascal格式xml）
import cv2
import utils
import random
import os
from pascal_voc_io import PascalVocWriter

class LetsPaste():
    def __init__(self,bg_dir,rect_dir,total_num,pic_min,pic_max):
        self.bg_dir = bg_dir
        self.rect_dir = rect_dir
        self.total_num = total_num
        self.pic_min = pic_min
        self.pic_max = pic_max
    def start_paste(self):
        parent_dir, tail = os.path.split(os.path.abspath(self.bg_dir))  # 使用abspath函数先规范化路径
        utils.create_new_empty_dir(parent_dir+'/magic_imgs/')
        for i in range(self.total_num):
            magic_pic = self.paste_one_bg()
            img_name = parent_dir+'/magic_imgs/'+str(i)+'.jpg'
            cv2.imwrite(img_name,magic_pic)
            print('magic saved:',img_name)
    def get_class_by_name(self,file_name):
        purename = file_name.split('.')[-2].split('/')[-1]
        c_name = purename[0:2]
        return c_name
    def paste_one_bg(self):
        #读取背景图及前景图
        bg_names = utils.get_dir_filelist_by_extension(self.bg_dir,'jpg')
        rect_names = utils.get_dir_filelist_by_extension(self.rect_dir,'jpg')
        rect_num = random.randint(self.pic_min,self.pic_max)
        bg = cv2.imread(random.choice(bg_names))
        random_rects_name = random.choices(rect_names,k=rect_num)
        self.rect_classes = []
        for rect_name in random_rects_name:
            rect_class = self.get_class_by_name(rect_name)
            self.rect_classes.append(rect_class)
        all_rects = []
        if rect_num > 0:
            for rect in random_rects_name:
                all_rects.append(cv2.imread(rect))
            #生成待粘贴区域
            while True:
                rois = utils.generate_rects(num=rect_num,
                                     width=all_rects[0].shape[0],
                                     height=all_rects[0].shape[1],
                                     prison=[0,0,bg.shape[0],bg.shape[1]])
                print('roi num:',len(rois))
                if self.interaction_rects(rois) == True:
                    print('有相交')
                else:
                    print('无相交')
                    print(rois)
                    break
            #开始粘贴
            for i,roi in enumerate(rois):
                x1,y1,x2,y2 = roi[0],roi[1],roi[2],roi[3]

                bg[y1:y2, x1:x2] = all_rects[i] # y1:y2,x1:x2
            self.rois = rois
        return bg

    def interaction_rects(self,rects):
        interact = False # False 表示无相交，True表示有相交
        if len(rects)<=1:
            return interact
        for i in range(len(rects)-1):
            for j in range(i+1,len(rects)):
                if utils.rect_interaction(rects[i],rects[j]) > -1:
                    interact = True
                    break
        return interact

class LetsPasteWithLabel(LetsPaste):
    def gen_voc_label(self,folder_name,file_name,img_size,img_path):
        writer = PascalVocWriter(folder_name, file_name+'.jpg', img_size, localImgPath=img_path)
        difficult = 0
        for i,roi in enumerate(self.rois):
            writer.addBndBox(roi[0],roi[1],roi[2],roi[3], self.rect_classes[i], difficult)
        writer.save(folder_name+'/'+file_name+'.xml')
        print('labelxml saved:',folder_name+'/'+file_name+'.xml')

    def start_paste(self):
        parent_dir, tail = os.path.split(os.path.abspath(self.bg_dir))  # 使用abspath函数先规范化路径
        utils.create_new_empty_dir(parent_dir+'/magic_imgs/')
        for i in range(self.total_num):
            magic_pic = self.paste_one_bg()
            img_name = parent_dir+'/magic_imgs/'+str(i)+'.jpg'
            cv2.imwrite(img_name,magic_pic)
            print('magic saved:',img_name)
            self.gen_voc_label(folder_name=parent_dir+'/magic_imgs/',file_name=str(i),img_size=magic_pic.shape,img_path=img_name)

if __name__ == '__main__':
    # lp = LetsPaste(bg_dir='./test',rect_dir='./rois',total_num=100,pic_min=1,pic_max=3)
    # lp.start_paste()
    lpwl = LetsPasteWithLabel(bg_dir='/Users/shidanlifuhetian/All/data/purebg_400',
                              rect_dir='/Users/shidanlifuhetian/All/Tdevelop/cyclegan/translation/',
                              total_num=100,pic_min=1,pic_max=3)
    lpwl.start_paste()
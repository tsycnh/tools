import os
import utils
import random
import shutil
class LetsSplit():
    def __init__(self,dir,train_count):
        self.dir = dir
        self.file_list = utils.get_dir_filelist_by_extension(self.dir,ext='jpg')
        self.parent_dir,tail = os.path.split(os.path.abspath(self.dir))# 使用abspath函数先规范化路径
        random.shuffle(self.file_list)
        self.train_count = train_count
        self.start_split()
    def start_split(self):
        dir_A = self.parent_dir+'/train'
        dir_B = self.parent_dir+'/test'
        utils.create_new_empty_dir(dir_A)
        utils.create_new_empty_dir(dir_B)
        for i,file in enumerate(self.file_list):
            _,name = os.path.split(file)
            if i < self.train_count:
                dst = dir_A+'/'+name
            else:
                dst = dir_B+'/'+name
            shutil.copy(file,dst)
            print('已拷贝：',dst)

if __name__ =='__main__':
    ls = LetsSplit('/Users/shidanlifuhetian/All/Tdevelop/Keras-GAN/cyclegan/datasets/plates/trainB',train_count=1500)
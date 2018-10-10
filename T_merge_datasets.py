# 将分类标记好bbox的图像一股脑的放在一起，并规范化命名
import sys
import utils
import os
import shutil
import random

if __name__ == "__main__":
    root_dir = sys.argv[1]
    parent_dir,_ = utils.get_parent_dir(root_dir)
    target_dir = os.path.join(parent_dir,'results')
    utils.create_new_empty_dir(target_dir)
    os.mkdir(os.path.join(target_dir,'images'))
    os.mkdir(os.path.join(target_dir,'annotations'))
    sub_dirs = utils.get_immediate_subdirectories(root_dir)

    total_count = 0
    for sub_dir in sub_dirs:
        sub_dir = os.path.join(root_dir,sub_dir)
        image_dir = os.path.join(sub_dir,'images')
        image_file_list = utils.get_dir_filelist_by_extension(image_dir,'bmp')
        total_count+=len(image_file_list)
    print('图像总数：%d'%total_count)
    file_paths=[]
    for i in range(1,total_count+1):
        new_name = utils.fixed_length(i,4)
        a = {
            'image':        os.path.join(target_dir,'images',new_name+'.bmp'),
            'annotation':   os.path.join(target_dir,'annotations',new_name+'.xml')
        }
        file_paths.append(a)
    random.seed(1)
    random.shuffle(file_paths)
    image_index = 0
    for sub_dir in sub_dirs:
        sub_dir = os.path.join(root_dir,sub_dir)
        image_dir = os.path.join(sub_dir,'images')
        anno_dir = os.path.join(sub_dir,'annotations')
        image_file_list = utils.get_dir_filelist_by_extension(image_dir,'bmp')
        for image_file in image_file_list:
            anno_file = image_file.replace('bmp','xml').replace('images','annotations')
            shutil.copy2(image_file,file_paths[image_index]['image'])
            shutil.copy2(anno_file,file_paths[image_index]['annotation'])
            image_index+=1
            print(image_file+' 已拷贝')
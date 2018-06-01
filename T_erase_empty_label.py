import xml.etree.ElementTree as ET
import utils
import os
import sys
import shutil
# 工具作用：批量移除没有bbox的标记文件。标记文件应为xml文件，格式为pascal voc标准格式。
# 同时将标签对应的图像拷贝到上层目录下的images文件夹下
# 使用方法：python /path/to/this_file.py folder_path
# folder_path 中所有不包含object标签的xml都会被删除
def delete_empty_label(labels_folder_path):
    file_list = utils.get_dir_filelist_by_extension(dir=labels_folder_path, ext='xml')
    # print(file_list)
    delete_list = []
    good_labels_count = 0
    for file in file_list:

        tree = ET.ElementTree(file=file)
        root = tree.getroot()

        contains_label = False
        for elem in tree.iter(tag='object'):
            contains_label = True
        if not contains_label:
            delete_list.append(file)
        else:
            good_labels_count += 1

    for file in delete_list:
        os.remove(file)
        print(file + ' 已删除')

    print('保留下来的标记文件共有%d个' % good_labels_count)
def export_image_and_label(labels_folder_path):
    parent_dir,_ = utils.get_parent_dir(labels_folder_path)
    target_dir = utils.create_new_empty_dir(parent_dir+'/images/')
    file_list = utils.get_dir_filelist_by_extension(dir=labels_folder_path, ext='xml')
    for file in file_list:
        tree = ET.ElementTree(file=file)
        for elem in tree.iter(tag='path'):
            full_path = elem.text
        for elem in tree.iter(tag='filename'):
            file_name = elem.text
        try:
            shutil.copy2(src=full_path,dst=target_dir+'/'+file_name)
        except:
            print(full_path+'复制失败')

def export_image_and_label_selfdefine(labels_folder_path,images_folder):
    parent_dir, _ = utils.get_parent_dir(labels_folder_path)
    target_dir = utils.create_new_empty_dir(parent_dir + '/images/')
    file_list = utils.get_dir_filelist_by_extension(dir=labels_folder_path, ext='xml')
    for file in file_list:
        tree = ET.ElementTree(file=file)

        for elem in tree.iter(tag='filename'):
            file_name = elem.text
        full_path = images_folder+'/'+file_name
        try:
            shutil.copy2(src=full_path, dst=target_dir + '/' + file_name)
        except:
            print(full_path + '复制失败')
if __name__ == "__main__":
    delete_empty_label(sys.argv[1])
    export_image_and_label(sys.argv[1])
import xml.etree.ElementTree as ET
import utils
import os
import sys
# 工具作用：批量移除没有bbox的标记文件。标记文件应为xml文件，格式为pascal voc标准格式。
# 使用方法：python /path/to/this_file.py folder_path
# folder_path 中所有不包含object标签的xml都会被删除
if __name__ == "__main__":
    file_list = utils.get_dir_filelist_by_extension(dir=sys.argv[1],ext='xml')
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
            good_labels_count +=1

    for file in delete_list:
        os.remove(file)
        print(file+' 已删除')

    print('保留下来的标记文件共有%d个' % good_labels_count)
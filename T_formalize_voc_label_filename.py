import xml.etree.ElementTree as ET
import utils
import os
import sys
def change_tag_text(file_list,target_dir):

    for file in file_list:
        tree = ET.ElementTree(file=file)
        root = tree.getroot()
        # print(root.tag)
        # print(root.attrib)
        print(file)
        for elem in tree.iter(tag='path'):
            # file_name = elem.text
            # index = file_name.find('.')
            # ext = file_name[index:]
            _,fn = utils.get_parent_dir(file)
            fn = fn.replace('xml','bmp')
            elem.text = ''
            # print(elem.text)

        tree.write(target_dir + os.path.basename(file))


if __name__ == "__main__":
    xmls_dir = '/Users/shidanlifuhetian/All/data/KHB_ANNO/USTB中厚板检测数据集/test/xmls1'

    # 工具作用：规范xml内容，filename规范为真实文件名
    file_list = utils.get_dir_filelist_by_extension(dir=xmls_dir,ext='xml')
    parent_dir,_ =utils.get_parent_dir(xmls_dir)
    utils.create_new_empty_dir(parent_dir+'/xmls2/')
    target_dir = parent_dir+'/xmls2/'
    change_tag_text(file_list,target_dir)
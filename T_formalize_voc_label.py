import xml.etree.ElementTree as ET
import utils
import os
import sys
def change_tag_text(file_list,tag,new_text,target_dir):

    for file in file_list:
        tree = ET.ElementTree(file=file)
        root = tree.getroot()
        # print(root.tag)
        # print(root.attrib)
        print(file)
        for elem in tree.iter(tag=tag):
            file_name = elem.text
            index = file_name.find('.')
            ext = file_name[index:]
            if ext != new_text:
                elem.text = new_text
            # print(elem.text)

        tree.write(target_dir + os.path.basename(file))


if __name__ == "__main__":
    xmls_dir = sys.argv[1]
    tag = sys.argv[2]
    new_text = sys.argv[3]
    # 工具作用：针对一些标签没有写文件扩展名的，给他加上。
    file_list = utils.get_dir_filelist_by_extension(dir=xmls_dir,ext='xml')
    parent_dir,_ =utils.get_parent_dir(xmls_dir)
    utils.create_new_empty_dir(parent_dir+'/xmls/')
    target_dir = parent_dir+'/xmls/'
    change_tag_text(file_list,tag,new_text,target_dir)
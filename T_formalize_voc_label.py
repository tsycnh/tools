import xml.etree.ElementTree as ET
import utils
import os

file_list = utils.get_dir_filelist_by_extension(dir='/Users/shidanlifuhetian/All/data/NEU-DET/ANNOTATIONS',ext='xml')
# print(file_list)
for file in file_list:
    tree = ET.ElementTree(file=file)
    root = tree.getroot()
    print(root.tag)
    print(root.attrib)
    for elem in tree.iter(tag='filename'):
        file_name = elem.text
        index = file_name.find('.')
        ext = file_name[index:]
        if ext != '.jpg':
            elem.text += '.jpg'
        print(elem.text)

    tree.write('./labels/'+os.path.basename(file))

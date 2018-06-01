import os
import shutil
import numpy as np

'''
所有的矩形坐标规范为：[xmin,ymin,xmax,ymax]，即左上角坐标加右下角坐标
'''

def get_immediate_subdirectories(a_dir):
  return [name for name in os.listdir(a_dir)
    if os.path.isdir(os.path.join(a_dir, name))]

# 获取某一文件夹下的所有文件夹，各种深度的文件夹都可以得到
def get_all_dirs(base_dir, output=[]):
    base_dir=os.path.abspath(base_dir)
    current_dir = base_dir
    subdirs = get_immediate_subdirectories(current_dir)
    if len(subdirs) != 0:
        for subdir in subdirs:
            # print(base_dir+'/'+subdir)
            output.append(base_dir + '/' + subdir)
            get_all_dirs(base_dir +'/' + subdir, output)
    return output


def get_dir_filelist_by_extension(dir, ext):
    r = os.listdir(dir)
    file_list = []
    for item in r:
        if item.split('.')[-1] == ext:
            file_list.append(dir + '/' + item)
    return file_list

def get_parent_dir(dir):
    parent_dir, tail = os.path.split(os.path.abspath(dir))  # 使用abspath函数先规范化路径
    return parent_dir,tail


def create_new_empty_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)
    return dir


# 判断两矩形是否相交，若相交返回相交面积，否则返回-1,gap表示两个矩形之间如果有gap大小的距离也算相交
def rect_interaction(rect1, rect2, gap=0):
    #  rect1 = [x1,y1,x2,y2]  x1,y1 左上角矩形坐标 x2,y2 右下角矩形坐标
    x1, y1, x2, y2 = rect1[0] - gap, rect1[1] - gap, rect1[2] + gap, rect1[3] + gap
    x3, y3, x4, y4 = rect2[0] - gap, rect2[1] - gap, rect2[2] + gap, rect2[3] + gap

    a = max(x1, x3)
    b = min(x2, x4)
    c = max(y1, y3)
    d = min(y2, y4)

    if a - b <= 0 and c - d <= 0:
        return (b - a) * (d - c)
    else:
        return -1


# 生成num个随机位置的矩形区域，每个矩形区域大小为width*height，坐标范围是prison内
def generate_rects(num,width,height,prison):

    x_left = prison[0]
    x_right = prison[2] - width
    y_top = prison[1]
    y_bottom = prison[3] - height
    rects = []
    for i in range(num):
        x = np.random.randint(x_left,x_right)
        y = np.random.randint(y_top,y_bottom)
        rect = [int(x),int(y),int(x)+width,int(y)+height]
        rects.append(rect)
    # rect格式: [xmin,ymin,xmax,ymax]
    return rects

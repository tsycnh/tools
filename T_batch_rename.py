
from utils import *
from shutil import *
if __name__ == "__main__":
    folder = "/Users/shidanlifuhetian/All/data/KHB_ANNO/VS"
    ext = "bmp"
    targetfolder = get_parent_dir(folder)[0]+"/renamed"
    targetfolder = create_new_empty_dir(targetfolder)
    filelist = get_dir_filelist_by_extension(folder,ext)
    for i in range(len(filelist)):
        src = filelist[i]
        dst = targetfolder+"/"+fixed_length(3000+i,4)+"."+ext
        copy2(src,dst)
        print("已拷贝：",dst)
    print("完成")

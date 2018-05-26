# 批量转换现场的img、cimg格式图像为bmp
# 通过调用外部exe来实现

import utils
import subprocess

if __name__ == '__main__':
    dirlist = utils.get_all_dirs('/Users/shidanlifuhetian/All/学习/学术生涯/写文章')

    for d in dirlist:
        target_dir = d.replace('学术生涯','诶嘿嘿888')
        subprocess.run(['/Applications/Calculator.app/Contents/MacOS/Calculator','args'])
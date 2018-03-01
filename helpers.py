# 一些写程序用的辅助工具，这里面的函数不会用在正式发布使用的程序中
import cv2

def draw_rects(rects,bg):
    for rect in rects:
        cv2.rectangle(bg,pt1=(rect[0],rect[1]),pt2=(rect[2],rect[3]),color=(0,0,255))
    return bg
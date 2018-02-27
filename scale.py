import cv2
import utils
class Scale():
    def __init__(self,images_dir,scale):
        self.images_dir = images_dir
        self.scale = scale
        self.out_dir = images_dir+'/scale_'+str(scale)+'/'
        utils.create_new_empty_dir(self.out_dir)
        self.start_scale()
    def start_scale(self):
        self.images_list = utils.get_dir_filelist_by_extension(self.images_dir,'jpg')
        for i,f in enumerate(self.images_list):
            img = cv2.imread(f)
            new_img = cv2.resize(img,dsize=(0,0),fx=self.scale,fy=self.scale)
            cv2.imwrite(self.out_dir+str(i)+'.jpg',new_img)
            print('已保存',self.out_dir+str(i)+'.jpg')

if __name__ == '__main__':
    s = Scale(images_dir='./test2',scale=2)

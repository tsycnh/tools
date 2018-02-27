* random_cut.py   用来对图像做随机的裁切，支持批量操作  
用法：
```
    lc = LetsCrop(prison=[536,2016,30,478],     #在prison区域内进行roi提取，格式[xmin,xmax,ymin,ymax]
                  in_dir='/path/to/indir',      #批量图像所在的文件夹（支持bmp格式）
                  out_dir='/path/to/outdir',    #裁切后图像保存再哪里
                  width=400,                    #裁切roi区域的宽度
                  height=400                    #裁切roi区域的高度
                  num=1000)                     #要生成的roi个数
```

程序首先在prison范围内生成num个roi区域，然后每次依据roi区域进行切割的时候，都会从in_dir内随机拿出一张图片进行切割，并存储切割结果。直到所有的roi
都切割完毕。  

================
* scale.py 按比例对图像进行批量缩放  支持jpg格式图像  
用法：
```python
    s = Scale(images_dir='./test2',#存有目标图像的目录
                scale=2)#缩放尺度如2、3为扩大2、3倍。0.5,0.25为缩小一半、四分之一
```
输出的图像会在images_dir下的新目录内，名为 scale_2、scale_0.5等等  

==================
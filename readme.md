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

* random_paste.py 在一张背景图上随机粘贴一定数量的前景图，支持jpg。批量随机操作

用法：

```python
    lp = LetsPaste(bg_dir='/path/to/bg/dir',    # 背景图图像目录
                    rect_dir='/path/to/obj/dir',# 前景图图像目录
                    total_num=100,              # 一共要生成多少张新图   
                    pic_min=1,                  # 每张bg上至少几个前景（包含）
                    pic_max=3)                  # 每张bg上之多几个前景（包含）
    lp.start_paste()  
```

每生成一张新bg都是先从背景图库里随机选一张，从前景图库随机选pic_min~pic_max张，
然后随机将这几张图粘贴到bg上，并保证几个前景不重叠。然后输出图像至bg目录同等级的magic_imgs目录下

带pascal voc标签的用法
```
    lpwl = LetsPasteWithLabel(bg_dir='/path/to/bg/dir',#大图
                              rect_dir='/path/to/roi/dir',#往大图上粘贴的小图
                              total_num=100,pic_min=1,pic_max=3)
    lpwl.start_paste()
```
标签的输出也是引用自labelImg  
会在每张新图像的同层次目录下保存同名的xml，符合Pascal Voc的bounding box标记格式，可以用labelimg程序进行查看 https://github.com/tzutalin/labelImg

================

* scale.py 按比例对图像进行批量缩放  输出均为jpg格式图像  
用法：
```python
    s = Scale(images_dir='/path/to/img/dir',#存有目标图像的目录
    width=128,
    img_ext='jpg')# 目标扩展名
```
四种用法：
1. **仅**设置scale值，其他留空，那么将按照scale成比例缩放，如0.5,2
2. 仅设置width值，其他留空，将按照新的width值成比例缩放
3. 仅设置height值，其他留空，将按照新的height值成比例缩放
4. 同时设置width、height值，其他留空，按照新的width、height强制缩放


输出的图像会在images_dir同等级目录内，名为 ~_scale_2、~_scale_0.5等等  

==================

* dataset_split.py  对图像数据库进行训练集和测试集的拆分

用法：
```python
    ls = LetsSplit('/path/to/dir',#含有图像的目录
                    train_count=1500)#训练集图像数量
```

程序会读取目标目录里的所有jpg图像，并将train_count数目的图像拷贝到同等级的train目录下，剩余的图像拷贝到
同等级的test目录下。所有的图像顺序都是随机打乱的

==================

* sift.py 对图像进行筛选，依据图像大小即长宽比

用法
```

```
===================
* center_cut.py 在图像中心切割最大的正方形

===================
* steel_img_batch_convert.py 批量的用杨老师的软件来将img图像转换成bmp图像
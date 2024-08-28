# https://blog.csdn.net/qq_45806961/article/details/138196945
# 优化了npz文件命名方式，增加了读取图片是否成功的判断语句，增加了判断npz文件保存文件夹是否存在（如不存在则创建）的语句
# 把img图像和对应的mask图像合并为一个npz文件
# 如果更换数据集，就需要更改这里，根据数据集的相关名称进行更改
 
import glob
import os
import cv2
import numpy as np
from tqdm import tqdm
 
def npz():
    path = r'E:\0012 - 20240810 - multi-water seg\dataset\dataset_8images_testNet\train\*.png'                                     # 图像路径
    output_path  = r'E:\0012 - 20240810 - multi-water seg\dataset\dataset_8images_testNet_npz'  
    
    # 项目中存放训练所用的npz文件路径
    if not os.path.exists(output_path):
        os.makedirs(output_path)  # 如果输出路径不存在，则创建
    
    for i,img_path in tqdm(enumerate(glob.glob(path))):
        if img_path.endswith('_label.png'):                     # 没有读取标签图片，提前给跳过
            continue
 
        image = cv2.imread(img_path)
        if image is None:
            print(f"Error: Failed to load image {img_path}. Skipping...")
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
        label_path = img_path.replace('.png', '_label.png')      # 读取标签图片
        print(label_path)
        label = cv2.imread(label_path,flags=0)                   # flags 默认读取灰度图像
 
        filename = os.path.basename(img_path)                   # 获取文件的基本名称 (包括扩展名)
        filename = os.path.splitext(filename)[0]                # 去除扩展名，保留文件名
        
        npz_filename = os.path.join(output_path, f"{filename}.npz")  # 构造完整的输出文件路径
        
        
        np.savez(npz_filename, image=image, label=label)        # 保存为 .npz 文件

 
npz()

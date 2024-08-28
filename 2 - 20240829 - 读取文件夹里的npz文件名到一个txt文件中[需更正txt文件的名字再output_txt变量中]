# line25的xxx.txt中，xxx为文件名，需修改为train或test或val等。只需要修改好名字，如果没有，会自动创建；如果已有txt，则会覆盖式的写入（已测试）

import os
import glob

def save_npz_filenames_to_txt(npz_folder, output_txt):
    # 确保输出路径的父文件夹存在
    os.makedirs(os.path.dirname(output_txt), exist_ok=True)
    
    # 获取指定文件夹中的所有 .npz 文件路径
    npz_files = glob.glob(os.path.join(npz_folder, '*.npz'))
    
    # 提取文件名（不带路径和后缀）
    filenames = [os.path.splitext(os.path.basename(npz_file))[0] for npz_file in npz_files]
    
    # 将文件名保存到 txt 文件中
    with open(output_txt, 'w') as f:
        for filename in filenames:
            f.write(filename + '\n')

# 示例用法
npz_folder = r'E:\0012 - 20240810 - multi-water seg\dataset\dataset_8images_testNet_npz'  # npz 文件所在的文件夹路径

# 此处需要修改xxx！！！
output_txt = r'E:\0012 - 20240810 - multi-water seg\codes\ST-UNet-main\lists\lists_Water_8images_testNet\xxx.txt'  # 输出 txt 文件的路径

save_npz_filenames_to_txt(npz_folder, output_txt)

#!/bin/python
# -*- coding: utf-8 -*-
# Author: CWSun @ 20200518
# Needs openCV 4.2.0 with python 3.7+
from pathlib import Path
import numpy as np
import cv2 as cv

# ===== 手動輸入部分 Manual input =====
# 設定影像路徑
base_dir = Path(r"./samples") # 建議填完整路徑
# 檔案清單，注意：垂直的先放
img_path = [base_dir/"0_0.jpg",base_dir/"1_0.jpg",base_dir/"2_0.jpg",
            base_dir/"0_1.jpg",base_dir/"1_1.jpg",base_dir/"2_1.jpg",]
ver = 3; hor = 2
output_filename="MergedTif.tif"

# ===== 主程式 Main script =====
# Check dimension
if len(img_path) != ( ver * hor):
    raise ValueError("[Error] Insufficient image files.")
# Detect the dimension by reading first image
img0 = cv.imread(str(img_path[0]))
if img0 is None:
    print(f"Cannot open the file {img_path[0]}. Please use ascii characters only.")
    print(f"無法開啟檔案 {img_path[0]}，請確認檔案路徑並'不含'非英文字元。")
    raise ValueError(f"Cannot open the file {img_path[0]}. Please use ascii characters only.")
rows, cols, deps = (None,None,None)
if img0.ndim == 3:
    rows, cols, deps = img0.shape
    # Allocate memory
    img_f = np.zeros(shape=(rows*ver,cols*hor,3),dtype=img0.dtype)
    del img0
    # Fillin the data
    for j in range(hor):
        # hor
        for i in range(ver):
            # col
            print(f"Reading {str(img_path[j*ver+i])}")
            imgi = cv.imread(str(img_path[j*ver+i]))
            img_f[rows*i:rows*(i+1),cols*j:cols*(j+1),:] = imgi
            del imgi

elif img0.ndim == 2:
    # Not tested yet
    rows, cols = img0.shape
    # Allocate memory
    img_f = np.zeros(shape=(rows*ver,cols*hor),dtype=img0.dtype)
    del img0
    # Fillin the data
    for j in range(hor):
        # hor
        for i in range(ver):
            # col
            print(f"Reading {str(img_path[j*ver+i])}")
            imgi = cv.imread(str(img_path[j*ver+i]))
            img_f[rows*i:rows*(i+1),cols*j:cols*(j+1)] = imgi
            del imgi
    

else:
    raise ValueError("[Dimension Error]")

# Save image
print(f"Saving image to {str(base_dir/output_filename)}")
cv.imwrite(str(base_dir/output_filename),img_f)
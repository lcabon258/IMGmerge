# immergeCV 使用 openCV 拼接多張影像  
---    
## 目的
拼接影像（不做任何幾何轉換）  
## 需要的函式庫  
* Python 3.7+ (Tested in 3.8)  
* OpenCV 4.2.0 (Tested in 4.2.0)  
* Numpy  
## 首次安裝環境時  
使用 conda：  
```conda create -n cv -c conda-forge python=3.8 opencv=4.2.0  numpy```  
## 執行  
1. 首先編輯檔案第10-17行：  
    * base_dir : 設定影像儲存路徑。  
    * img_path : 要處理的影像，注意：程式是以「欄優先」合併，即先往下，再往右的順序。
    * ver : 垂直影像張數（列數）。
    * hor : 水瓶影像張數（欄數）。
    * output_filename : 輸出的檔名。
2. 請依據路徑中是否有非英文路徑，若有的話請使用 [immergeCV2.py](./immergeCV2.py)，否則使用 [immergeCV.py](./immergeCV.py)。  
3. 執行：  
啟用環境：  
```  
conda activate cv  
```  
執行程式：  
```  
python immergeCV.py
```  
結束時：  
```  
conda deactivate
```  

## 範例影像  

![範例拼接影像](./samples/MergedTif.jpg)
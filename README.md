# desk-coin-ATM

## 目錄

-   [專案介紹](#專案介紹)
-   [硬體介紹](#硬體介紹)
-   [準備](#準備)
-   [功能和程式](#功能和程式)
-   [使用方法](#使用方法)
-   [參考資料](#參考資料)

## 專案介紹
結合硬幣分類系統以及伺服馬達控制硬幣落下，並配合臉部識別系統，製造簡易版的桌上ATM

## 硬體介紹
### 材料清單
* Rasberry Pi 4 x 1
* Rasberry Pi Camera Module x 1
* 麵包板 x 1
* 5mm光敏電阻 x 4
* led(非常亮) x 4
* 伺服馬達 x5

### 硬體組成
- 將硬幣進行分流
  
![image](https://github.com/user-attachments/assets/e7ccc52b-fa1c-4425-a27a-25a91fd49521)

- LDR與伺服馬達組奘

![image](https://github.com/user-attachments/assets/588cd55a-b496-4820-a3a4-939c22356380)
![image](https://github.com/user-attachments/assets/880692e2-2e0b-46a2-a438-bb6499a72184)

- 全部組合在一起
  
   ![image](https://github.com/user-attachments/assets/c27870c3-cbd9-423b-a468-22c05768236e)

## 準備

首先，具備Raspbian Buster OS之樹梅派4B，並確保內含Python版本為3

### 安裝Open-CV

用下列指令將CONF_SWAPSIZE = 100變更為CONF_SWAPSIZE=2048
```bash
sudo nano /etc/dphys-swapfile
```

安裝+解壓，其中最後一步會執行一個多小時，請耐心等待
```bash
sudo apt-get install build-essential cmake pkg-config

sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libgtk2.0-dev libgtk-3-dev

sudo apt-get install libatlas-base-dev gfortran

sudo pip3 install numpy

wget -O opencv.zip https://github.com/opencv/opencv/archive/4.4.0.zip

wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.4.0.zip

unzip opencv.zip

unzip opencv_contrib.zip

cd ~/opencv-4.4.0/

mkdir build

cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \ -D CMAKE_INSTALL_PREFIX=/usr/local \ -D INSTALL_PYTHON_EXAMPLES=ON \ -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-4.4.0/modules \ -D BUILD_EXAMPLES=ON ..

make -j $(nproc)
```

### 安裝需要的套件
```bash
sudo pip3 install telepot

sudo pip3 install face_recognition

sudo pip3 install imutils

sudo pip3 install pickle

sudo pip3 install cv2

sudo pip3 install os

sudo pip3 install ast
```

### 建立臉部辨識資料庫
1. 從github匯入資料庫
```bash
git clone https://github.com/carolinedunn/facial_recognition
```

2. 匯入後開啟其中的headshots_picam.py

![image](https://github.com/user-attachments/assets/21d31161-1a3d-4ca5-bcaa-8e53a6bcfc42)

3. 將其中name的部分改成你希望的名字

![image](https://github.com/user-attachments/assets/d748de97-d5e3-4598-9c12-827bd9c396ee)

4. 在home/facial_recognition/dataset中，新增和步驟2相同名字的資料夾

![image](https://github.com/user-attachments/assets/3f1bdf1f-3f5c-490b-b5cf-e69ea21bca07)

5. 運行headshots_picam.py，使用空白鍵拍攝不同角度自拍照(至少十張)

6. 開啟Termianl，輸入以下程式碼以訓練臉部辨識模型
```bash
cd facial_recognition

python3 train_model.py
```

7. 獲得encodings.pickle為你已訓練的臉部辨識模型

### 創建Telegram bot
1. 下載並註冊Telegram https://telegram.org/apps
   ![image](https://github.com/user-attachments/assets/7571e553-2041-4fd5-9ae8-aadbbf69ccd4)
   
2. 使用 @BotFather來創建並管理你的bot
   
   ![image](https://github.com/user-attachments/assets/610f6980-9c5a-4dbd-ab67-a5bf69100124)
   
3. 創建Telegram bot的範例
   
- https://ithelp.ithome.com.tw/articles/10245264

- https://hackmd.io/@truckski/HkgaMUc24?type=view#Python-Telegram-Bot-%E6%95%99%E5%AD%B8-by-%E9%99%B3%E9%81%94%E4%BB%81

4. 將你的token輸入tgbot.py中的"YOUR TOKEN HERE".

   注意: 請妥善保管你的bot的token.

## 功能和程式

### tgbot.py

- /start

   1. 導入final_ldr.py，在final_ldr.py運行結束後，向用戶端回傳"Finish this process"
   
- /show

   1. 透過fetch_total_money方法，從total_money.txt抓出最新的total_money
 
   2. 將被抓出的total_money顯示在Telegram上。

- /withdraw

   1. 在Telegram上詢問用戶要提取多少錢，並接收用戶輸入的金額。
 
   2. 導入final_motor.py

- /unlock

   1. 啟動樹梅派鏡頭模組，確認偵測到的臉是否與數據庫中的資料符合。
 
   2. 若符合則轉動伺服馬達來解鎖機器
 
   3. 若不符合則伺服馬達不會動作

### final_ldr.py

1. 啟動LDR以偵測硬幣數量和計算總金額

2. 總金額和硬幣數量分別寫入total_money.txt和coin_count.txt

### final_motor.py

1. 透過tgbot.py中的fetch_total_money()和fetch_coint_count()，獲得total_money和coin_count

2. 透過get_input_number()，得到用戶在Telegram上輸入的提款數字
  
3. 根據用戶輸入的數字和機器內的硬幣總量，計算4個伺服馬達分別要讓多少個硬幣落下

4. 將被扣減過的總金額和硬幣數量重新寫入total_money.txt和coin_count.txt

### facial_req.py

- 使用encodings.pickle作為已訓練好的臉部識別模型

- 若偵測到的臉有在資料庫內，則透過旋轉伺服馬達解鎖機器

## 使用方法

1. 運行tgbot.py

2. 輸入/start後投入硬幣，自動偵測投入的硬幣和金額總數

   ![image](https://github.com/user-attachments/assets/71000c00-6200-4b99-b0aa-f7fd09bdc319)

3. 輸入/show，顯示目前機器內總金額

   ![image](https://github.com/user-attachments/assets/2176cea5-473e-4f99-9952-6a2faa0b34e6)

4. 輸入/withdraw，輸入你想取出的金額，等待機器將對應的金額落下

   ![image](https://github.com/user-attachments/assets/8d2c1e6b-dfbc-4a48-9b63-719ef511f4e7)

5. 輸入/unlock禁行臉部辨識，辨識成功後可取出金額

   ![image](https://github.com/user-attachments/assets/1fb63f8c-0f99-4579-8157-5a6f8e3923e1)

## 參考資料
- https://core-electronics.com.au/guides/face-identify-raspberry-pi/  臉部辨識參考網站

- https://github.com/carolinedunn/facial_recognition 臉部辨識資料訓練

- https://circuitdigest.com/microcontroller-projects/raspberry-pi-telegram-bot 樹梅派連接telegram參考

- https://www.bilibili.com/opus/633076062099603481 伺服馬達程式碼參考

- https://youtu.be/wzRc-Arj42U?si=Xr3aOuXEamanT4tw 硬體構成範例

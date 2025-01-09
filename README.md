# desk-coin-ATM

## 目錄

-   [專案介紹](#專案介紹)
-   [硬體介紹](#硬體介紹)
-   [準備](#準備)
-   [功能和程式](#功能和程式)
-   [參考資料](#參考資料)

## 專案介紹
結合硬幣分類系統以及伺服馬達控制硬幣落下，並配合臉部識別系統，製造簡易版的桌上ATM

### 專案緣由
/暫無

## 硬體介紹
### 材料清單
* Rasberry Pi 4 x 1
* Rasberry Pi Camera Module x 1
* 麵包板 x 1
* 5mm光敏電阻 x 4
* led(非常亮) x 4
* 伺服馬達 x5

### 硬體組成
/解釋組合

## 創建Telegram bot
1. 下載並註冊Telegram https://telegram.org/apps
   ![image](https://github.com/user-attachments/assets/7571e553-2041-4fd5-9ae8-aadbbf69ccd4)
2. 使用 @BotFather來創建並管理你的bot
   
   ![image](https://github.com/user-attachments/assets/610f6980-9c5a-4dbd-ab67-a5bf69100124)
3. 創建Telegram bot的範例
   
．https://ithelp.ithome.com.tw/articles/10245264

．https://hackmd.io/@truckski/HkgaMUc24?type=view#Python-Telegram-Bot-%E6%95%99%E5%AD%B8-by-%E9%99%B3%E9%81%94%E4%BB%81

4. 將你的token輸入tgbot.py中的"YOUR TOKEN HERE".

注意: 請妥善保管你的bot的token.


## 準備
首先，具備Raspbian Buster OS之樹梅派4B，並確保內含Python版本為3

### 安裝Open-CV和Mediapipe
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

安裝Mediapipe
```bash
sudo pip3 install mediapipe-rpi4

sudo pip3 install gtts

sudo apt install mpg321

sudo pip3 install numpy --upgrade --ignore-installed
```

###安裝telepot

## 功能和程式
###tgbot.py

###final_ldr.py

###final_motor.py

###facial_req.py

## 參考資料
https://core-electronics.com.au/guides/face-identify-raspberry-pi/  臉部辨識參考網站

https://github.com/carolinedunn/facial_recognition 臉部辨識資料訓練

https://circuitdigest.com/microcontroller-projects/raspberry-pi-telegram-bot 樹梅派連接telegram

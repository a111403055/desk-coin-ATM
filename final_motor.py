from gpiozero import AngularServo
from time import sleep
import tgbot

def get_input_number(filename="user_input.txt"): # 獲取用戶在tgbot.py輸入的值
    with open(filename, "r") as file:
        lines = file.readlines()
        if not lines:
            return None  # 文件为空时返回None

        last_line = lines[-1].strip()
        try:
            number = int(last_line.split(": ")[-1])
            print(number)
            return number
        except (IndexError, ValueError):
            return None  # 如果格式不正确或转换失败，返回None

a = tgbot.fetch_total_money() # 獲取機器內總金額
b = tgbot.fetch_coin_count() # 獲取4個LDRs分別偵測到的硬幣數
c = get_input_number() # 獲取用戶輸入值

servo_counts = [0, 0, 0, 0] # 初始化

# 標定4個servo motor的GPIO pin
servo1 = AngularServo(5, min_angle=-90, max_angle=90)
servo2 = AngularServo(6, min_angle=-90, max_angle=90)
servo3 = AngularServo(13, min_angle=-90, max_angle=90)
servo4 = AngularServo(19, min_angle=-90, max_angle=90)

# 將機器內總金額減少後寫入total_money.txt中
a = a - c
with open("total_money.txt", "a") as file:
    file.write(f"{a}\n")

# 依50 10 5 1的順序，計算用戶輸入值要如何才能取出
# 並對應地減少4個LDRs分別偵測到的硬幣數，以及增加servo_counts矩陣的對應值
for i in range(3,-1,-1):
    while c > 0 and b[i] > 0:
        if i == 3 and c >= 50:
            c -= 50
            b[i] -= 1
            servo_counts[i] += 1
        elif i == 2 and c >= 10:
            c -= 10
            b[i] -= 1
            servo_counts[i] += 1
        elif i == 1 and c >= 5:
            c -= 5
            b[i] -= 1
            servo_counts[i] += 1
        elif i == 0 and c >= 1:
            c -= 1
            b[i] -= 1
            servo_counts[i] += 1
        else:
            break

# 將4個LDRs分別偵測到的硬幣數寫入coin_count.txt中
with open("coin_count.txt", "a") as file:
    file.write(f"{b}\n")

# 根據servo_counts的值，旋轉對應的伺服馬達，以取得用戶輸入的值
for i in range(3,-1,-1):
    while servo_counts[i] > 0:
        if i == 0:
            servo1.angle = -90
            sleep(0.5)
            servo1.angle = 90
            sleep(0.5)
            servo_counts[i] -= 1
            
        elif i == 1:
            servo2.angle = -90
            sleep(0.5)
            servo2.angle = 90
            sleep(0.5)
            servo_counts[i] -= 1
            
        elif i == 2:
            servo3.angle = -90
            sleep(0.5)
            servo3.angle = 90
            sleep(0.5)
            servo_counts[i] -= 1
            
        elif i == 3:
            servo4.angle = -90
            sleep(0.5)
            servo4.angle = 90
            sleep(0.5)
            servo_counts[i] -= 1
            

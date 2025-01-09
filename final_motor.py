from gpiozero import Servo
from time import sleep
import tgbot

def get_input_number(filename="user_input.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()
        if not lines:
            return None  # 文件为空时返回None

        last_line = lines[-1]
        # 假设每行格式为 "User {chat_id}: {number}\n"
        try:
            number = int(last_line.strip().split(": ")[-1])
            return number
        except (IndexError, ValueError):
            return None  # 如果格式不正确或转换失败，返回None

a = tgbot.fetch_total_money()
b = tgbot.fetch_coin_count()
c = get_input_number()

servo_counts = [0, 0, 0, 0]


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

a -= c

print(a)
print(b)
print(c)
print(servo_counts)

servo1 = Servo(5)
servo2 = Servo(6)
servo3 = Servo(13)
servo4 = Servo(19)

for i in range(3,-1,-1):
    while servo_counts[i] > 0:
        if i == 0:
            servo1.min()
            sleep(0.5)
            servo1.max()
            sleep(0.5)
        elif i == 1:
            servo2.min()
            sleep(0.5)
            servo2.max()
            sleep(0.5)
        elif i == 2:
            servo3.min()
            sleep(0.5)
            servo3.max()
            sleep(0.5)
        elif i == 3:
            servo4.min()
            sleep(0.5)
            servo4.max()
            sleep(0.5)


#while True:
#    servo.min()
#    sleep(2)
#    servo.max()
#    sleep(2)


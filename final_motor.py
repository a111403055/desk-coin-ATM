from gpiozero import Servo
from time import sleep
import tgbot

a = tgbot.fetch_total_money()
b = tgbot.fetch_coin_count()
c = tgbot.fetch_input_number()


#a = 62
#b = [4, 15, 20, 50]

servo_counts = [0, 0, 0, 0]

print(a)
print(b)
print(c)

for i in range(3,-1,-1):
    while a > 0 and b[i] > 0:
        if i == 3 and a >= 50:
            a-=50
            b[i]-=50
            servo_counts[i]+=1
        elif i == 2 and a >= 10:
            a-=10
            b[i]-=10
            servo_counts[i]+=1
        elif i == 1 and a >= 5:
            a-=5
            b[i]-=5
            servo_counts[i]+=1
        elif i == 0 and a >= 1:
            a-=1
            b[i]-=1
            servo_counts[i]+=1
        else:
            break
 
print(a)
print(b) 
print(servo_counts)

#servo = Servo(17)

#while True:
#    servo.min()
#    sleep(2)
#    servo.max()
#    sleep(2)


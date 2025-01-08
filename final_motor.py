from gpiozero import Servo
from time import sleep

a = from tgbot import number
b = from tgbot import dark_counts 


print(a)
print(b)

for i in range(len(b)):
    while a > 0 and b[i] > 0:
      if i == 0:
          if a >= b[i]:
              a -= 50
              b[i] -= 1
          else:
              break
return a, b

while a > 0:
  if b[3] >= 1:
    a - 50

#servo = Servo(17)

#while True:
#    servo.min()
#    sleep(2)
#    servo.max()
#    sleep(2)

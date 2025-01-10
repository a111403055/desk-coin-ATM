import RPi.GPIO as GPIO
import time

LDR_PINS = [17, 18, 27, 22]  # 定義4個LDRs的GPIO pins
COUNT_THRESHOLD = 0.5  # Adjust this for debounce or sensitivity

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
for pin in LDR_PINS:
    GPIO.setup(pin, GPIO.IN)

# Darkness counters for each LDR
dark_counts = [0, 0, 0, 0]  # 4個LDRs偵測的預設值

print("Press Ctrl+C to exit")

global total_money

try:
    a = 0
    for j in range(10): # 偵測的次數(總時長)
        for i, pin in enumerate(LDR_PINS):
            ldr_value = GPIO.input(pin)
            
            # 偵測硬幣經過(亮度變暗)
            if ldr_value == 0: # 設定0為硬幣經過
                if i == 0:
                    a += 1 # 機器內總金額增加
                    dark_counts[i] += 1 # 對應的LDR數量加一(代表此處增加一個硬幣)
                
                if i == 1:
                    a += 5
                    dark_counts[i] += 1 
                
                if i == 2:
                    a += 10
                    dark_counts[i] += 1 
                    
                if i == 3:
                    a += 50 
                    dark_counts[i] += 1 
        
        # Sleep to avoid bouncing
        time.sleep(COUNT_THRESHOLD)

        total_money += a
        
        print(f"Total money: {total_money}")


except KeyboardInterrupt:
    print("\nExiting program")
finally:
    # 將total_money寫入total_money.txt中
    with open("total_money.txt", "a") as file: 
        file.write(f"{total_money}\n")

    # 將4個LDRs偵測到的硬幣數寫入coin_count.txt中
    with open("coin_count.txt", "a") as file:
        file.write(f"{dark_counts}\n")
    
    GPIO.cleanup()

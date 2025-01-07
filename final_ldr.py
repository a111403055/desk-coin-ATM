import RPi.GPIO as GPIO
import time

# GPIO Pins for LDRs
LDR_PINS = [17, 18, 27, 22]  # Define GPIO pins for 4 LDRs
COUNT_THRESHOLD = 0.5  # Adjust this for debounce or sensitivity

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
for pin in LDR_PINS:
    GPIO.setup(pin, GPIO.IN)

# Darkness counters for each LDR
dark_counts = [0, 0, 0, 0]  # Initialize count for 4 LDRs

print("Press Ctrl+C to exit")

global total_money

try:
    for j in range(10):
        for i, pin in enumerate(LDR_PINS):
            # Read LDR value
            ldr_value = GPIO.input(pin)
            
            # Detect darkness (adjust condition if needed)
            if ldr_value == 0: # Darkness condition
                if i == 0:
                    dark_counts[i] += 1
                
                if i == 1:
                    dark_counts[i] += 5
                
                if i == 2:
                    dark_counts[i] += 10
                    
                if i == 3:
                    dark_counts[i] += 50
        
        # Sleep to avoid bouncing
        time.sleep(COUNT_THRESHOLD)

        # Combine counts for all LDRs and print unified result
        total_money = sum(dark_counts)
            
        print(f"Total money: {total_money}")


except KeyboardInterrupt:
    print("\nExiting program")
finally:
    
    GPIO.cleanup()

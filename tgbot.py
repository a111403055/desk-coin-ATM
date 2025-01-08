import time
import telepot
from telepot.loop import MessageLoop

# 狀態管理變數
user_states = {}

def fetch_total_money():
    try:
        from final_ldr import total_money  # 導入當前 total_money
        return total_money
    except ImportError:
        return "無法加載 final_ldr 模組！"
    except Exception as e:
        return f"發生錯誤: {e}"
    
def fetch_coin_count():
    try:
        from final_ldr import dark_counts  # 導入當前 total_money
        return dark_counts
    except ImportError:
        return "無法加載 final_ldr 模組！"
    except Exception as e:
        return f"發生錯誤: {e}"

def action(msg):
    global user_states
    chat_id = msg['chat']['id']
    command = msg['text']

    # 檢查用戶是否處於特定狀態
    if chat_id in user_states and user_states[chat_id] == 'awaiting_number':
        try:
            # 嘗試將輸入轉為數字
            number = int(command)
            user_states.pop(chat_id)  # 處理完成，清除狀態
            # 存取數字或執行其他邏輯
            with open("user_input.txt", "a") as file:
                file.write(f"User {chat_id}: {number}\n")
            telegram_bot.sendMessage(chat_id, f"收到數字: {number}")
            import final_motor  # 在這裡引入 final_motor 並使用 number
            #final_motor.control_servo(number)
        except ValueError:
            telegram_bot.sendMessage(chat_id, "請輸入有效的數字！")
        return

    print('Received: %s' % command)

    # 處理不同命令
    if command == '/hi':
        telegram_bot.sendMessage(chat_id, "test")
        
    elif command == '/start':
        
        telegram_bot.sendMessage(chat_id, "Start coin machine")
        import final_ldr
        total_coin = fetch_total_money()
        telegram_bot.sendMessage(chat_id, f"Start coin machine. Total money: {total_coin}")
        
    elif command == '/withdraw':
        
        telegram_bot.sendMessage(chat_id, "請輸入數字：")
        user_states[chat_id] = 'awaiting_number'  # 設置狀態為等待數字
        coin_counts = fetch_coin_count()
        #telegram_bot.sendMessage(chat_id, f"Start coin machine. Total money: {coin_counts}")
        import final_motor
        
    elif command == '/unlock':
        telegram_bot.sendMessage(chat_id, "Start face recognition")
        import facial_req
        

# 初始化 Telegram Bot
telegram_bot = telepot.Bot('7662998172:AAHWJB78tA_Qi003MB-BEpiHcO0JFP7G3DA')

print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()

print('Up and Running....')

while True:
    time.sleep(10)


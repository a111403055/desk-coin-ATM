import time
import telepot
from telepot.loop import MessageLoop

# 狀態管理變數
user_states = {}

def fetch_total_money(filename="total_money.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()
        if not lines:
            return None  # 文件为空时返回None

        last_line = lines[-1]
        # 假设每行格式为 "User {chat_id}: {number}\n"
        try:
            total_money = int(last_line.strip())
            return total_money
        except (IndexError, ValueError):
            return None  # 如果格式不正确或转换失败，返回None
    
def fetch_coin_count():
    try:
        from final_ldr import dark_counts  # current coin counts
        return dark_counts
    except ImportError:
        return "無法加載 final_ldr 模組！"
    except Exception as e:
        return f"發生錯誤: {e}"

def action(msg):
    global user_states
    global a
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
            
            
            total_coin = fetch_total_money()
            
            if number <= total_coin: 
                telegram_bot.sendMessage(chat_id, f"收到數字: {number}")
                import final_motor  # 在這裡引入 final_motor
            else:
                telegram_bot.sendMessage(chat_id, "No enough money") 
            
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
        telegram_bot.sendMessage(chat_id, "This process has finished")
        
    elif command == '/show':
        total_coin = fetch_total_money()
        telegram_bot.sendMessage(chat_id, f"Total money: {total_coin}")
        
    elif command == '/withdraw':
        
        telegram_bot.sendMessage(chat_id, "請輸入數字：")
        coin_counts = fetch_coin_count()
        user_states[chat_id] = 'awaiting_number'  # 設置狀態為等待數字
        #telegram_bot.sendMessage(chat_id, f"Start coin machine. Total money: {coin_counts}")
        
    elif command == '/show':
        total_coin = fetch_total_money()
        telegram_bot.sendMessage(chat_id, f"Total money: {total_coin}")   
        
    elif command == '/unlock':
        telegram_bot.sendMessage(chat_id, "Start face recognition")
        import facial_req
        
if __name__ == "__main__":
    # 初始化 Telegram Bot
    telegram_bot = telepot.Bot('7662998172:AAHWJB78tA_Qi003MB-BEpiHcO0JFP7G3DA')

    print(telegram_bot.getMe())

    MessageLoop(telegram_bot, action).run_as_thread()

    print('Up and Running....')
    
    a = 0
    
    while True:
        time.sleep(10)


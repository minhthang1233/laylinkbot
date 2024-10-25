from telethon import TelegramClient, events
import re
import os

# Thông tin bot từ các biến môi trường
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Khởi tạo client cho bot
bot = TelegramClient('bot', API_ID, API_HASH)

async def main():
    # Kết nối bot với Telegram
    await bot.start(bot_token=BOT_TOKEN)
    print("Bot đã kết nối thành công và đang chạy...")

# Hàm lấy link từ văn bản
def extract_links(text):
    # Tìm tất cả các link có trong tin nhắn
    links = re.findall(r'(https?://[^\s]+)', text)
    return links

# Lắng nghe tin nhắn từ người dùng và xử lý
@bot.on(events.NewMessage)
async def handler(event):
    text = event.message.message
    print(f"Nhận tin nhắn: {text}")  # Log tin nhắn nhận được
    links = extract_links(text)
    if links:
        await event.reply(f"Links found: {' '.join(links)}")
        print("Đã tìm thấy link và trả lời người dùng.")  # Log phản hồi thành công
    else:
        await event.reply("Không có link nào trong tin nhắn này.")
        print("Không có link trong tin nhắn.")  # Log khi không có link nào

# Chạy bot và log quá trình
print("Đang khởi động bot...")
with bot:
    bot.loop.run_until_complete(main())
    bot.run_until_disconnected()

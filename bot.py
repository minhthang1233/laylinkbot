from telethon import TelegramClient, events
import re

# Thông tin bot từ BotFather
API_ID = 21357718  # Thay bằng API_ID của bạn
API_HASH = "df3564e279df7787a6292c45b177524a"  # Thay bằng API_HASH của bạn
BOT_TOKEN = "7596481021:AAEYehQLfPlWHNzuDsVF-rFR1zxaxaw4LeE "  # Thay bằng BOT_TOKEN bạn nhận được từ BotFather

# Khởi tạo client cho bot
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Hàm lấy link từ văn bản
def extract_links(text):
    # Tìm tất cả các link dạng HTML hoặc HTTP/S
    links = re.findall(r'(https?://[^\s]+)', text)
    return links

# Lắng nghe tin nhắn từ người dùng
@bot.on(events.NewMessage)
async def handler(event):
    message = event.message  # Lấy tin nhắn
    text = message.raw_text  # Lấy nội dung văn bản thô của tin nhắn
    
    # Kiểm tra nếu tin nhắn có dạng văn bản
    if text:
        links = extract_links(text)  # Trích xuất link từ văn bản
        
        # Kiểm tra nếu có link trong văn bản
        if links:
            await event.reply(f"Links found: {' '.join(links)}")
        else:
            await event.reply("Không có link nào trong tin nhắn này.")
    
    # Kiểm tra nếu tin nhắn là loại khác, ví dụ tin nhắn chuyển tiếp
    elif message.is_forwarded:
        forward_text = message.forward.text
        links = extract_links(forward_text)
        
        if links:
            await event.reply(f"Links found in forwarded message: {' '.join(links)}")
        else:
            await event.reply("Không có link nào trong tin nhắn chuyển tiếp này.")
    else:
        await event.reply("Tin nhắn này không chứa văn bản có thể đọc được.")

# Chạy bot
print("Bot đang chạy...")
bot.run_until_disconnected()

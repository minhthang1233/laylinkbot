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
    message = event.message  # Lấy tin nhắn gốc
    links = []
    
    # Kiểm tra nếu tin nhắn là văn bản hoặc chuyển tiếp
    if message.raw_text:
        # Lấy nội dung từ văn bản hoặc tin nhắn gốc
        links.extend(extract_links(message.raw_text))
    elif message.is_forwarded and message.forward.text:
        # Nếu tin nhắn được chuyển tiếp, lấy nội dung từ tin nhắn chuyển tiếp
        links.extend(extract_links(message.forward.text))
    
    # Nếu có link, gửi lại cho người dùng
    if links:
        await event.reply(f"Links found: {' '.join(links)}")
    else:
        await event.reply("Không tìm thấy link nào trong tin nhắn này.")

# Chạy bot
print("Bot đang chạy...")
bot.run_until_disconnected()

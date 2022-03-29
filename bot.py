from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
from datetime import datetime

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")
USERS_ = config("USERS_CHANNEL")
USERS_NAME_ = config("USERSNAME_CHANNEL")

# Tách chuỗi thành dạng list ngăn cách khoảng trắng
#User
USER_ID = [int(i) for i in USERS_.split()]
#FROM Channel ID
FROM = [int(i) for i in FROM_.split()]
#To Channel ID
TO = [int(i) for i in TO_.split()]
#User Name
USER_NAME = USERS_NAME_.split()

#Khai báo và kết nối client
try:
    #Khai báo Client
    BotHuuKhoa = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    #Chạy client
    BotHuuKhoa.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

#Sự kiện : Có tin nhắn báo về 
@BotHuuKhoa.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            #await BotzHubUser.send_message(
            #    i,
            #    event.message
            #)
            # Lấy username từ New Message
            sender = await event.get_sender()
            nguoidung = sender.username
            print(sender.username)
            # Lấy id user từ New Message
            #sender = event.sender_id
            #print(sender)
            if nguoidung in USER_NAME:
            #if sender in USER_ID:
                await BotHuuKhoa.forward_messages(entity=i, messages=event.message)
                print(event.date.strftime('%m/%d/%Y, %H:%M:%S'))
                print('ok')        
        except Exception as e:
            print(e)

print("Bot da khoi dong.")
BotHuuKhoa.run_until_disconnected()

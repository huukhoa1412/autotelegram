from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
from datetime import datetime

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
#Đăng nhập telegram
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
#FROM
##ID
FROM_ = config("FROM_CHANNEL")
##USENAME
FROM_USER_ = config("FROM_CHANNEL_USER")
#TO
##ID
TO_ = config("TO_CHANNEL")
##USENAME
TO_USER_ = config("TO_CHANNEL_USER")
#USER
##ID
USER_ID_ = config("USER")
##USENAME
USER_NAME_ = config("USER_NAME")


# Tách chuỗi thành dạng list ngăn cách khoảng trắng
#User ID
USER_ID = [int(i) for i in USER_ID_.split()]
#FROM Channel ID
FROM = [int(i) for i in FROM_.split()]
#To Channel ID
TO = [int(i) for i in TO_.split()]
#UserName
TO_USER = TO_USER_.split()
#User TO Channel
USER_NAME = USER_NAME_.split()

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
            # Lấy username từ New Message
            sender = await event.get_sender()
            from_id = event.peer_id.channel_id
            nguoidung = sender.username
            fisrt_name = sender.first_name
            last_name = sender.last_name
            print(f'User:{nguoidung}-{fisrt_name}-{last_name}-{from_id}')
            # Lấy id user từ New Message
            #sender = event.sender_id
            #print(sender)
            if nguoidung in USER_NAME:
            #if sender in USER_ID:
                dialogs = await BotHuuKhoa.get_dialogs(limit=None)
                await BotHuuKhoa.forward_messages(entity=i, messages=event.message)
                print(event.date.strftime('%m/%d/%Y, %H:%M:%S'))
                print('ok')        
        except Exception as e:
            print(e)

print("Bot da khoi dong.")
BotHuuKhoa.run_until_disconnected()

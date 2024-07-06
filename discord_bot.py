from urllib3.exceptions import InsecureRequestWarning
import discord
import os
from discord.ext import commands
import requests
import json
from config import Config
import asyncio
from discord import Embed, Color
import certifi
# Tắt cảnh báo SSL

intents = discord.Intents.all()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)
previous_message = None
previous_message_question = None


@bot.event
async def on_ready():
    print("Discord on ready")
    channel = bot.get_channel(Config.MTIPSCODER_CHANNEL_ID)
    await channel.send('Hikari đã chạy!')
    # Chạy câu hỏi đầu tiên


async def send_question_discord(message):
    channel = bot.get_channel(Config.MTIPSCODER_CHANNEL_ID)
    await channel.send(message)


@bot.event
async def on_message(message):
    global previous_message
    global previous_message_question
    print("Lấy message")
    # Xử lí khác
    msg_content = str(message.content).lower()
    if msg_content == '!ping':
        await message.channel.send('Pong!')

    # Kiểm tra câu trả lời
    # Trả lời là A B C D và tiếp tục, ok
    if (msg_content in ['a', 'b', 'c', 'd', 'tiếp tục', 'ok'] or msg_content.endswith('.')) and previous_message_question:
        result = previous_message_question.split(".", 1)
        id = result[0]
        await send_hikari_question_answer(channel=message.channel, id=id, answer=msg_content)

        await asyncio.sleep(2)  # Chờ 2 giây
        await send_hikari_question(channel=message.channel, user=message.author.name)

    # Lấy câu hỏi
    if msg_content == '!hikari':
        await send_hikari_question(channel=message.channel, user=message.author.name)


async def send_hikari_question(channel, user):
    global previous_message_question
    url = Config.DOMAIN_NAME+'/notification/send-discord'
    print("In File: discord_bot.py, Line: 63",url)
    res = requests.get(url, headers={
        'content-type': 'application/json',
    },  params={"user": user}, verify=certifi.where())
    # print(res.__dict__)
    # Nhận và đọc phản hồi từ máy chủ
    if res.status_code == 200:
        response_data = res.json()
        # Lấy dữ liệu từ payload
        message_content = response_data['payload']['message']
        image_path = response_data['image_path']
        image_path_ab = response_data['image_path_ab']
        # Tạo embed
        embed = Embed(title="Đây là câu hỏi",
                      description=message_content, color=Color.blue())

        if image_path:
            # Thêm ảnh vào Embed
            file = discord.File(
                image_path_ab, filename="image.png")
            embed.set_image(url="attachment://image.png")
            await channel.send(file=file, embed=embed)
            # Lưu lại câu trước đó
            previous_message_question = message_content
            return

        # Lưu lại câu trước đó
        previous_message_question = message_content
        await channel.send(embed=embed)
    else:
        await channel.send("Hikari không lấy được câu hỏi mới vui lòng thử lại")


async def send_hikari_question_answer(channel, id, answer):
    url = Config.DOMAIN_NAME+'/notification/send-answer-discord/'+str(id)
    print("In File: discord_bot.py, Line: 98",url)
    data = {
        'answer': answer
    }
    res = requests.get(url, params=data, headers={
        'content-type': 'application/json'}, verify=certifi.where())

    if res.status_code == 200:
        response_data = res.json()
        # Lấy dữ liệu từ payload
        message_content = response_data['payload']
        image_path = response_data['image_path']
        image_path_ab = response_data['image_path_ab']
        # Tạo một Rich Embed
        embed = Embed(title="Đáp án câu trên",
                      description=message_content, color=0x00ff00)

        if image_path:
            # Thêm ảnh vào Embed
            file = discord.File(
                image_path_ab, filename="image.png")
            embed.set_image(url="attachment://image.png")
            await channel.send(file=file, embed=embed)
            return

        await channel.send(embed=embed)
    else:
        await channel.send("Hikari không lấy được câu trả lời vui lòng thử lại")

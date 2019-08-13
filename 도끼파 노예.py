import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!안녕")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("이게 어른한테 어디서 반말이야!")

    if message.content.startswith("!도움말"):
        await message.channel.send("그런거 없는디?")

    if message.content.startswith("!사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("굿"):
        await message.channel.send("고맙데이~")

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)
        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

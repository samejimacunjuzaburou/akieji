import discord

with open('./sendMessage.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

intents = discord.Intents.default()
intents.members = True  # サーバーメンバーの情報を取得するために必要

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} としてログインしました。')
    channel = client.get_channel(チャンネルID)  # メッセージを送信するチャンネルを取得する
    await channel.send(contents)  # メッセージを送信する

client.run("トークンID")
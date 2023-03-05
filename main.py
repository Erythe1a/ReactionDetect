import discord
import os

# クライアント接続
intents=discord.Intents.none()
intents.reactions = True
intents.guilds = True
client = discord.Client(intents=intents)

# 起動時の処理（無くても問題ない）
@client.event
async def on_ready():
    print('ログインしました')

# リアクションされた時に動作する処理
@client.event
async def on_raw_reaction_add(payload):
# リアクションされたメッセージのチャンネル
    txt_channel = client.get_channel(payload.channel_id)
# リアクションされたメッセージ
    message = await txt_channel.fetch_message(payload.message_id)
# リアクションしたユーザ
    user = payload.member
# 自分自身に対するリアクションは通知しない
    if (message.author == user):
        return
# Bot 専用のチャンネル ID 
    channel = client.get_channel(CHANNEL_ID)
# 左からリアクションされたメッセージの投稿主、リアクション、リアクションしたユーザの表示名、
# メッセージの内容、メッセージへのリンク
    msg = f"{message.author.mention} {payload.emoji}\nFrom:{user.display_name} \
          \nMessage:{message.content}\n{message.jump_url}"
    await channel.send(msg)

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
client.run(TOKEN)

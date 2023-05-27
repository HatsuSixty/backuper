#!/bin/env python3

import discord
import io
import json
import os.path as p
import shutil
from dotenv import load_dotenv
from os import getenv, mkdir
from sys import stderr

load_dotenv()

collected_messages = ""
collected_attachments = []

class MyClient(discord.Client):
    prefix = "!"

    async def on_ready(self):
        print(f"{self.user} is ready to start backuping!")

    async def on_message(self, message):
        global collected_messages, collected_attachments
        content = message.content
        if content.startswith(self.prefix):
            args = content[len(self.prefix):].split()
            match args[0]:
                case "backup":
                    if not message.author.id == message.guild.owner_id:
                        await message.channel.send("Only ADM :XD:")
                    else:
                        await message.channel.send("Starting backup...")
                        messages = []
                        async for m in message.channel.history(limit=None):
                            print(f"[INFO] Saving message `{m.id}`")
                            md = m.created_at
                            m_object = {
                                "content": m.content,
                                "date": f"{md.day}/{md.month}/{md.year} {md.hour}:{md.minute}:{md.second}",
                                "author": f"{m.author.name}#{m.author.discriminator}"
                            }
                            if m.attachments:
                                m_object["attachments"] = []
                                for a in m.attachments:
                                    fpath = f"assets/file{len(messages)+len(collected_attachments)}"
                                    m_object["attachments"].append(fpath)
                                    buf = io.BytesIO(b'')
                                    await a.save(buf)
                                    collected_attachments.append({
                                        "name": fpath,
                                        "buffer": buf
                                    })
                            messages.append(m_object)
                        collected_messages = json.dumps(messages, indent=2)
                        await self.close()
                case _:
                    await message.channel.send("Unknown command :XD:")

if not p.isdir("assets"):
    mkdir("assets")
if p.isfile("assets"):
    print("ERROR: The folder `assets` either doesn't exist or is a file", file=stderr)
    exit(1)

intents = discord.Intents.default()
intents.message_content = True

DISCORD_PREFIX = getenv("DISCORD_PREFIX")
DISCORD_TOKEN = getenv("DISCORD_TOKEN")
if (not DISCORD_PREFIX) or (not DISCORD_TOKEN):
    print(f"ERROR: The environment variable {'DISCORD_PREFIX' if not DISCORD_PREFIX else 'DISCORD_TOKEN'} is not set", file=stderr)
    exit(1)

client = MyClient(intents=intents)
client.prefix = DISCORD_PREFIX
client.run(DISCORD_TOKEN)

with open("messages.json", "w") as f:
    print(collected_messages, file=f)

for a in collected_attachments:
    with open(a["name"], "wb") as f:
        shutil.copyfileobj(a["buffer"], f)

import discord
from dotenv import load_dotenv
import os
load_dotenv()

server_id = os.getenv('SERVER_ID')
channel_id = os.getenv('CHANNEL_ID')
token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
	async def on_ready(self):
		print(f'Logged on as {self.user}!')
		self.server = self.get_guild(int(server_id))
		self.channel = self.server.get_channel(int(channel_id))

	def is_private_message_from_user(self, message: discord.Message):
		return isinstance(message.channel, discord.DMChannel) and not message.author.bot

	async def convert_attachments_to_files(self, message: discord.Message):
		files = []
		if message.attachments:
			for attachment in message.attachments:
				files.append(await attachment.to_file())
		return files

	async def on_message(self, message: discord.Message):
		if not self.is_private_message_from_user(message):
			return

		files = await self.convert_attachments_to_files(message)

		await self.channel.send(f'{message.content}', files=files)
		await message.channel.send('Le message a bien été envoyé !')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

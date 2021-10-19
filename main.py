from twitchio.ext import commands
import configparser
import os


def read_ini_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    for sect in config.sections():
        for key in config[sect]:
            print((key, config[sect][key]))

    return config


class ymbot(commands.Bot):

    def __init__(self):
        cwd = os.getcwd()
        config = read_ini_file(cwd + "/config.ini")
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=config['APP']['access_token'], prefix='!', nick='ymbot', initial_channels=['phantoml22'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'{self.nick} is ready to go!')

    @commands.command()
    async def atq(self, ctx: commands.Context):
        # Add new song to current queue
        await ctx.send(f'{ctx.author.name} requested {ctx.message.content[4:]}')

bot = ymbot()
try:
    bot.run()
except Exception as e:
    bot.close()


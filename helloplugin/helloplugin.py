from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if "hello" in message.content.lower():
            await message.channel.send("Hey! How are you?")
        elif "good" in message.content.lower():
            await message.channel.send("Ah! Glad to hear it.")
        elif "bruh" in message.content.lower():
            await message.channel.send("brooooooo ")
        elif "boss" in message.content.lower():
            await message.channel.send("boss ded ")
        elif "kidnap" in message.content.lower():
            await message.channel.send("I brought the guns. LETS DO THIS")
        elif "die" in message.content.lower():
            await message.channel.send("NO")
        elif "dead" in message.content.lower():
            await message.channel.send("who isn't bro who isn't")
        elif "corpse" in message.content.lower():
            await message.channel.send("RIP")
        elif "kill" in message.content.lower():
            await message.channel.send("NO")
        elif "cute" in message.content.lower():
            await message.channel.send("IKR")
        elif "bro" in message.content.lower():
            await message.channel.send("brooooooo")
        elif "zen" in message.content.lower():
            await message.channel.send("don't tag master")
        elif "chill" in message.content.lower():
            await message.channel.send("can't chill, too much work")
        elif "baka" in message.content.lower():
            await message.channel.send("baka who? where?")
        elif "good morning" in message.content.lower():
            await message.channel.send("Good Morning !")
        elif "good night" in message.content.lower():
            await message.channel.send("Good Night !")
        elif "hey" in message.content.lower():
            await message.channel.send("yo!  How are you?")
        elif "sup" in message.content.lower():
            await message.channel.send("Sup")
        elif "killzen" in message.content.lower():
            await message.channel.send("in your dreams lol")
        elif "kill zen" in message.content.lower():
            await message.channel.send("pfft not gonna happen kiddo")
        elif "dum" in message.content.lower():
            await message.channel.send("No you are dum")
        elif "bad" in message.content.lower():
            await message.channel.send("Why? Tell me?")
        elif "sup" in message.content.lower():
            await message.channel.send("Sup")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))

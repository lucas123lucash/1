import discord
from discord.ext import commands
import os
import requests
import json
import subprocess
import time

# Configuración del bot
token = 'TU_TOKEN_DE_DISCORD'
ngrok_token = 'TU_TOKEN_DE_NGROK'

# Crear el cliente del bot
bot = commands.Bot(command_prefix='!')

# Función para iniciar Ngrok
def iniciar_ngrok():
    subprocess.Popen(['ngrok', 'tcp', '25565'])

# Función para obtener la URL de Ngrok
def obtener_url_ngrok():
    time.sleep(10)  # Espera 10 segundos para que Ngrok se inicie completamente
    url = requests.get('http://127.0.0.1:4040/api/tunnels')
    url_ngrok = json.loads(url.text)['tunnels'][0]['public_url']
    return url_ngrok

# Comando para iniciar el servidor
@bot.command()
async def start(ctx):
    await ctx.send('Iniciando el servidor...')
    iniciar_ngrok()  # Iniciar Ngrok
    time.sleep(5)  # Esperar un poco antes de obtener la URL
    url_ngrok = obtener_url_ngrok()  # Obtener la URL de Ngrok
    await ctx.send(f'Servidor iniciado. Únete con esta IP: {url_ngrok}')

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Iniciar el bot
bot.run(token)

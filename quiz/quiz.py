import random
import json
import discord
from discord.ext import commands
from datetime import date



# Definir todas las preguntas del quiz
all_questions = [
    {'text': "¿Cuál es la capital de Francia?", 'options': ["Berlín", "Madrid", "París", "Roma"], 'correct': "París"},
    {'text': "¿Cuál es el océano más grande del mundo?", 'options': ["Atlántico", "Índico", "Ártico", "Pacífico"], 'correct': "Pacífico"},
    {'text': "¿En qué año llegó el hombre a la luna?", 'options': ["1965", "1969", "1972", "1980"], 'correct': "1969"},
    {'text': "¿Cuál es el país más grande del mundo?", 'options': ["China", "Estados Unidos", "Canadá", "Rusia"], 'correct': "Rusia"},
    {'text': "¿Qué elemento tiene el símbolo químico 'O'?", 'options': ["Oro", "Oxígeno", "Osmio", "Oganesón"], 'correct': "Oxígeno"},
    {'text': "¿Cuál es la capital de España?", 'options': ["Madrid", "Barcelona", "Valencia", "Sevilla"], 'correct': "Madrid"},
    {'text': "¿Qué planeta es conocido como el planeta rojo?", 'options': ["Marte", "Venus", "Júpiter", "Saturno"], 'correct': "Marte"},
    {'text': "¿Cuál es el río más largo del mundo?", 'options': ["Amazonas", "Nilo", "Yangtsé", "Misisipi"], 'correct': "Nilo"},
    {'text': "¿Cuál es el animal terrestre más grande?", 'options': ["Elefante", "Rinoceronte", "Hipopótamo", "Jirafa"], 'correct': "Elefante"},
    {'text': "¿Qué país es conocido como la tierra del sol naciente?", 'options': ["China", "Corea del Sur", "Japón", "Vietnam"], 'correct': "Japón"},
    {'text': "¿Quién pintó la Mona Lisa?", 'options': ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], 'correct': "Leonardo da Vinci"},
    {'text': "¿Cuál es el idioma más hablado en el mundo?", 'options': ["Inglés", "Español", "Chino mandarín", "Hindú"], 'correct': "Chino mandarín"},
    {'text': "¿En qué país se encuentra la Torre Eiffel?", 'options': ["España", "Italia", "Francia", "Reino Unido"], 'correct': "Francia"},
    {'text': "¿Cuál es el metal más abundante en la Tierra?", 'options': ["Hierro", "Aluminio", "Cobre", "Oro"], 'correct': "Hierro"},
    {'text': "¿Cuál es el deporte más popular en el mundo?", 'options': ["Baloncesto", "Críquet", "Fútbol", "Tenis"], 'correct': "Fútbol"},
    {'text': "¿Qué instrumento musical tiene teclas blancas y negras?", 'options': ["Guitarra", "Batería", "Piano", "Violín"], 'correct': "Piano"},
    {'text': "¿En qué año comenzó la Segunda Guerra Mundial?", 'options': ["1914", "1939", "1945", "1950"], 'correct': "1939"},
    {'text': "¿Cuál es el continente más grande del mundo?", 'options': ["África", "Asia", "América", "Europa"], 'correct': "Asia"},
    {'text': "¿Cuál es el órgano más grande del cuerpo humano?", 'options': ["Corazón", "Hígado", "Cerebro", "Piel"], 'correct': "Piel"},
    {'text': "¿Quién es el autor de 'Don Quijote de la Mancha'?", 'options': ["Gabriel García Márquez", "Miguel de Cervantes", "Mario Vargas Llosa", "Jorge Luis Borges"], 'correct': "Miguel de Cervantes"}
]


# Ruta del archivo JSON para guardar los logros
ACHIEVEMENTS_FILE = 'achievements.json'

# Crear instancia del bot, todos los comandos del bot comenzarán con !
bot = commands.Bot(command_prefix='!') 

# 5 preguntas aleatorias
questions = random.sample(all_questions, 5)
current_question = 0 #índice de la pregunta actual
score = 0 #guarda el puntaje del usuario


# Funciones para cargar y guardar logros
def load_achievements():
    try:
        with open(ACHIEVEMENTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_achievements(achievements):
    with open(ACHIEVEMENTS_FILE, 'w') as f:
        json.dump(achievements, f, indent=4)
        

# Crear instancia del bot
@bot.event   #la función siguiente es un evento.
async def on_ready():   #función asincrónica que se ejecuta cuando el bot está listo y conectado.
    print(f'Bot conectado como {bot.user}')

#Reiniciar la selección de preguntas al iniciar el quiz
@bot.command(name='quiz') #ejecutar con !quiz
async def start_quiz(ctx):
    global questions, current_question, score
    questions = random.sample(all_questions, 5)
    current_question = 0 #Reinicia el índice de la pregunta actual.
    score = 0 #Reinicia el puntaje.
    await ask_question(ctx)

async def ask_question(ctx): #función para hacer una pregunta.
    question = questions[current_question] #btiene la pregunta actual.
    text = f"{question['text']}\n" #Prepara el texto de la pregunta
    for i, option in enumerate(question['options'], start=1): #Recorre las opciones de respuesta, enumerándolas desde 1.
        text += f"{i}. {option}\n" #Añade cada opción al texto de la pregunta.
    await ctx.send(text) #Envía la pregunta y sus opciones al canal de Discord.

@bot.event
async def on_message(message): #ejecuta cada vez que el bot recibe un mensaje.
    global current_question, score

    # Ignorar mensajes del bot
    if message.author == bot.user:
        return

    if current_question < len(questions):
        question = questions[current_question]
        if message.content.isdigit():
            answer = int(message.content) - 1 #Convierte el contenido del mensaje a un índice de opción.
            if question['options'][answer] == question['correct']:
                score += 1
                await message.channel.send("¡Correcto!\n")
            else:
                await message.channel.send(f"Incorrecto. La respuesta correcta era: {question['correct']}\n")

            current_question += 1
            if current_question < len(questions):
                await ask_question(message.channel)
            else:
                await show_score(message.channel)
    await bot.process_commands(message)

async def show_score(channel,user):
    global score
    await channel.send(f"Tu puntaje final es: {score} de {len(questions)}")
    update_achievements(user, score)
    
    
def update_achievements(user, score):
    achievements = load_achievements()
    user_id = str(user.id)
    if user_id in achievements:
        # Obtener la fecha actual en formato YYYY-MM-DD
        today = date.today().isoformat()
        achievements[user_id]['achievements'].append({
            'date': today,
            'scores': [score],
            'total_attempts': 1
        })
    else:
        achievements[user_id] = {
            'name': user.name,
            'achievements': [{
                'date': date.today().isoformat(),
                'scores': [score],
                'total_attempts': 1
            }]
        }
    save_achievements(achievements)

#Comando para mostrar logros:
@bot.command(name='logros')
async def show_achievements(ctx):
    achievements = load_achievements()
    if not achievements:
        await ctx.send("No hay logros registrados.")
        return

    embed = discord.Embed(title="Logros de los usuarios")
    for user_id, data in achievements.items():
        scores = ', '.join(map(str, data['scores']))
        embed.add_field(name=data['name'], value=f"Puntajes: {scores}", inline=False)
    await ctx.send(embed=embed)

# Reemplazar con el token de Discord
bot.run('YOUR_TOKEN')
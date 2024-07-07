import random

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

# Seleccionar 5 preguntas aleatorias
questions = random.sample(all_questions, 5)
current_question = 0
score = 0

# Función para hacer una pregunta
def ask_question():
    global current_question
    question = questions[current_question]
    text = f"{question['text']}\n"
    for i, option in enumerate(question['options'], start=1):
        text += f"{i}. {option}\n"
    return text

# Función para mostrar el puntaje
def show_score():
    global score
    return f"Tu puntaje final es: {score} de {len(questions)}"

# Simulación del quiz
for i in range(len(questions)):
    print(ask_question())
    answer = int(input("Selecciona la respuesta correcta (número): ")) - 1
    if questions[current_question]['options'][answer] == questions[current_question]['correct']:
        score += 1
        print("¡Correcto!\n")
    else:
        print(f"Incorrecto. La respuesta correcta era: {questions[current_question]['correct']}\n")
    current_question += 1

print(show_score())

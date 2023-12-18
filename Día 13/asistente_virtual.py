import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / idioma
voz_id = "id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"


# escuchar nuestro microfono y devolver audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscr en google
            pedido = r.recognize_google(audio, language="es-es")

            #prueba de que pudo ingresar
            print("Dijiste: "+ pedido)

            # devolver a pedido
            return pedido
        # en caso de que no compenda el audio
        except sr.UnknownValueError:

            #pruba de que no comprendio el audio
            print("ups, no entendi")

            # devolver error
            return "sigo esperando"
        # en caso de no resolver el pedido
        except sr.RequestError:

            # pruba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"
        # error inesperado
        except:
            # pruba de que no comprendio el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"


# funcion para que el asistente pueda ser escuchado
def decir_mensaje(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', voz_id)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear varioable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}

    # decir el dia de la semana
    decir_mensaje(f"Hoy es {calendario[dia_semana]}")


# informar que hora es
def pedir_hora():

    # crear variable con datos de hoy
    hora = datetime.datetime.now()
    print(hora)

    #crear varioable para la hora
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    decir_mensaje(hora)


# funcion saludo inicial
def saludo_inicial():

    # Crear variable con dato de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buenos días"
    else:
        momento = "Buenas tardes"

    # Decir el saludo
    decir_mensaje(f"{momento}, soy Helena, tu asistente personal. Por favor, dime en qué te puedo ayudar")


# funcion central del asistente
def pedir_cosas():

    #activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            decir_mensaje("Con gusto, estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'abrir navegador' in pedido:
            decir_mensaje("Claro, estoy en eso")
            webbrowser.open("https://www.google.com")
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            decir_mensaje("Buscando eso en wikipedia")
            pedido = pedido.replace("busca en wikipedia", '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            decir_mensaje('Wikipedia dice lo siguiente:')
            decir_mensaje(resultado)
            continue
        elif 'busca en internet' in pedido:
            decir_mensaje("Ya mismo estoy en eso")
            pedido = pedido.replace("busca en internet", '')
            pywhatkit.search(pedido)
            decir_mensaje("Esto es lo que he encontrado")
            continue
        elif 'reproducir' in pedido:
            decir_mensaje("Buena idea, ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            decir_mensaje(pyjokes.get_joke("es"))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                decir_mensaje(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                decir_mensaje("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            decir_mensaje("Me voy a descansar, cualquier cosa me avisas")
            comenzar = False


pedir_cosas()

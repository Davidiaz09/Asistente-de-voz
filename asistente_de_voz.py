import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser #python
import datetime  #python
import wikipedia #pyhton


#Nombre asistente:
name = "Ania"

#Objeto de renocimiento de voz:
audio_recognizer = sr.Recognizer()

#Iniciando pyttsx3 (voz del asistente):
engine = pyttsx3.init()

#Definiendo voz:
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


#Función de reconocer audio:
def listener():

    """Reconoce y captura el audio del usuario.
    Return. Devuelve el audio del usuario transformado en texto"""
    
    try:
        
        #Configurando el micófono:
        with sr.Microphone() as audio_source:
            
            #Tiempo de espera para poder hablar:
            audio_recognizer.pause_threshold = 1.0
            
            print("Puedes hablar")
            audio = audio_recognizer.listen(audio_source)
            rec = audio_recognizer.recognize_google(audio, language="es-co")
            
        return rec
    
    #En caso de no haber podido entender el audio:
    except sr.UnknownValueError:
        speaker("No te he entendido, puedes repetir?")
        
    #Error en el pedido
    except sr.RequestError:
        speaker("No he podido encontrar lo que pides")
        
    #En caso de error inesperado:
    except:
        speaker("Lo siento, no he entendido lo que dices")


#Dar voz al asistente:
def speaker(message):

    """Empleada para que el asistente reproduzca un mensaje en voz."""
    
    engine.say(message)
    engine.runAndWait()


#Creando saludo inicial:      
def start_greeting():

    "Genera el saludo inicial del asistente."
    
    greeting = f"Hola, soy {name} tu asistente virtual, ¿en que te puedo ayudar?"
    speaker(greeting)


#Función para obtener la fecha actual
def ask_for_day():

    "Proporciona la fecha actual."
    
    date = datetime.date 
    
    day = date.weekday(date.today())
    weekdays_name = {0: "Lunes",
                     1: "Martes",
                     2: "Miércoles",
                     3: "Jueves",
                     4: "Viernes",
                     5: "Sábado",
                     6: "Domingo"}
    
    speaker(f"El día de hoy es {weekdays_name[day]} {date.today()}")


#Función para obtener la hora actual    
def ask_for_time():

    "Proporciona la hora actual."
    
    time = datetime.datetime
    speaker(f"La hora es {time.now().hour} y {time.now().minute}")
    

#Función para iniciar al asistente:
def run_assistant():

    "Ejecuta el bucle principal del asistente, escuchando y procesando los comandos proporcionados por el usuario."
    
    start_greeting()
    
    while True:
       
        try:
            result = listener()
            requirement = result.lower()
            
            #Para obtener la hora actual:
            if "qué hora es" in requirement or "dime la hora" in requirement or "necesito la hora" in requirement:
                ask_for_time()
                continue
            
            #Para obtener la fecha actual:
            elif "qué día es hoy" in requirement or "fecha de hoy" in requirement:
                ask_for_day()
                continue
            
            #Para abrir YouTube:
            elif "abre youtube" in requirement:
                speaker("abriendo youtube")
                webbrowser.open("https://www.youtube.com")
                continue
            
            #Para abrir el navegador:    
            elif "abre el navegador" in requirement or "abre google" in requirement:
                speaker("abriendo google")
                webbrowser.open("https://www.google.com")
                continue
            
            #Para realizar una consulta en wikipedia:
            elif "busca en wikipedia" in requirement:
                try:
                    speaker("buscando en wikipedia")
                    requirement = requirement.replace("busca en wikipedia", "")
                    wikipedia.set_lang("es")
                    search_result = wikipedia.summary(requirement, sentences=1)
                    speaker(search_result)
                
                except wikipedia.exceptions.PageError: 
                    speaker("no he podido encontrar lo que buscas, puedes repetir?")
                    
                continue
            
            #Para realizar una busqueda en internet
            elif "busca en internet" in requirement:
                speaker("buscando en internet")
                request = requirement.replace("busca en internet", "")
                pywhatkit.search(request)    
                continue
            
            #Para reproducir un video en Youtube:
            elif "reproduce" in requirement:
                speaker("reproduciendo")
                pywhatkit.playonyt(requirement)
                continue
            
            #Para pedir un chiste:
            elif "chiste" in requirement:
                speaker(pyjokes.get_joke("es"))
                continue
            
            #Para consultar el precio de las acciones:
            elif "precio de las acciones de" in requirement or "valor de las acciones de" in requirement:
                company = requirement.split("de")[-1].lstrip()
                companies = {"apple": "AAPL", 
                             "microsoft": "MSFT",
                             "google": "GOOGL",
                             "amazon": "AMZN",
                             "meta": "META",
                             "nvidia": "NVDA",
                             "tesla": "TSLA"
                             }
            
                try:
                    extract_company = companies[company]
                    get_company = yf.Ticker(extract_company)
                    history_prices = get_company.history(period="1d")
                    stock_price = history_prices["Close"].iloc[-1]
                    speaker(f"el precio de las acciones de {company} es de: {stock_price.round(2)} dolares")
                    
                except:
                    speaker(f"no he podido encontrar el precio de las acciones de {company}")

                continue
            
            #Para finalizar el programa:
            if "adiós" in result:
                speaker("Espero haberte ayudado, adiós.")
                break
                
            
        except AttributeError:
            continue
            
            
        
            
        
run_assistant()
        
        

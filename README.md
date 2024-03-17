Este repositorio cuenta con un único módulo en el que se llevó a cabo el desarrollo de un asistente virtual capaz de realizar ciertas acciones solicitadas a través de comandos de voz.
Las librerías empleadas en la creación del asistente son: pyttsx3, speech_recognition, pywhatkit, yfinance, pyjokes, webbrowser, datetime y wikipedia.
El nombre de la asistente es Ania, está configurada en el idioma español.

¿Qué puede hacer Ania?/ Comandos de voz con los que trabaja el asistente:
Ania puede reconocer lo que dice el usuario gracias a la función "listener" y hablar mediante la función "speaker".

-Ania proporciona información sobre el la fecha actual al escuchar: 
    "qué día es hoy"
    "fecha de hoy"

-Ania proporciona información sobre el la hora actual al escuchar:
    "qué hora es"
    "dime la hora"
    "necesito la hora"

-Ania abre YouTube en el navegador al escuchar:
    "abre youtube"

-Ania abre el navegador al escuchar:
    "abre el navegador"

-Ania busca en wikipedia lo que pide el usuario y recita la información al escuchar:
    "busca en wikipedía (pedido del usuario)"
    **ejemplo: "ania, busca en wikipedia información sobre Python"**

-Ania realiza cualquier tipo de búsqueda en internet (abre el navegador y muestra el resultado de búsqueda) al escuchar:
    "busca en internet"
    **ejemplo: busca en internet fotos de perros**

-Ania reproduce un video en YouTube al escuchar:
    "reproduce"
    **ejemplo: ania, reproduce la ultima vez de bandalos chinos**

-Ania cuenta un chiste al escuchar:
    "chiste"

-Ania puede compartir el costo de las acciones de Apple, Google, Microsoft, Amazon, Meta, Nvidia y tesla al escuchar:
    "precio de las acciones de"
    "valor de las acciones de"
    **ejemplo: Ania, dame el precio de las acciones de nvidia**

Para finalizar el asistente basta con decir la palabra "adios" y Ania se despedirá.


Información sobre las funciones del programa: 
-listener: se configura el micrófono y permite convertir la voz del usuario a texto (formato str) gracias a la API de reconocimiento de voz de Google (recognize_google()). Capta la solicitud del usuario.

-speaker: permite convertir el texto (formato str) gracias a la librería pyttsx3 y su metodo "say()".

-start_greeting: realiza un saludo predeterminado al iniciar el programa

-ask_for_day: Proporciona información sobre la fecha actual.

-ask_for_time: Proporciona información sobre la hora actual.

-run_assistant: es la función principal que ejecuta el asistente virtual, permite mantener activado el programa usando un bucle while True que finaliza al escuchar la palabra "adios".
En esta función se define la lógica para recibir las solicitudes del usuario a través del reconocimiento de voz, procesarlas y responder en consecuencia realizando una acción.
Dentro de run_assistant llama a las funciones anteriores y se definen las acciones: abrir YouTube, abrir navegador, buscar en wikipedia, buscar en internet, reproducir en Youtube, contar chiste, buscar precio de acciones de empresas específicas.

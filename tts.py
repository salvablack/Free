from gtts import gTTS

def text_to_speech(text, filename):
    # Crear un objeto gTTS
    tts = gTTS(text=text, lang='es')  # Puedes especificar el idioma aquí
    
    # Guardar la voz generada en un archivo MP3
    tts.save(filename)
    
    print(f"Archivo MP3 guardado como '{filename}'")

# Texto que quieres convertir a voz
texto = input("Introduce el texto que deseas convertir a voz: ")

# Nombre del archivo MP3 de salida
nombre_archivo = input("Introduce el nombre del archivo MP3 de salida (con extensión): ")

# Convertir texto a voz y guardar en archivo MP3
text_to_speech(texto, nombre_archivo)


import cv2

# Ruta al archivo haarcascade_frontalface_default.xml
cascade_path = 'haarcascade_frontalface_default.xml'

# Inicializar el clasificador frontal de Haar
face_cascade = cv2.CascadeClassifier(cascade_path)



# Inicializar la captura de video desde la cámara web externa (cambia el índice 1 a 0 si es tu única cámara)
cap = cv2.VideoCapture(1)

while True:
    # Capturar un fotograma
    ret, frame = cap.read()
    
    # Convertir a escala de grises para la detección de caras
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar caras en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    # Dibujar rectángulos alrededor de las caras detectadas y mostrar el resultado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Mostrar la imagen capturada
    cv2.imshow('Face Detection', frame)
    
    # Detener el bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()

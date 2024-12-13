import streamlit as st
import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Configuración de la app
st.title("Lector de Códigos QR")
st.write("Activa la cámara para escanear un código QR. Cuando se detecte, se mostrará el contenido.")

# Configuración de la cámara
video_capture = st.camera_input("Activa tu cámara")

# Procesar el frame de la cámara
if video_capture:
    # Leer la imagen desde la cámara
    frame = cv2.imdecode(np.frombuffer(video_capture.getvalue(), np.uint8), cv2.IMREAD_COLOR)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Decodificar códigos QR
    qr_codes = decode(frame_rgb)

    # Procesar los resultados
    if qr_codes:
        for qr_code in qr_codes:
            data = qr_code.data.decode("utf-8")
            rect = qr_code.rect
            
            # Dibujar el rectángulo alrededor del código QR
            cv2.rectangle(frame_rgb, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 2)
            
            # Mostrar el contenido
            st.success(f"Código QR Detectado: {data}")
            st.image(frame_rgb, caption="Código QR detectado y capturado", channels="RGB")
    else:
        st.warning("No se detectó ningún código QR.")

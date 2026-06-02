import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# 1. Configuração inicial da página do Streamlit
st.set_page_config(
    page_title="Scanner com Yolo",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título principal da aplicação
st.title("Scanner com YOLO")
st.write("Protótipo leve para detecção de objetos em tempo real via câmera.")

# 2. Inicialização e cache do modelo YOLO para otimização de performance
@st.cache_resource
def load_yolo_model():
    # Carrega a versão nano do YOLOv8 (leve e ideal para deploy no Render)
    return YOLO("yolov8n.pt")

model = load_yolo_model()

# 4. Interface com botão para ativar o acesso à câmera
# O componente 'camera_input' do Streamlit nativamente solicita autorização e abre a câmera
base_cam = st.checkbox("Ativar Câmera", value=False)

if base_cam:
    img_file = st.camera_input("Posicione o objeto em frente à câmera")
    
    # 3. Processamento da imagem capturada e execução da detecção
    if img_file is not None:
        # Converte o arquivo de imagem recebido para o formato PIL
        image = Image.open(img_file)
        
        # Executa a inferência do YOLO na imagem capturada
        results = model(image)
        
        # Renderiza os resultados (caixas delimitadoras e rótulos) na imagem original
        annotated_frame = results[0].plot()
        
        # Exibe o resultado final processado na tela do Streamlit
        st.subheader("Objetos Detectados:")
        st.image(annotated_frame, channels="RGB", use_container_width=True)
else:
    st.info("Clique no checkbox acima para ativar a câmera e iniciar o scanner.")
# projeto-yolo
# Scanner com YOLOv8 & Streamlit

Este é um protótipo educacional de um scanner de objetos em tempo real utilizando a biblioteca **YOLOv8** (Ultralytics) integrada a uma interface web minimalista com **Streamlit**. O projeto foi desenhado especificamente para ser leve, rápido e totalmente compatível com ambientes de deploy em nuvem baseados em instâncias enxutas, como o **Render**.

---

## 🚀 Funcionalidades

* **Detecção em Tempo Real:** Captura de imagens diretamente da câmera do usuário (utilizando a API nativa do Streamlit).
* **Modelo Otimizado:** Uso do modelo pré-treinado `yolov8n.pt` (versão Nano), garantindo baixo consumo de memória RAM e inferência rápida.
* **Interface Fluida:** Layout limpo e responsivo sem componentes ou condicionais redundantes.
* **Pronto para Deploy:** Configurações otimizadas para rodar em servidores Linux sem monitor gráfico (`opencv-python-headless`).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Streamlit** (Interface Web)
* **Ultralytics YOLOv8** (Detecção de Objetos)
* **OpenCV (Headless)** (Processamento de Imagem em Nuvem)
* **PIL (Pillow) & NumPy** (Manipulação de Matrizes e Imagens)

---

## 📦 Como Rodar Localmente

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO

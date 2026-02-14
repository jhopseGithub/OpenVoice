import torch
import os
from openvoice import utils
from openvoice.api import ToneColorConverter, BaseSpeakerTTS

"""
Script de optimización para OpenVoice.
Aplica técnicas de:
1. Inferencia en FP16 (Half Precision) para ahorro de memoria y velocidad.
2. torch.compile para optimización de grafos (PyTorch 2.0+).
3. Uso explícito de dispositivos (CUDA/CPU).
"""

def optimize_model(model, device):
    """
    Aplica optimizaciones de PyTorch al modelo proporcionado.
    """
    if 'cuda' in str(device):
        print(f"[*] Optimizando modelo para {device} (FP16 + torch.compile)")
        model = model.half()  # Convertir a media precisión
    
    # torch.compile está disponible en PyTorch 2.0+ y mejora el rendimiento de ejecución
    try:
        model = torch.compile(model)
        print("[+] torch.compile aplicado exitosamente.")
    except Exception as e:
        print(f"[!] No se pudo aplicar torch.compile: {e}")
    
    return model

def main():
    # Rutas de ejemplo (ajustar según el entorno)
    config_path = 'checkpoints_v2/base_speakers/ses/config.json'
    ckpt_path = 'checkpoints_v2/base_speakers/ses/checkpoint.pth'
    
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"[*] Iniciando optimización en: {device}")

    # Ejemplo de optimización para BaseSpeakerTTS
    if os.path.exists(config_path):
        print("[*] Cargando BaseSpeakerTTS...")
        base_speaker = BaseSpeakerTTS(config_path, device=device)
        base_speaker.load_ckpt(ckpt_path)
        
        # Optimizar el modelo interno
        base_speaker.model = optimize_model(base_speaker.model, device)
        print("[V] BaseSpeakerTTS optimizado.")
    else:
        print(f"[!] Archivo de configuración no encontrado en {config_path}. Omita este paso si no ha descargado los checkpoints.")

    # Ejemplo de optimización para ToneColorConverter
    # converter_config = 'checkpoints_v2/converter/config.json'
    # if os.path.exists(converter_config):
    #     converter = ToneColorConverter(converter_config, device=device)
    #     converter.model = optimize_model(converter.model, device)

if __name__ == "__main__":
    main()

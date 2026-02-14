# Bibliografía y Fundamentación Teórica - OpenVoice

Este documento proporciona la base académica y técnica de OpenVoice, así como las referencias utilizadas para su optimización.

## Referencia Principal
- **Qin, Z., Zhao, W., Yu, X., & Sun, X. (2023).** *OpenVoice: Versatile Instant Voice Cloning*. arXiv preprint arXiv:2312.01479.
  - *Fundamento:* Introduce la arquitectura desacoplada que separa el clonado del color tonal (timbre) del control de estilo y lenguaje.

## Modelos y Arquitecturas Fundacionales
- **Kim, J., Kong, J., & Son, J. (2021).** *Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech (VITS)*. ICML.
  - *Relación:* OpenVoice utiliza VITS y VITS2 como bases para el modelo de "Base Speaker".
- **Kim, J., et al. (2023).** *VITS2: Improving Quality and Efficiency of Single-Stage Text-to-Speech with Adversarial Learning and Transformers*.
  - *Relación:* Mejora la eficiencia y calidad del audio en comparación con VITS.
- **Kim, J., et al. (2020).** *Glow-TTS: A Generative Flow-posture for Text-to-Speech via Monotonic Alignment Search*. NeurIPS.
  - *Relación:* Base para el alineamiento y flujo generativo en TTS.
- **Kong, J., Kim, J., & Bae, J. (2020).** *HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis*. NeurIPS.
  - *Relación:* Utilizado para la vocodificación de alta fidelidad.

## Tecnologías de Optimización
- **Intel Distribution of OpenVINO Toolkit.**
  - *Referencia:* [OpenVINO Documentation](https://docs.openvino.ai/).
  - *Aplicación:* Optimización de la inferencia del Tone Color Converter mediante compresión de pesos y ejecución acelerada.
- **Neural Network Compression Framework (NNCF).**
  - *Referencia:* [NNCF GitHub](https://github.com/openvinotoolkit/nncf).
  - *Aplicación:* Cuantización y poda de modelos para reducir la latencia.

## Modelos Relacionados para Comparación
- **Casanova, E., et al. (2022).** *YourTTS: Towards Zero-Shot Multi-Speaker TTS and Zero-Shot Voice Conversion for everyone*.
- **Le, M., et al. (2023).** *Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale*.

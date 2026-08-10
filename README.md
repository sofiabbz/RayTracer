# Ray Tracer em Python

Um ray tracer construído do zero, sem bibliotecas gráficas — só matemática, Pillow e vontade.

## O que é isso

Ray tracing é a técnica que Pixar, Disney e todo motor de render 3D usa: você dispara "raios" (linhas) da câmera para cada pixel da tela e simula fisicamente como a luz interage com os objetos. O resultado sai renderizado, sem GPU, direto do CPU.

Este projeto reconstrói essa técnica em camadas, uma versão por vez.

## Progressão

| Versão | O que faz | Preview |
|--------|-----------|---------|
| v1 | Esfera colorida + céu | `docs/v1.png` |
| v2 | Iluminação (a esfera ganha volume) | *em breve* |
| v3 | Múltiplas esferas | *em breve* |
| v4 | Sombras | *em breve* |
| v5 | Reflexos | *em breve* |
| v6 | Chão de xadrez | *em breve* |
| v7 | Anti-aliasing | *em breve* |
| v8 | Refração (vidro) | *em breve* |

## Como rodar

```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
python raytracer.py
```

A imagem sai em `output/v1_esfera.png`.

## Referências

- [Ray Tracing in One Weekend](https://raytracing.github.io/books/RayTracingInOneWeekend.html) — o guia clássico
- [Scratchapixel](https://www.scratchapixel.com/) — teoria mais aprofundada

"""
Ray Tracer - Versao 1
Renderiza uma esfera colorida sobre um fundo gradiente (ceu).
"""

from PIL import Image
import math

# Dimensoes da imagem final
LARGURA = 400
ALTURA = 300

# A cena: uma esfera vermelha flutuando na frente da camera
ESFERA_CENTRO = (0, 0, -3)
ESFERA_RAIO = 1.0
ESFERA_COR = (0.9, 0.3, 0.3)


def subtrai(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def produto_escalar(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def normaliza(v):
    tamanho = math.sqrt(produto_escalar(v, v))
    return (v[0] / tamanho, v[1] / tamanho, v[2] / tamanho)


def intersecta_esfera(origem, direcao, centro, raio):
    """
    Verifica se o raio (origem + t * direcao) atinge a esfera.
    Retorna a distancia t se atingir, ou None caso contrario.

    Matematica: a interseccao raio-esfera vira uma equacao quadratica.
    Se o discriminante for negativo, o raio passa longe da esfera.
    """
    oc = subtrai(origem, centro)
    b = produto_escalar(oc, direcao)
    c = produto_escalar(oc, oc) - raio * raio
    discriminante = b * b - c

    if discriminante < 0:
        return None

    t = -b - math.sqrt(discriminante)
    return t if t > 0 else None


def cor_do_pixel(x, y):
    """
    Dispara um raio da camera passando pelo pixel (x, y)
    e retorna a cor RGB que aquele raio "ve".
    """
    # Converte pixel para coordenada da cena (aspect-corrigida)
    u = (x - LARGURA / 2) / ALTURA
    v = -(y - ALTURA / 2) / ALTURA

    origem = (0, 0, 0)
    direcao = normaliza((u, v, -1))

    # O raio atinge a esfera?
    t = intersecta_esfera(origem, direcao, ESFERA_CENTRO, ESFERA_RAIO)
    if t is not None:
        return ESFERA_COR

    # Nao atingiu: pinta o ceu com um gradiente vertical suave
    fator = 0.5 * (direcao[1] + 1)
    return (1 - fator * 0.5, 1 - fator * 0.3, 1)


def renderiza():
    imagem = Image.new("RGB", (LARGURA, ALTURA))
    pixels = []

    for y in range(ALTURA):
        for x in range(LARGURA):
            r, g, b = cor_do_pixel(x, y)
            pixels.append((
                max(0, min(255, int(r * 255))),
                max(0, min(255, int(g * 255))),
                max(0, min(255, int(b * 255))),
            ))

        if y % 30 == 0:
            print(f"Renderizando... {int(100 * y / ALTURA)}%")

    imagem.putdata(pixels)
    imagem.save("output/v1_esfera.png")
    print("Pronto! Imagem salva em output/v1_esfera.png")


if __name__ == "__main__":
    renderiza()

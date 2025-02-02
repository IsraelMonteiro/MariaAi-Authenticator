from PIL import Image, ImageDraw
import os

def adicionar_qr_com_linha(imagem_base_path, imagem_qr_path, output_path):
    """
    Adiciona uma imagem QR no lado direito da imagem base, com uma linha vermelha passando por trás.

    :param imagem_base_path: Caminho para a imagem base.
    :param imagem_qr_path: Caminho para a imagem QR.
    :param output_path: Caminho onde a imagem final será salva.
    """
    try:
        # Abrir a imagem base e a imagem QR
        imagem_base = Image.open(imagem_base_path).convert("RGBA")
        imagem_qr = Image.open(imagem_qr_path).convert("RGBA")

        # Dimensões da imagem base
        base_width, base_height = imagem_base.size

        # Redimensionar o QR Code para se ajustar melhor à imagem base
        qr_tamanho = base_height // 4  # 25% da altura da imagem base
        imagem_qr = imagem_qr.resize((qr_tamanho, qr_tamanho))

        # Dimensões do QR Code
        qr_width, qr_height = imagem_qr.size

        # Posicionar o QR Code no lado direito no meio da imagem
        posicao_qr = (base_width - qr_width - 10, (base_height - qr_height) // 2)

        # Criar uma camada de desenho para adicionar a linha vermelha
        camada = Image.new("RGBA", imagem_base.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(camada)

        # Adicionar uma linha vermelha de cima a baixo no lado direito (por trás do QR)
        linha_x = base_width - qr_width - 10 + qr_width // 2
        draw.line([(linha_x, 0), (linha_x, base_height)], fill="red", width=2)

        # Combinar a linha vermelha com a imagem base
        imagem_com_linha = Image.alpha_composite(imagem_base, camada)

        # Adicionar o QR Code na imagem final
        imagem_com_linha.paste(imagem_qr, posicao_qr, imagem_qr)

        # Converter para RGB para salvar como JPEG
        imagem_final_rgb = imagem_com_linha.convert("RGB")
        imagem_final_rgb.save(output_path, format="JPEG")
        print(f"Imagem com QR salva em: {output_path}")
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Configuração dos caminhos
base_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório do script atual
assets_dir = os.path.join(base_dir, "../assets")  # Pasta assets no mesmo nível de src

# Caminhos para os arquivos de entrada e saída
imagens_base = [
    os.path.join(assets_dir, "MAIAI (MariaAi).JPEG"),
    os.path.join(assets_dir, "CYA (CyaNetAI Token).JPEG"),
    os.path.join(assets_dir, "AIGT (AIgnition Token).JPEG"),
]
imagem_qr = os.path.join(assets_dir, "MariaAi_Network_Logo_com_qr.png")

# Diretório de saída para as imagens resultantes
output_dir = os.path.join(assets_dir, "output")
os.makedirs(output_dir, exist_ok=True)

# Adicionar o QR Code a cada imagem base
for imagem_base_path in imagens_base:
    nome_base = os.path.basename(imagem_base_path)
    output_path = os.path.join(output_dir, f"QR_{nome_base}")
    adicionar_qr_com_linha(imagem_base_path, imagem_qr, output_path)

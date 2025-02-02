from PIL import Image, ImageDraw
import os

def add_qr_with_line(base_image_path, qr_image_path, output_path):
    """
    Adds a QR Code to the right side of a base image, with a red line passing behind it.

    :param base_image_path: Path to the base image.
    :param qr_image_path: Path to the QR Code image.
    :param output_path: Path where the final image will be saved.
    """
    try:
        # Open the base image and the QR Code image
        base_image = Image.open(base_image_path).convert("RGBA")
        qr_image = Image.open(qr_image_path).convert("RGBA")

        # Dimensions of the base image
        base_width, base_height = base_image.size

        # Resize the QR Code to fit better on the base image
        qr_size = base_height // 4  # 25% of the base image height
        qr_image = qr_image.resize((qr_size, qr_size))

        # Dimensions of the QR Code
        qr_width, qr_height = qr_image.size

        # Position the QR Code on the right side, vertically centered
        qr_position = (base_width - qr_width - 10, (base_height - qr_height) // 2)

        # Create a drawing layer to add the red line
        layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(layer)

        # Add a red line from top to bottom on the right side (behind the QR Code)
        line_x = base_width - qr_width - 10 + qr_width // 2
        draw.line([(line_x, 0), (line_x, base_height)], fill="red", width=2)

        # Combine the red line with the base image
        image_with_line = Image.alpha_composite(base_image, layer)

        # Add the QR Code to the final image
        image_with_line.paste(qr_image, qr_position, qr_image)

        # Convert to RGB to save as JPEG
        final_image_rgb = image_with_line.convert("RGB")
        final_image_rgb.save(output_path, format="JPEG")
        print(f"Image with QR saved at: {output_path}")
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Path configuration
base_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
assets_dir = os.path.join(base_dir, "../assets")  # Assets folder at the same level as src

# Input and output file paths
base_images = [
    os.path.join(assets_dir, "MAIAI (MariaAi).JPEG"),
    os.path.join(assets_dir, "CYA (CyaNetAI Token).JPEG"),
    os.path.join(assets_dir, "AIGT (AIgnition Token).JPEG"),
]
qr_image_path = os.path.join(assets_dir, "MariaAi_Network_Logo_com_qr.png")

# Output directory for the processed images
output_dir = os.path.join(assets_dir, "output")
os.makedirs(output_dir, exist_ok=True)

# Add the QR Code to each base image
for base_image_path in base_images:
    base_name = os.path.basename(base_image_path)
    output_path = os.path.join(output_dir, f"QR_{base_name}")
    add_qr_with_line(base_image_path, qr_image_path, output_path)

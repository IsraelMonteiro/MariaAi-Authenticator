from PIL import Image
import qrcode
import os

def create_qr_code(url, size=300):
    """
    Creates a QR Code with custom colors.
    
    :param url: URL to be encoded in the QR Code.
    :param size: Final size of the QR Code in pixels.
    :return: Resized QR Code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create the QR Code with a golden color and transparent background
    qr_img = qr.make_image(fill_color="#FFD700", back_color=None).convert("RGBA")  # "#FFD700" is gold
    return qr_img.resize((size, size))

def center_qr_code(background_image_path, qr_img, output_path):
    """
    Centers a QR Code on a background image and saves the result.

    :param background_image_path: Path to the background image.
    :param qr_img: QR Code image.
    :param output_path: Path where the final image will be saved.
    """
    try:
        # Open the background image
        background = Image.open(background_image_path).convert("RGBA")
        bg_width, bg_height = background.size

        # Dimensions of the QR Code
        qr_width, qr_height = qr_img.size

        # Calculate the position to center the QR Code
        position = ((bg_width - qr_width) // 2, (bg_height - qr_height) // 2)

        # Overlay the QR Code on the background image
        background.paste(qr_img, position, qr_img)

        # Save the final image
        background.save(output_path)
        print(f"QR Code generated and saved at: {output_path}")
    except FileNotFoundError:
        print(f"Error: Background file not found at '{background_image_path}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def save_transparent_qr(qr_img, output_path):
    """
    Saves the QR Code with a transparent background as a PNG file.
    
    :param qr_img: QR Code image.
    :param output_path: Path where the QR Code will be saved.
    """
    try:
        qr_img.save(output_path, format="PNG")
        print(f"Transparent QR Code saved at: {output_path}")
    except Exception as e:
        print(f"Error saving transparent QR Code: {e}")


# Path configuration and URL
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Base path of the project
assets_dir = os.path.join(base_dir, "assets")  # Path to the assets folder

# File paths
background_image = os.path.join(assets_dir, "MariaAi_Network_Logo.jpeg")
output_image = os.path.join(assets_dir, "MariaAi_Network_Logo_with_qr.png")
output_transparent_qr = os.path.join(assets_dir, "MariaAi_Network_QR_transparent.png")
url = "https://mariaai.fun"

# Ensure the output directory exists
os.makedirs(assets_dir, exist_ok=True)

# Generate the QR Code with a transparent background
qr_code = create_qr_code(url)

# Save the transparent QR Code
save_transparent_qr(qr_code, output_transparent_qr)

# Center the QR Code on the background image
center_qr_code(background_image, qr_code, output_image)

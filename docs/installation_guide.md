# Installation Guide for MariaAi Authenticator

Welcome to the **MariaAi Authenticator** project! Follow this guide to set up and run the project in your local environment. This document provides step-by-step instructions to ensure you can start using the Secure QR Generator and image authentication tools effectively.

---

## **Prerequisites**

Before installing the project, ensure the following tools are installed on your system:

1. **Python**: Version 3.8 or higher.
2. **Poetry**: Used for managing project dependencies and environments.
   - Install Poetry using:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```
3. **Git**: Required to clone the repository.
4. **Dependencies**: The required libraries (`Pillow`, `qrcode`) are included in the project dependencies.

---

## **Setup Instructions**

### **1. Clone the Repository**

Clone the MariaAi Authenticator repository from GitHub to your local machine:
```bash
git clone https://github.com/IsraelMonteiro/MariaAi-Authenticator
```
Navigate to the project directory:
```bash
cd mariaai-authenticator
```

---

### **2. Install Dependencies**

The project uses **Poetry** to manage dependencies. Install them with:
```bash
poetry install
```

Activate the virtual environment:
```bash
poetry shell
```

---

### **3. Project Structure**

Below is the directory structure of the project:

```
SyaNet_AI_Integration_MVP/
├── docs/                      # Documentation files
│   ├── installation_guide.md  # Installation guide
│   └── README.md              # Project overview
├── poetry.lock                # Poetry lock file for dependencies
├── pyproject.toml             # Project and dependencies configuration
├── pytest.ini                 # Pytest configuration file
├── requirements.txt           # Dependency list (alternative to Poetry)
├── src/                       # Main source code
│   ├── assets/                # Input and processed images
│   │   ├── AIGT (AIgnition Token).JPEG
│   │   ├── CYA (CyaNetAI Token).JPEG
│   │   ├── MAIAI (MariaAi).JPEG
│   │   ├── MariaAi_Network_Logo.jpeg
│   │   ├── MariaAi_Network_Logo_com_qr.png
│   │   └── output/            # Processed images
│   ├── main/                  # Core scripts
│   │   ├── adicionar_qr_imagens.py  # Adds QR Codes to images
│   │   ├── qr_mariai.py            # Generates custom QR Codes
│   │   ├── cyanet_ai/              # Functions related to CyaNet
│   │   ├── icp/                    # ICP integration
│   │   └── image_processing/       # Image processing functions
│   ├── utils/                 # Utility functions
│   │   ├── blockchain.py      # Blockchain integration
│   │   ├── qr_generator.py    # QR Code generator
│   │   └── security_tools.py  # Security tools
│   └── tests/                 # Automated tests
│       ├── test_basic.py      # Basic tests
│       ├── test_core.py       # Core tests
│       ├── test_image_processing.py  # Image processing tests
│       └── ...                # Additional test scripts
├── static/                    # Static files (CSS, JS)
├── uploads/                   # User-uploaded files
└── ...
```

---

### **4. Run the Project**

#### **Generate a QR Code**
To generate a QR Code and embed it into an image, run the following script:
```bash
python src/main/qr_mariai.py
```

#### **Authenticate Images with QR Code**
To add a QR Code to existing images with additional visual authentication, run:
```bash
python src/main/adicionar_qr_imagens.py
```

---

### **5. Output**

The generated QR Codes and authenticated images will be saved in the `src/assets/output/` directory.

---

## **Troubleshooting**

- **Missing Dependencies**: If you encounter errors like `ModuleNotFoundError`, ensure dependencies are installed by running:
  ```bash
  poetry install
  ```

- **Path Issues**: Ensure all paths to assets and scripts are correctly configured relative to the root directory.

- **Image Format Errors**: Ensure that input images are in supported formats (e.g., `.jpeg`, `.png`).

---

## **Additional Resources**

For more details, visit:
- 🌐 **Official Website**: [https://mariaai.fun](https://mariaai.fun)
- 💬 **Telegram**: [https://t.me/mariaAi18y](https://t.me/mariaAi18y)
- 🐦 **Twitter (X)**: [https://x.com/MariaAi18y](https://x.com/MariaAi18y)

---

## **Contributing**

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

**Developed with 💡 by MariaAI**


# PyQt5 Image Processing with OCR and Search

**Description**

This PyQt5 application provides image processing tools, OCR (Optical Character Recognition) capabilities, and a text-based search feature to highlight matching text within images. ✨

**Features**

*   **Image Loading:** Supports common image formats (JPEG, PNG) and PDF files. 🖼️
*   **OCR:** Extracts text from images using Tesseract OCR. 📖
*   **Text Search and Highlight:**  Allows users to search for text within an image and highlights matching occurrences. 🔍

**Getting Started**

**Prerequisites**

*   Python 3.x
*   PyQt5
*   OpenCV (cv2)
*   Pytesseract
*   pdf2image
*   Pillow (PIL)

**Installation**

1.  **Install Tesseract OCR:**  Follow the instructions based on your operating system (https://linuxhint.com/install_tesseract_windows/)

2.  **Install Python libraries:**

    ```bash
    pip install PyQt5 opencv-python pytesseract pdf2image Pillow
    ```

**Usage**

1.  Run the application (assuming your main Python file is `OCR_size.py`):

    ```bash
    python OCR_size.py 
    ```

2.  **Select an image:** Click the "Choose Image" button to select an image or PDF file.

3.  **Perform OCR (optional):** Click the "OCR" button to extract all text from the image.

4.  **Search for text:**
    *   Enter text into the search field.
    *   Click "Search" (or equivalent) to highlight matching text within the image.

**Dependencies**

*   **PyQt5:** GUI framework.
*   **OpenCV (cv2):** Image processing and manipulation.
*   **Pytesseract:** OCR engine.
*   **pdf2image:** Conversion of PDF files to images.
*   **Pillow (PIL):** Additional image processing support.

**Notes**

*   Ensure the Tesseract OCR executable is in the correct path or modify the `pytesseract.pytesseract.tesseract_cmd` line in your code.


**Let me know if you have more specifics about how you want the Dockerized version of your app to function, and I'll refine the Dockerfile further!**


**Contact**

[9nounqwerty@gmail.com/email for questions or feedback]


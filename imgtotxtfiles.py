# from PIL import Image
# import pytesseract 
# print("giuhiu")

# img1 = r"C:\Users\priyasekar\Pictures\pics\Screenshotsample.png"
# text = pytesseract.image_to_string(Image.open(img1))

# print(text)

import os
from PIL import Image
import pytesseract
from tkinter import Tk, filedialog

# Function to select an image file
def select_image():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    return file_path

def select_output_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(
        title="Select Output File",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    return file_path

def main():
    # Select an image
    image_path = select_image()
    if not image_path:
        print("No image selected. Exiting.")
        return

    # Convert image to text
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        print("Text extracted from image:")
        print(text)
    except Exception as e:
        print(f"An error occurred during text extraction: {e}")
        return

    # Select output file
    output_file_path = select_output_file()
    if not output_file_path:
        print("No output file selected. Exiting.")
        return

    # Save text to the selected file
    try:
        with open(output_file_path, "w") as text_file:
            text_file.write(text)
        print(f"Text saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    main()

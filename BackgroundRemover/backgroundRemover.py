import sys
import os
from PIL import Image
from rembg import remove
from rembg import remove as rembg_remove

def remove_background(input_image_path, output_image_path):
    with open(input_image_path, "rb") as input_file:
        input_image = input_file.read()
        output_image = rembg_remove(input_image)
        with open(output_image_path, "wb") as output_file:
            output_file.write(output_image)

def main():
    if len(sys.argv) != 3:
        print("Usage: python background_remover.py <input_image> <output_image>")
        return

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    if not os.path.isfile(input_image_path):
        print(f"Error: File '{input_image_path}' does not exist.")
        return

    try:
        Image.open(input_image_path)
    except IOError:
        print("Error: The input file is not a valid image.")
        return

    remove_background(input_image_path, output_image_path)
    print(f"Background removed successfully. Saved output as '{output_image_path}'.")

if __name__ == "__main__":
    main()

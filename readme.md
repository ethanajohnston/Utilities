# Ethan's Useful Utilities

### TextToCSVConverter
  
This script reads data from an input text file, processes it, and writes the output to a CSV file. It defines a function split_into_columns() to split each line in the input file into columns based on whitespace. The script also changes the working directory to the script's directory, ensuring that the input and output files are read and written from the correct location. It also prints a message to the console, indicating that the processing is complete and the resulting CSV file has been saved.

I used it for formatting a bunch of S parameters of a transistor from a provided .dat file into data which could be used in matlab.

### Background Remover

The script removes the background from images in common file formats such as JPEG, PNG, and BMP. It leverages the rembg library to perform background removal and provides an easy-to-use command-line interface. The resolution is not reduced.

To use the utility:

1. Ensure you have Python installed on your system.
2. Install the required rembg library using pip install rembg.
3. Save the provided Python script as background_remover.py.
4. Open a terminal and navigate to the directory containing the script.
5. Run the command: python background_remover.py <input_image> <output_image>, replacing <input_image> with the path to the image you want to process and <output_image> with the desired path for the image with the background removed.
6. After running the command, the script will remove the background from the input image and save the result to the specified output path.

example: python backgroundRemover.py input.jpg C:/Users/ethan/Desktop/output_image.png
# ASCII art generation in Python suing the Pillow module

<h4>Details about the repository:- </h4>This repository focuses on the generation of ascii art on the basis of the images which is given as the input to the program. It uses the Pillow module and array of strings that are mapped according to the dim or bright pixels to portray the input images in the form of ASCII character.

# Image to ASCII Art Converter

This Python program converts images into ASCII art using a range of ASCII characters to represent pixel brightness. The result is a text-based image that mimics the original photo in a simplified form.

## Features
- Converts any image to a grayscale ASCII art format.
- Supports image resizing while maintaining the aspect ratio.
- Utilizes a wide range of ASCII characters for better detail and contrast.
- Saves the output as a text file.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ascii-art-converter.git
   cd ascii-art-converter
   ```

2. **Install the Dependencies**:
   This program requires the Python Imaging Library (PIL), which is part of the `Pillow` package.
   Install it using pip:
   ```bash
   pip install pillow
   ```

## Usage

1. Place the image you want to convert in the project folder.
2. Modify the `image_path` variable in the script to point to your image file:
   ```python
   image_path = "your_image.jpg"
   ```
3. Run the Python script:
   ```bash
   python ascii_art_converter.py
   ```

4. The ASCII art will be saved as `output_ascii_art.txt` in the project directory.

### Example:
To convert an image named `example.jpg`:
```python
image_path = "example.jpg"
```

### Output:
The ASCII art is saved in `output_ascii_art.txt` and can be viewed in any text editor.

## Customization

- **Adjust Width**: You can modify the width of the ASCII output by changing the `new_width` parameter in the `image_to_ascii()` function:
   ```python
   image_to_ascii(image_path, new_width=150)
   ```

- **Character Set**: You can adjust the range of ASCII characters for different styles:
   ```python
   ASCII_CHARS = ["@", "#", "$", "%", "&", "*", "+", ":", ".", " "]
   ```

## License

This project is licensed under the MIT License.

---

Replace `yourusername` with your GitHub username and customize the example image name as needed. This should give users a clear idea of what the project does and how to use it!

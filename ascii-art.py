from PIL import Image

# A wider range of ASCII characters for better detail
ASCII_CHARS = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]

def resize_image(image, new_width=120):
    """Resize the image while maintaining the aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Adjust for better aspect ratio
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """Convert the image to grayscale."""
    return image.convert("L")

def map_pixels_to_ascii(image):
    """Map grayscale pixels to ASCII characters."""
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])  # Dividing by 25 to map pixel values (0-255) to ASCII chars
    return ascii_str

def image_to_ascii(image_path, new_width=120):
    """Convert an image to ASCII art."""
    image = Image.open(image_path)

    # Resize the image
    image = resize_image(image, new_width)
    
    # Convert image to grayscale
    image = grayscale_image(image)
    
    # Convert pixels to ASCII characters
    ascii_str = map_pixels_to_ascii(image)
    
    # Format the ASCII string into lines of the correct width
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:(i + img_width)] for i in range(0, ascii_str_len, img_width)])
    
    return ascii_img

def save_ascii_art(ascii_art, output_file):
    """Save the ASCII art to a file."""
    with open(output_file, "w") as f:
        f.write(ascii_art)

# Path to your image
image_path = r"C://Users/7/Documents/coding_tutorial/DSA/Practice/image_file.png"
# Convert the image to ASCII
ascii_art = image_to_ascii(image_path)
# Save the ASCII art to a file
save_ascii_art(ascii_art, "output_ascii_art.txt")

print("ASCII art saved to output_ascii_art.txt")

from PIL import Image
import os

ASCII_CHARS = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]

if(os.path.exists('sample.png')):
    def resize_image(image, new_width=120):
        width, height = image.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.55)
        resized_image = image.resize((new_width, new_height))
        return resized_image

    def grayscale_image(image):
        return image.convert("L")

    def map_pixels_to_ascii(image):
        pixels = image.getdata()
        ascii_str = "".join([ASCII_CHARS[pixel // 26] for pixel in pixels])  # Fixed the range issue
        return ascii_str

    def image_to_ascii(image_path, new_width=120):
        image = Image.open(image_path)
        image = resize_image(image, new_width)
        image = grayscale_image(image)
        ascii_str = map_pixels_to_ascii(image)
        img_width = image.width
        ascii_str_len = len(ascii_str)
        ascii_img = "\n".join([ascii_str[i:(i + img_width)] for i in range(0, ascii_str_len, img_width)])
        return ascii_img

    def save_ascii_art(ascii_art, output_file):
        with open(output_file, "w") as f:
            f.write(ascii_art)

    image_path = r"sample.jpg"
    ascii_art = image_to_ascii(image_path)
    save_ascii_art(ascii_art, "output_ascii_art.txt")

    print("ASCII art saved to output_ascii_art.txt")

else:
    print("The image file (sample.jpg) doesn't exist in this directory...")
from PIL import Image

# Load the provided image
# img_path = '/mnt/data/something.jpg' # set in env var
img = Image.open(img_path)

output_width = 80
# Calculate the appropriate height to maintain aspect ratio
aspect_ratio = img.height / img.width
output_height = int(aspect_ratio * output_width * 0.55)

# Resize the image
img = img.resize((output_width, output_height))
img = img.convert('L')  # Convert to grayscale

# ASCII characters from light to dark
ascii_chars = " .:-=+*#%@"

# Map pixels to ASCII chars
pixels = img.getdata()
ascii_str = ""
for i, pixel in enumerate(pixels):
    ascii_str += ascii_chars[pixel * len(ascii_chars) // 256]
    if (i + 1) % output_width == 0:
        ascii_str += "\n"

print(ascii_str)
